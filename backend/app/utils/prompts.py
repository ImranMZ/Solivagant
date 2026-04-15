"""AI prompt templates for Groq API"""

LOGO_PROMPT_TEMPLATE = """Create a minimalist and professional logo design description for {business_name}, a company in the {industry} industry.
The logo should be:
- {style} in style
- {color_scheme} color scheme
- Clean, modern, and memorable
- Suitable for web and print

Provide a detailed description of the logo design."""

WEBSITE_CONTENT_PROMPT = """Generate engaging and professional website copy for {business_name}.
Tagline: {tagline}
Industry: {industry}

Create:
1. A compelling hero section headline
2. Three features/benefits
3. A call-to-action
4. Footer tagline

Format as JSON with keys: hero_headline, features, cta, footer_tagline"""

SEO_PROMPT_TEMPLATE = """Generate SEO metadata for a website for {business_name}.
Tagline: {tagline}
Industry: {industry}

Create:
1. Meta title (max 60 chars)
2. Meta description (max 160 chars)
3. Keywords (5-8 relevant keywords)

Format as JSON with keys: title, description, keywords"""
