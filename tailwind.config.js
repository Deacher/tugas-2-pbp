/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./item_inventory/**/*.{html,js}', './static/**/*.{html,js}', './templates/**/*.{html,js}', './main/**/*.{html,js}', "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
  },
  plugins: [require('flowbite/plugin')],
}

