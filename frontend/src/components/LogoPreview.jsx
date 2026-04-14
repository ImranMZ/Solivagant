import { motion } from 'framer-motion';

const LogoPreview = ({ logoUrl, businessName }) => {
  if (!logoUrl) return null;

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
      className="bg-white rounded-lg shadow-lg p-6 text-center"
    >
      <h3 className="text-xl font-bold mb-4 text-gray-800">Your Logo</h3>
      <div className="mb-4">
        <img
          src={logoUrl}
          alt={`${businessName} logo`}
          className="max-w-full h-auto max-h-64 mx-auto rounded-lg"
        />
      </div>
      <a
        href={logoUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors"
      >
        Download Logo
      </a>
    </motion.div>
  );
};

export default LogoPreview;
