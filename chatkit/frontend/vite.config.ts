import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

const backendTarget = "http://127.0.0.1:8000";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: "0.0.0.0",
    proxy: {
      "/chatkit": {
        target: backendTarget,
        changeOrigin: true,
      },
    },
  },
});