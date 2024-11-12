module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',  // Agrega esta línea para que Tailwind procese todas las plantillas de las apps de Django
    './**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}