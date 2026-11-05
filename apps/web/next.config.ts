import type { NextConfig } from "next";
import path from "path";

const API_DEST = process.env.NEXT_PUBLIC_API_URL || "https://mono-readerapi-production.up.railway.app";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  outputFileTracingRoot: path.join(__dirname, "../../"),
  transpilePackages: ["@mono-reader/shared"],
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: `${API_DEST}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
