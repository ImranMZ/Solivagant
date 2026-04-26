"""
Vibe configurations for AI-powered website generation.
Extracted from website_gen_ai.py for modularity.
"""

VIBES = {
    "premium": {
        "name": "Premium",
        "description": "Luxury, sophisticated, high-end aesthetic",
        "personality": "elegant, exclusive, refined",
        "layout_style": "spacious, cinematic, dramatic",
        "font_tier": "editorial",
    },
    "playful": {
        "name": "Playful",
        "description": "Fun, energetic, approachable design",
        "personality": "friendly, creative, dynamic",
        "layout_style": "bouncy, colorful, asymmetrical",
        "font_tier": "rounded",
    },
    "professional": {
        "name": "Professional",
        "description": "Trustworthy, corporate, reliable",
        "personality": "serious, dependable, expert",
        "layout_style": "structured, balanced, clean",
        "font_tier": "sans-serif",
    },
    "minimal": {
        "name": "Minimal",
        "description": "Clean, focused, modern simplicity",
        "personality": "pure, essential, contemporary",
        "layout_style": "bare, breathable, intentional",
        "font_tier": "geometric",
    },
    "bold": {
        "name": "Bold",
        "description": "Attention-grabbing, confident, memorable",
        "personality": "strong, assertive, distinctive",
        "layout_style": "striking, oversized, high-contrast",
        "font_tier": "display",
    },
}


def get_vibe_config(vibe_key: str) -> dict:
    """Get vibe config by key, defaulting to professional."""
    return VIBES.get(vibe_key, VIBES["professional"])


def list_vibes() -> list[dict]:
    """Return list of vibe definitions for API display."""
    return [
        {"key": k, "name": v["name"], "description": v["description"]}
        for k, v in VIBES.items()
    ]
