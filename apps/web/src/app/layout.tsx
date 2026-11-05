import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Leitor Monocromático — Experiência Editorial Pura em E-Ink",
  description: "Sistema de leitura focado, minimalista e cognitivo em camadas sem distrações visuais.",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR" data-theme="eink" data-font="serif">
      <body className="min-h-screen transition-colors duration-200">
        {children}
      </body>
    </html>
  );
}
