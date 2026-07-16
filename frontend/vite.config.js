import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],

  server: {
    proxy: {
      "/api": {
        target: "https://fictional-dollop-x54pwrp6qq96hv7vp-8000.app.github.dev",
        changeOrigin: true,
        secure: true,
      },
    },
  },
});