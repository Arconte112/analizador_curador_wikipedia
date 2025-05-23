import Link from 'next/link';
import { WikipediaSearchSuggestion } from '@/types';
import { BookOpen } from 'lucide-react';

interface SearchResultsListProps {
  results: WikipediaSearchSuggestion[];
}

const SearchResultsList: React.FC<SearchResultsListProps> = ({ results }) => {
  if (results.length === 0) {
    return <p className="text-gray-500">No results found.</p>;
  }

  return (
    <ul className="space-y-2">
      {results.map((suggestion) => (
        <li key={suggestion.title} className="border p-3 rounded-md hover:bg-gray-50">
          <Link href={`/article/${encodeURIComponent(suggestion.title)}`} className="flex items-center space-x-2 text-blue-600 hover:text-blue-800">
            <BookOpen size={18} />
            <span>{suggestion.title}</span>
          </Link>
        </li>
      ))}
    </ul>
  );
};

export default SearchResultsList;
