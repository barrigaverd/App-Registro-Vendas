import flet as ft

class StationeryTheme:
    # Color Palette - Elegant, Light, Professional Feminine
    PRIMARY = "#E5989B"       # Soft Rose / Pastel Pink
    SECONDARY = "#FFCDD2"     # Very Light Pink
    BACKGROUND = "#FAFAFA"    # Soft White (Paper-like)
    SURFACE = "#FFFFFF"       # Pure White Cards
    
    # Text Colors - High Contrast but soft
    TEXT_PRIMARY = "#374151"  # Slate 700 (Softer than pure black)
    TEXT_SECONDARY = "#6B7280" # Slate 500
    TEXT_ACCENT = "#B5838D"    # Muted Mauve
    
    # Borders & Accents
    BORDER_LIGHT = "#F3F4F6"  # Gray 100
    ERROR = "#EF4444"         # Red 500 (standard for errors)
    SUCCESS = "#4CAF82"       # Soft Mint Green (confirmação elegante)
    
    # Typography
    HEADING_FONT = "Cormorant Infant"
    BODY_FONT = "Outfit"
    ACCENT_FONT = "Great Vibes"
    
    @staticmethod
    def get_theme():
        return ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=StationeryTheme.PRIMARY,
                surface=StationeryTheme.BACKGROUND,
                on_surface=StationeryTheme.TEXT_PRIMARY,
                secondary=StationeryTheme.SECONDARY,
                on_secondary=StationeryTheme.TEXT_PRIMARY,
                error=StationeryTheme.ERROR,
            ),
            font_family=StationeryTheme.BODY_FONT
        )
    
    @staticmethod
    def get_fonts():
        return {
            "Cormorant Infant": "https://fonts.googleapis.com/css2?family=Cormorant+Infant:wght@400;600;700&display=swap",
            "Outfit": "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&display=swap",
            "Great Vibes": "https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap"
        }
