import type { NextConfig } from "next";
import path from "path";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  outputFileTracingRoot: path.join(__dirname, "../../"),
  transpilePackages: ["@mono-reader/shared"],
  async rewrites() {
    const apiPort = process.env.API_PORT || "3001";
    const apiUrl = process.env.API_URL || `http://127.0.0.1:${apiPort}`;
    return [
      {
        source: "/api/:path*",
        destination: `${apiUrl}/api/:path*`,
      },
    ];
  },
};

export default nextConfig;
