import { NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";

async function handleProxy(
  req: NextRequest,
  { params }: { params: Promise<{ path: string[] }> }
) {
  const { path } = await params;
  const pathStr = Array.isArray(path) ? path.join("/") : path;
  const searchParams = req.nextUrl.search;

  // Em produção no Railway, usa API_URL ou o domínio público da API criada
  const fallbackUrl =
    process.env.NODE_ENV === "development"
      ? "http://127.0.0.1:3001"
      : "https://mono-readerapi-production.up.railway.app";

  const targetBase = process.env.API_URL || fallbackUrl;
  const targetUrl = `${targetBase.replace(/\/$/, "")}/api/${pathStr}${searchParams}`;

  const headers = new Headers(req.headers);
  headers.delete("host");
  headers.delete("connection");

  try {
    const isBodyAllowed = req.method !== "GET" && req.method !== "HEAD";
    const body = isBodyAllowed ? await req.arrayBuffer() : undefined;

    const response = await fetch(targetUrl, {
      method: req.method,
      headers,
      body,
      // @ts-ignore
      duplex: "half",
      cache: "no-store",
    });

    const responseHeaders = new Headers(response.headers);
    responseHeaders.set("Access-Control-Allow-Origin", "*");

    return new NextResponse(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: responseHeaders,
    });
  } catch (error: any) {
    console.error(`[API Proxy Error] Falha ao conectar em ${targetUrl}:`, error);
    return NextResponse.json(
      {
        error: "Falha na comunicação com o serviço de API",
        target: targetUrl,
        details: error?.message || String(error),
      },
      { status: 502 }
    );
  }
}

export const GET = handleProxy;
export const POST = handleProxy;
export const PUT = handleProxy;
export const DELETE = handleProxy;
export const PATCH = handleProxy;
export const OPTIONS = handleProxy;
