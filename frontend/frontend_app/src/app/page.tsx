'use client';

import { useState } from 'react';
import toast from 'react-hot-toast';
import SearchBar from '@/components/SearchBar';
import SearchResultsList from '@/components/SearchResultsList';
import LoadingSpinner from '@/components/LoadingSpinner';
import ErrorMessage from '@/components/ErrorMessage';
import { searchWikipedia } from '@/lib/api';
import { WikipediaSearchSuggestion } from '@/types';
import { SearchIcon } from 'lucide-react';

export default function HomePage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [results, setResults] = useState<WikipediaSearchSuggestion[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (term: string) => {
    setSearchTerm(term);
    setIsLoading(true);
    setError(null);
    setHasSearched(true);
    try {
      const searchData = await searchWikipedia(term);
      setResults(searchData.suggestions);
      if (searchData.suggestions.length === 0) {
        toast.success('Search complete. No articles found for your term.');
      } else {
        toast.success(`Found ${searchData.suggestions.length} suggestion(s).`);
      }
    } catch (err) {
      console.error("Search failed:", err);
      const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred during search.';
      setError(errorMessage);
      toast.error(`Search failed: ${errorMessage}`);
      setResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">Explore Wikipedia</h1>
        <p className="text-lg text-gray-600">
          Enter a term to search for articles on Wikipedia.
        </p>
      </div>

      <SearchBar onSearch={handleSearch} isLoading={isLoading} />

      {isLoading && (
        <div className="mt-6">
          <LoadingSpinner />
        </div>
      )}

      {error && (
        <div className="mt-6">
          <ErrorMessage message={error} />
        </div>
      )}

      {hasSearched && !isLoading && !error && (
        <div className="mt-6">
          <h2 className="text-2xl font-semibold text-gray-700 mb-4">
            Search Results for "{searchTerm}"
          </h2>
          <SearchResultsList results={results} />
        </div>
      )}

      {!hasSearched && !isLoading && (
        <div className="mt-10 text-center text-gray-500">
          <SearchIcon size={48} className="mx-auto mb-4" />
          <p>Enter a search term above to find Wikipedia articles.</p>
        </div>
      )}
    </div>
  );
}
