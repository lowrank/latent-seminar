import fs from "fs";
import path from "path";
import matter from "gray-matter";

const CONTENT_DIR = "./content";
const EXCLUDE = ["templates"];
const OUTPUT = "tmp/tagData.json";

function collectTags(dirPath: string): Record<string, number> {
  const tagCounts: Record<string, number> = {};

  const walk = (dir: string) => {
    const files = fs.readdirSync(dir);
    for (const file of files) {
      const fullPath = path.join(dir, file);
      const relPath = path.relative(CONTENT_DIR, fullPath);
      if (EXCLUDE.some(ex => relPath.split(path.sep).includes(ex))) continue;

      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        walk(fullPath);
      } else if (file.endsWith(".md")) {
        const content = fs.readFileSync(fullPath, "utf8");
        const { data } = matter(content);
        if (Array.isArray(data.tags)) {
          data.tags.forEach(tag => {
            tagCounts[tag] = (tagCounts[tag] || 0) + 1;
          });
        }
      }
    }
  };

  walk(dirPath);
  return tagCounts;
}

const tagData = collectTags(CONTENT_DIR);
fs.writeFileSync(OUTPUT, JSON.stringify(tagData, null, 2));
console.log("✅ Tag data saved to:", OUTPUT);
