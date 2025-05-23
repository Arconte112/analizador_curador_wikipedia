'use client';

import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import toast from 'react-hot-toast';
import { getWikipediaArticleDetails, saveArticle, getSavedArticles } from '@/lib/api';
import { ArticleDetail as ArticleDetailType, SavedArticleCreatePayload, SavedArticle } from '@/types';
import ArticleDisplay from '@/components/ArticleDisplay';
import LoadingSpinner from '@/components/LoadingSpinner';
import ErrorMessage from '@/components/ErrorMessage';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

export default function ArticleDetailPage() {
  const params = useParams();
  const title = params.title ? decodeURIComponent(params.title as string) : null;

  const [article, setArticle] = useState<ArticleDetailType | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isSaving, setIsSaving] = useState(false);
  const [isAlreadySaved, setIsAlreadySaved] = useState(false);

  useEffect(() => {
    if (title) {
      const fetchArticle = async () => {
        setIsLoading(true);
        setError(null);
        try {
          const articleData = await getWikipediaArticleDetails(title);
          setArticle(articleData);
          // Check if article is already saved
          const savedArticles = await getSavedArticles();
          if (savedArticles.some(sa => sa.url_wikipedia === articleData.original_url)) {
            setIsAlreadySaved(true);
          }
        } catch (err) {
          console.error("Failed to fetch article details:", err);
          const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred.';
          setError(`Failed to load article: ${errorMessage}`);
          toast.error(`Error: ${errorMessage}`);
        } finally {
          setIsLoading(false);
        }
      };
      fetchArticle();
    } else {
      setError("Article title not found in URL.");
      setIsLoading(false);
    }
  }, [title]);

  const handleSaveArticle = async () => {
    if (!article) return;
    setIsSaving(true);
    try {
      const payload: SavedArticleCreatePayload = {
        title_wikipedia: article.title,
        url_wikipedia: article.original_url,
        summary_processed: article.processed_summary,
        frequent_words: article.analysis.frequent_words,
        word_count: article.analysis.word_count,
      };
      await saveArticle(payload);
      toast.success('Article saved successfully!');
      setIsAlreadySaved(true);
    } catch (err) {
      console.error("Failed to save article:", err);
      const errorMessage = err instanceof Error ? err.message : 'Could not save the article.';
      toast.error(`Save failed: ${errorMessage}`);
    } finally {
      setIsSaving(false);
    }
  };

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <LoadingSpinner />
        <p className="mt-2 text-gray-600">Loading article details...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center">
        <ErrorMessage message={error} />
        <Link href="/" className="mt-4 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700">
          <ArrowLeft size={18} className="mr-2" />
          Back to Search
        </Link>
      </div>
    );
  }

  if (!article) {
    return (
      <div className="text-center">
        <ErrorMessage message="Article data could not be loaded." />
         <Link href="/" className="mt-4 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700">
          <ArrowLeft size={18} className="mr-2" />
          Back to Search
        </Link>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <Link href="/" className="inline-flex items-center text-blue-600 hover:text-blue-800 mb-4 group">
        <ArrowLeft size={20} className="mr-1 group-hover:-translate-x-1 transition-transform" />
        Back to Search Results
      </Link>
      <ArticleDisplay 
        article={article} 
        onSave={handleSaveArticle} 
        isSaving={isSaving}
        isSaved={isAlreadySaved}
      />
    </div>
  );
}
