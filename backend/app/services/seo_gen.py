"""
SEO meta tags generation service
"""

from typing import Dict, List


class SEOGenerator:
    """Service for generating SEO meta tags"""
    
    @staticmethod
    def generate_meta_tags(
        business_name: str,
        industry: str,
        tagline: str = None
    ) -> Dict[str, any]:
        """
        Generate SEO meta tags for a business
        
        Args:
            business_name: Name of the business
            industry: Industry/niche
            tagline: Optional tagline
            
        Returns:
            Dictionary containing SEO meta tags
        """
        # Generate title (max 60 chars)
        title = f"{business_name} - {industry} Services"
        if len(title) > 60:
            title = f"{business_name} | {industry}"
            if len(title) > 60:
                title = f"{business_name[:57]}..."
        
        # Generate description (max 160 chars)
        description = f"{business_name} provides professional {industry} services. "
        if tagline:
            description += f"{tagline} "
        description += "Contact us today for more information."
        
        if len(description) > 160:
            description = description[:157] + "..."
        
        # Generate keywords
        keywords = [
            industry.lower(),
            business_name.lower(),
            f"{industry.lower()} services",
            f"professional {industry.lower()}",
            f"{business_name.lower()} {industry.lower()}"
        ]
        
        # Open Graph tags
        og_title = business_name
        og_description = f"Discover {business_name} for all your {industry} needs"
        
        # JSON-LD structured data
        json_ld = f'''{{
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "{business_name}",
            "description": "{industry}",
            "url": "https://{business_name.lower().replace(' ', '')}.com"
        }}'''
        
        return {
            "title": title,
            "description": description,
            "keywords": keywords,
            "og_title": og_title,
            "og_description": og_description,
            "json_ld": json_ld
        }
