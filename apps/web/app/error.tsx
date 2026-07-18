"use client";

import { useEffect } from "react";

export default function Error({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  useEffect(() => { console.error("Route error:", error); }, [error]);
  return <main className="grid min-h-screen place-items-center p-6 text-center"><div><p className="eyebrow mb-3">ChainScribe Enterprise</p><h1 className="text-3xl font-semibold">Something went wrong</h1><p className="mt-3 text-sm text-muted">Please try loading this page again.</p><button className="mt-6 rounded-lg bg-ink px-4 py-2 text-sm font-semibold text-canvas" onClick={reset} type="button">Try again</button></div></main>;
}