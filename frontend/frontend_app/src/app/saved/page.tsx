'use client';

import { useEffect, useState } from 'react';
import toast from 'react-hot-toast';
import { getSavedArticles, deleteSavedArticle } from '@/lib/api';
import { SavedArticle } from '@/types';
import SavedArticleCard from '@/components/SavedArticleCard';
import LoadingSpinner from '@/components/LoadingSpinner';
import ErrorMessage from '@/components/ErrorMessage';
import { ListX, Archive } from 'lucide-react';

export default function SavedArticlesPage() {
  const [savedArticles, setSavedArticles] = useState<SavedArticle[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);

  const fetchSavedArticles = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const articles = await getSavedArticles();
      setSavedArticles(articles.sort((a, b) => new Date(b.saved_at).getTime() - new Date(a.saved_at).getTime()));
    } catch (err) {
      console.error("Failed to fetch saved articles:", err);
      const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred.';
      setError(`Failed to load saved articles: ${errorMessage}`);
      toast.error(`Error: ${errorMessage}`);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchSavedArticles();
  }, []);

  const handleDeleteArticle = async (articleId: number) => {
    setDeletingId(articleId);
    try {
      await deleteSavedArticle(articleId);
      toast.success('Article deleted successfully!');
      // Refetch or filter out the deleted article
      setSavedArticles(prevArticles => prevArticles.filter(article => article.id !== articleId));
    } catch (err) {
      console.error("Failed to delete article:", err);
      const errorMessage = err instanceof Error ? err.message : 'Could not delete the article.';
      toast.error(`Delete failed: ${errorMessage}`);
    } finally {
      setDeletingId(null);
    }
  };

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <LoadingSpinner />
        <p className="mt-2 text-gray-600">Loading saved articles...</p>
      </div>
    );
  }

  if (error) {
    return <ErrorMessage message={error} />;
  }

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-gray-800 mb-6 flex items-center">
        <Archive size={30} className="mr-3 text-indigo-600" />
        My Saved Articles
      </h1>
      {savedArticles.length === 0 ? (
        <div className="text-center text-gray-500 py-10">
          <ListX size={48} className="mx-auto mb-4" />
          <p>You haven't saved any articles yet.</p>
          <p>Search for articles and save them to see them here.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {savedArticles.map(article => (
            <SavedArticleCard 
              key={article.id} 
              article={article} 
              onDelete={handleDeleteArticle}
              isDeleting={deletingId === article.id}
            />
          ))}
        </div>
      )}
    </div>
  );
}
