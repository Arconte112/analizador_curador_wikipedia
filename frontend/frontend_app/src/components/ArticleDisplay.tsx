import { ArticleDetail } from '@/types';
import { ExternalLink, BarChart2, FileText, Save } from 'lucide-react';

interface ArticleDisplayProps {
  article: ArticleDetail;
  onSave: () => void;
  isSaving?: boolean;
  isSaved?: boolean;
}

const ArticleDisplay: React.FC<ArticleDisplayProps> = ({ article, onSave, isSaving, isSaved }) => {
  return (
    <div className="p-4 border rounded-lg shadow-sm bg-white">
      <div className="flex justify-between items-start mb-4">
        <h1 className="text-3xl font-bold text-gray-800">{article.title}</h1>
        <button
          onClick={onSave}
          disabled={isSaving || isSaved}
          className="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 px-4 rounded-lg flex items-center space-x-2 transition duration-150 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isSaving ? (
            <div className="animate-spin rounded-full h-5 w-5 border-t-2 border-b-2 border-white"></div>
          ) : (
            <Save size={20} />
          )}
          <span>{isSaved ? 'Saved' : isSaving ? 'Saving...' : 'Save Article'}</span>
        </button>
      </div>

      <a
        href={article.original_url}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center space-x-1 text-sm text-blue-600 hover:text-blue-800 hover:underline mb-4"
      >
        <ExternalLink size={16} />
        <span>View on Wikipedia</span>
      </a>

      <div className="mb-6">
        <h2 className="text-xl font-semibold text-gray-700 mb-2 flex items-center">
          <FileText size={22} className="mr-2 text-indigo-600" />
          Processed Summary
        </h2>
        <p className="text-gray-600 leading-relaxed whitespace-pre-wrap">{article.processed_summary}</p>
      </div>

      <div>
        <h2 className="text-xl font-semibold text-gray-700 mb-3 flex items-center">
          <BarChart2 size={22} className="mr-2 text-indigo-600" />
          Text Analysis
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-gray-50 p-4 rounded-lg">
            <h3 className="text-md font-medium text-gray-600 mb-1">Word Count</h3>
            <p className="text-2xl font-semibold text-gray-800">{article.analysis.word_count}</p>
          </div>
          <div className="bg-gray-50 p-4 rounded-lg">
            <h3 className="text-md font-medium text-gray-600 mb-2">Most Frequent Words</h3>
            {Object.entries(article.analysis.frequent_words).length > 0 ? (
              <ul className="list-disc list-inside space-y-1">
                {Object.entries(article.analysis.frequent_words).map(([word, count]) => (
                  <li key={word} className="text-sm text-gray-700">
                    <span className="font-medium">{word}:</span> {count}
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-sm text-gray-500">No frequent words data available.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArticleDisplay;
