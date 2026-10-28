import { defineConfig } from 'astro/config';

export default defineConfig({
  trailingSlash: 'always',
  build: { format: 'directory' },
});
