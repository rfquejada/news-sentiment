function Article({ article }) {
  return (
    <li className="bg-white shadow-md rounded-lg overflow-hidden max-w-sm w-full">
      <img 
        src={article.image_url} 
        alt={article.title} 
        className="w-full h-48 object-cover"
      />
      <div className="p-4">
        <h2 className="font-bold text-xl mb-2 text-gray-800">{article.title}</h2>
        <p className="text-gray-700 mb-4">{article.description}</p>
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