import CardArticle from "./Article";

function ArticleGrid({ articles }) {
  if (!articles || articles.length === 0) {
    return (
      <p className="text-center text-gray-600">No articles found.</p>
    );
  }

  return (
    <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-4">
      {articles.map((article, idx) => (
        <CardArticle key={idx} article={article} />
      ))}
    </ul>
  );
}

export default ArticleGrid;