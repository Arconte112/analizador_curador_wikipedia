'use client';

import Link from 'next/link';
import { SavedArticle } from '@/types';
import { Trash2, ExternalLink, FileText } from 'lucide-react';

interface SavedArticleCardProps {
  article: SavedArticle;
  onDelete: (articleId: number) => void;
  isDeleting?: boolean;
}

const SavedArticleCard: React.FC<SavedArticleCardProps> = ({ article, onDelete, isDeleting }) => {
  const handleDelete = () => {
    if (window.confirm(`Are you sure you want to delete "${article.title_wikipedia}"?`)) {
      onDelete(article.id);
    }
  };

  return (
    <div className="border p-4 rounded-lg shadow-sm bg-white hover:shadow-md transition-shadow">
      <div className="flex justify-between items-start mb-2">
        <Link href={`/article/${encodeURIComponent(article.title_wikipedia)}`} className="text-xl font-semibold text-blue-700 hover:text-blue-900 hover:underline">
          {article.title_wikipedia}
        </Link>
        <button
          onClick={handleDelete}
          disabled={isDeleting}
          className="text-red-500 hover:text-red-700 disabled:opacity-50 p-1"
          aria-label="Delete article"
        >
          {isDeleting ? (
            <div className="animate-spin rounded-full h-5 w-5 border-t-2 border-b-2 border-red-500"></div>
          ) : (
            <Trash2 size={20} />
          )}
        </button>
      </div>
      
      {article.summary_processed && (
        <p className="text-sm text-gray-600 mb-3 line-clamp-3">
          <FileText size={14} className="inline mr-1 align-text-bottom" />
          {article.summary_processed}
        </p>
      )}

      <div className="flex items-center justify-between text-xs text-gray-500">
        <a
          href={article.url_wikipedia}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center space-x-1 hover:text-blue-600 hover:underline"
        >
          <ExternalLink size={12} />
          <span>View on Wikipedia</span>
        </a>
        <span>Saved: {new Date(article.saved_at).toLocaleDateString()}</span>
      </div>
    </div>
  );
};

export default SavedArticleCard;
