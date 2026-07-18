import type { Config } from "tailwindcss";
export default { content:["./app/**/*.{ts,tsx}","./components/**/*.{ts,tsx}"], theme:{extend:{colors:{canvas:"#07090d",surface:"#0d1118",line:"#1d2635",ink:"#ecf3ff",muted:"#8290a5",signal:"#66e3c4",violet:"#9476ff",danger:"#ff6577"},boxShadow:{glow:"0 0 40px rgba(102,227,196,.10)"}}}, plugins:[] } satisfies Config;
