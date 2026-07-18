import Link from "next/link";

export default function NotFound() {
  return (
    <main className="grid min-h-screen place-items-center p-6 text-center">
      <div>
        <p className="eyebrow mb-3">ChainScribe Enterprise</p>
        <h1 className="text-3xl font-semibold">Page not found</h1>
        <p className="mt-3 text-sm text-muted">The page you requested does not exist or is no longer available.</p>
        <Link className="mt-6 inline-block rounded-lg bg-ink px-4 py-2 text-sm font-semibold text-canvas" href="/">Return to dashboard</Link>
      </div>
    </main>
  );
}