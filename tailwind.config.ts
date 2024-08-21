import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        "mac-yellow": "#F9B83E",
        "mac-light-yellow": "#f3c761",
        "mac-red": "#850044",
        "mac-light-red": "#9B406D",
        "mac-dark-red": "#740232",
        "mac-grey": "#535f65",
        "mac-light-grey": "#ececec",
        "mac-off-white": "#F6F7F8",
      },
    },
  },
  plugins: [],
};
export default config;
