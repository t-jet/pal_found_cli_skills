import { defineConfig } from "vite";
import foundryWidgetPlugin from "@osdk/widget.vite-plugin";
export default defineConfig({
  plugins: [foundryWidgetPlugin()],
  build: { rollupOptions: { input: ["./counter.html", "./summary.html"] } },
});
