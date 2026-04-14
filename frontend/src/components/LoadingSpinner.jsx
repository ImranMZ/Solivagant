import { motion } from 'framer-motion';

const LoadingSpinner = () => {
  return (
    <div className="flex flex-col items-center justify-center p-8">
      <motion.div
        className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full"
        animate={{ rotate: 360 }}
        transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
      />
      <p className="mt-4 text-lg text-gray-600">Generating your brand...</p>
      <p className="text-sm text-gray-500">This may take up to 30 seconds</p>
    </div>
  );
};

export default LoadingSpinner;
