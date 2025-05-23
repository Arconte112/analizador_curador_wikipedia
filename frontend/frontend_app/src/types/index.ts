export interface WikipediaSearchSuggestion {
  title: string;
  page_id?: string;
}

export interface WikipediaSearchResult {
  suggestions: WikipediaSearchSuggestion[];
}

export interface ArticleAnalysis {
  word_count: number;
  frequent_words: Record<string, number>;
}

export interface ArticleDetail {
  title: string;
  processed_summary: string;
  analysis: ArticleAnalysis;
  original_url: string;
}

export interface SavedArticle {
  id: number;
  title_wikipedia: string;
  url_wikipedia: string;
  summary_processed?: string | null;
  frequent_words?: Record<string, number> | null;
  word_count?: number | null;
  saved_at: string; // ISO datetime string
}

export type SavedArticleCreatePayload = Omit<SavedArticle, "id" | "saved_at">;
