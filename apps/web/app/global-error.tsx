"use client";

import { useEffect } from "react";

export default function GlobalError({ error, reset }: { error: Error & { digest?: string }; reset: () => void }) {
  useEffect(() => { console.error("Global application error:", error); }, [error]);
  return <html lang="en"><body><main style={{ display: "grid", minHeight: "100vh", placeItems: "center", padding: "1.5rem", fontFamily: "Arial, sans-serif", textAlign: "center" }}><div><h1>Something went wrong</h1><p>Please try again.</p><button onClick={reset} type="button">Try again</button></div></main></body></html>;
}