import { motion } from 'framer-motion';

const ColorSwatch = ({ color, name }) => (
  <div className="text-center">
    <div
      className="w-16 h-16 rounded-lg shadow-md mx-auto mb-2 border border-gray-200"
      style={{ backgroundColor: color }}
    />
    <p className="text-xs text-gray-600">{name}</p>
    <p className="text-xs font-mono text-gray-500">{color}</p>
  </div>
);

const SEOCard = ({ seoTags }) => {
  if (!seoTags) return null;

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    alert('Copied to clipboard!');
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="bg-white rounded-lg shadow-lg p-6"
    >
      <h3 className="text-xl font-bold mb-4 text-gray-800">SEO Meta Tags</h3>
      
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Title Tag</label>
          <div className="mt-1 flex">
            <input
              type="text"
              value={seoTags.title}
              readOnly
              className="flex-1 p-2 border border-gray-300 rounded-l-lg bg-gray-50 text-sm"
            />
            <button
              onClick={() => copyToClipboard(seoTags.title)}
              className="px-4 py-2 bg-blue-600 text-white rounded-r-lg hover:bg-blue-700 text-sm"
            >
              Copy
            </button>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Meta Description</label>
          <div className="mt-1 flex">
            <textarea
              value={seoTags.description}
              readOnly
              rows={2}
              className="flex-1 p-2 border border-gray-300 rounded-l-lg bg-gray-50 text-sm"
            />
            <button
              onClick={() => copyToClipboard(seoTags.description)}
              className="px-4 py-2 bg-blue-600 text-white rounded-r-lg hover:bg-blue-700 text-sm"
            >
              Copy
            </button>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Keywords</label>
          <div className="mt-1 flex flex-wrap gap-2">
            {seoTags.keywords?.map((keyword, index) => (
              <span
                key={index}
                className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm"
              >
                {keyword}
              </span>
            ))}
          </div>
        </div>
      </div>
    </motion.div>
  );
};

export { ColorSwatch, SEOCard };
