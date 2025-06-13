import CardArticle from "./Article";

function ArticleGrid({ articles }) {
  if (!articles || articles.length === 0) {
    return (
      <p className="text-center text-gray-600">No articles found.</p>
    );
  }

  return (
    <div className="w-full flex justify-center px-8 py-6">
      <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 max-w-7xl w-full justify-items-center">
        {articles.map((article, idx) => (
          <CardArticle key={idx} article={article} />
        ))}
      </ul>
    </div>
  );
}

export default ArticleGrid;