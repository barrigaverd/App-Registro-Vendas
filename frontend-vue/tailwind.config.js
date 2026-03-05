/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#E5989B',
        secondary: '#FFCDD2',
        background: '#FAF3F0',
        surface: '#FFFFFF',
        error: '#D32F2F',
        success: '#4CAF50',
        text: {
          primary: '#374151',
          secondary: '#6B7280'
        }
      },
      fontFamily: {
        heading: ['Cormorant Infant', 'serif'],
        accent: ['Great Vibes', 'cursive'],
        body: ['Outfit', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
