import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// The entry image is the invitation letter in entry.png: a watercolour
// letter-paper background (letter-paper-bg2.png) with the letter text
// typeset onto it by draw_letter.py (PIL, DejaVu Serif), so every word
// is legible and correctly spelled. This program copies it, byte for
// byte, to the output directory the harness grades.
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
if (!existsSync(source)) throw new Error("entry.png is missing from the repository");
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync(source, dest);

// Verify the output the gate will check: a whole PNG, 1024x1024,
// at most 1 MiB. PNG signature is 8 bytes; IHDR (width, height) sits
// at bytes 16..24, big-endian.
const buf = readFileSync(dest);
const PNG_SIG = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!buf.subarray(0, 8).equals(PNG_SIG)) throw new Error("output is not a PNG");
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
const bytes = statSync(dest).size;
if (width !== 1024 || height !== 1024) {
  throw new Error(`output is ${width}x${height}, expected 1024x1024`);
}
if (bytes > 1048576) throw new Error(`output is ${bytes} bytes, over the 1 MiB gate`);
console.log(`wrote ${dest}: ${width}x${height} PNG, ${bytes} bytes`);
