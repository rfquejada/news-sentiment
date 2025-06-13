function Article({ article }) {
  // Helper function to get sentiment color classes
  const getSentimentColor = (sentiment) => {
    switch (sentiment?.toLowerCase()) {
      case 'positive':
        return 'text-green-600 bg-green-100';
      case 'negative':
        return 'text-red-600 bg-red-100';
      case 'neutral':
        return 'text-yellow-600 bg-yellow-100';
      default:
        return 'text-gray-600 bg-gray-100';
    }
  };

  return (
    <li className="bg-white shadow-md rounded-lg overflow-hidden max-w-sm w-full">
      <img 
        src={article.image_url} 
        alt={article.title} 
        className="w-full h-48 object-cover"
      />
      <div className="p-4">
        <div className="flex justify-between items-start mb-2">
          <span className="text-sm text-gray-500">
            {article.pubDate}
          </span>
          {article.sentiment && (
            <span className={`px-2 py-1 rounded-full text-xs font-medium ${getSentimentColor(article.sentiment)}`}>
              {article.sentiment}
            </span>
          )}
        </div>
        
        <h2 className="font-bold text-xl mb-2 text-gray-800">{article.title}</h2>
        <p className="text-gray-700 mb-4 line-clamp-3">{article.description}</p>
        
        {article.sentiment_score !== undefined && (
          <div className="mb-4">
            <span className="text-sm text-gray-600">
              Sentiment Score: <span className="font-medium">{article.sentiment_score.toFixed(2)}</span>
            </span>
          </div>
        )}
        
        <a 
          href={article.link} 
          target="_blank" 
          rel="noreferrer" 
          className="text-blue-500 hover:text-blue-700 font-medium"
        >
          Read more
        </a>
      </div>
    </li>
  );
}

export default Article;