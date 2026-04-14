import { motion } from 'framer-motion';

const WebsitePreview = ({ content, colors }) => {
  if (!content) return null;

  const htmlContent = `
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>${content.headline}</title>
        <style>
          * { margin: 0; padding: 0; box-sizing: border-box; }
          body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
          .hero { 
            background: ${colors?.primary || '#3B82F6'}; 
            color: white; 
            padding: 4rem 2rem; 
            text-align: center;
          }
          .hero h1 { font-size: 2.5rem; margin-bottom: 1rem; }
          .hero p { font-size: 1.25rem; margin-bottom: 2rem; }
          .cta-button {
            background: ${colors?.accent || '#60A5FA'};
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 0.5rem;
            font-size: 1.1rem;
            cursor: pointer;
          }
          .section { padding: 3rem 2rem; max-width: 1200px; margin: 0 auto; }
          .features { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 2rem;
            margin-top: 2rem;
          }
          .feature-card {
            background: ${colors?.background || '#FFFFFF'};
            padding: 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
          }
          .about { background: ${colors?.secondary || '#1E40AF'}; color: white; }
          .contact { text-align: center; }
        </style>
      </head>
      <body>
        <div class="hero">
          <h1>${content.headline}</h1>
          <p>${content.subheadline}</p>
          <button class="cta-button">${content.cta_text}</button>
        </div>
        
        <div class="section about">
          <h2>About Us</h2>
          <p style="margin-top: 1rem;">${content.about_section}</p>
        </div>
        
        <div class="section">
          <h2>Our Features</h2>
          <div class="features">
            ${(content.features || []).map(feature => `
              <div class="feature-card">
                <h3 style="color: ${colors?.primary || '#3B82F6'}">${feature}</h3>
              </div>
            `).join('')}
          </div>
        </div>
        
        <div class="section contact">
          <h2>Contact Us</h2>
          <p style="margin-top: 1rem;">Email: ${content.contact_email}</p>
        </div>
      </body>
    </html>
  `;

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="bg-white rounded-lg shadow-lg overflow-hidden"
    >
      <h3 className="text-xl font-bold p-4 bg-gray-50 border-b">Website Preview</h3>
      <iframe
        srcDoc={htmlContent}
        title="Website Preview"
        className="w-full h-[600px] border-0"
        sandbox="allow-scripts"
      />
    </motion.div>
  );
};

export default WebsitePreview;
