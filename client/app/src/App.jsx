import { useState, useEffect } from 'react';
import axios from 'axios';
import ArticleGrid from './components/ArticleGrid';

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  let [articles, setArticles] = useState([]);
  let [totalArticles, setTotalArticles] = useState([]);
  const [sentimentFilter, setSentimentFilter] = useState(null);

  const API_BASE_URL = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchArticles = async () => {
      setLoading(true);

      const params = {};
      if (sentimentFilter === "positive") params.isPositive = true;
      else if (sentimentFilter === "negative") params.isNegative = true;
      else if (sentimentFilter === "neutral") params.isNeutral = true;

      try {
        const response = await axios.get(`${API_BASE_URL}/api/fetch-news-articles`, {
          params
        });

        setArticles(response.data.articles);
        setTotalArticles(response.data.total_articles);
      } catch (err) {
        console.error("Error fetching news: ", err);
      }

      setLoading(false);
    };

    fetchArticles();
    console.log(articles);
  }, [sentimentFilter]);

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center px-4 py-8">
      <div className="w-full flex flex-col items-center">
        <h1 className="text-3xl font-bold text-gray-800 mb-8 text-center">
          Latest Philippine News with Sentiment Analyzer
        </h1>
        <div className="flex justify-center flex-wrap gap-2 mb-8">
          <button
            onClick={() => setSentimentFilter(null)}
            className={`px-4 py-2 rounded-md font-medium transition-colors ${
              sentimentFilter === null
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
            }`}
          >
            All
          </button>
          <button
            onClick={() => setSentimentFilter("positive")}
            className={`px-4 py-2 rounded-md font-medium transition-colors ${
              sentimentFilter === "positive"
                ? 'bg-green-600 text-white'
                : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
            }`}
          >
            Positive
          </button>
          <button
            onClick={() => setSentimentFilter("negative")}
            className={`px-4 py-2 rounded-md font-medium transition-colors ${
              sentimentFilter === "negative"
                ? 'bg-red-600 text-white'
                : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
            }`}
          >
            Negative
          </button>
          <button
            onClick={() => setSentimentFilter("neutral")}
            className={`px-4 py-2 rounded-md font-medium transition-colors ${
              sentimentFilter === "neutral"
                ? 'bg-yellow-500 text-white'
                : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
            }`}
          >
            Neutral
          </button>
        </div>

        {loading ? (
          <p className="text-center">Loading...</p>
        ) : error ? (
          <p className="text-red-500 text-center">{error}</p>
        ) : (
          <div className="w-full">
            <ArticleGrid articles={articles} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;