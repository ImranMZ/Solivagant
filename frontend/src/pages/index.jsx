'use client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { motion } from 'framer-motion';
import { generateBrand } from '../utils/api';
import LoadingSpinner from '../components/LoadingSpinner';
import LogoPreview from '../components/LogoPreview';
import WebsitePreview from '../components/WebsitePreview';
import { SEOCard } from '../components/SEOCard';

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = async (data) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await generateBrand(data);
      setResult(response);
    } catch (err) {
      setError('Failed to generate brand. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-white">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold text-gray-900">
            AI Brand Generator
          </h1>
          <p className="mt-2 text-gray-600">
            Create complete brand identities in seconds
          </p>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        {/* Input Form */}
        {!result && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="max-w-2xl mx-auto"
          >
            <div className="bg-white rounded-lg shadow-lg p-8">
              <h2 className="text-2xl font-bold mb-6">Tell us about your business</h2>
              
              <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Business Name *
                  </label>
                  <input
                    type="text"
                    {...register('business_name', { required: 'Business name is required' })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="e.g., TechStart"
                  />
                  {errors.business_name && (
                    <p className="mt-1 text-sm text-red-600">{errors.business_name.message}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Industry/Niche *
                  </label>
                  <input
                    type="text"
                    {...register('industry', { required: 'Industry is required' })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="e.g., Software Development"
                  />
                  {errors.industry && (
                    <p className="mt-1 text-sm text-red-600">{errors.industry.message}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Brand Style
                  </label>
                  <select
                    {...register('style')}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="minimalist">Minimalist</option>
                    <option value="modern">Modern</option>
                    <option value="playful">Playful</option>
                    <option value="professional">Professional</option>
                    <option value="bold">Bold</option>
                    <option value="elegant">Elegant</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Color Scheme (Optional)
                  </label>
                  <input
                    type="text"
                    {...register('color_scheme')}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="e.g., blue and white, warm colors"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Tagline (Optional)
                  </label>
                  <input
                    type="text"
                    {...register('tagline')}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="e.g., Innovating the Future"
                  />
                </div>

                <button
                  type="submit"
                  disabled={loading}
                  className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
                >
                  {loading ? 'Generating...' : 'Generate My Brand'}
                </button>
              </form>

              {error && (
                <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
                  <p className="text-red-600">{error}</p>
                </div>
              )}
            </div>
          </motion.div>
        )}

        {/* Loading State */}
        {loading && <LoadingSpinner />}

        {/* Results */}
        {result && !loading && (
          <div className="space-y-8">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-bold">Your Brand Kit</h2>
              <button
                onClick={() => setResult(null)}
                className="px-4 py-2 text-blue-600 hover:text-blue-800"
              >
                ← Generate Another
              </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {/* Logo */}
              <LogoPreview logoUrl={result.logo?.url} businessName={result.business_name} />

              {/* Color Palette */}
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5 }}
                className="bg-white rounded-lg shadow-lg p-6"
              >
                <h3 className="text-xl font-bold mb-4 text-gray-800">Color Palette</h3>
                <div className="grid grid-cols-5 gap-4">
                  {Object.entries(result.colors || {}).map(([name, color]) => (
                    <div key={name} className="text-center">
                      <div
                        className="w-16 h-16 rounded-lg shadow-md mx-auto mb-2 border border-gray-200"
                        style={{ backgroundColor: color }}
                      />
                      <p className="text-xs text-gray-600 capitalize">{name}</p>
                      <p className="text-xs font-mono text-gray-500">{color}</p>
                    </div>
                  ))}
                </div>
              </motion.div>
            </div>

            {/* Website Preview */}
            <WebsitePreview content={result.website_content} colors={result.colors} />

            {/* SEO Tags */}
            <SEOCard seoTags={result.seo_tags} />
          </div>
        )}
      </main>
    </div>
  );
}
