import re

file_path = r"c:\Users\jaafa\Downloads\llm_wiki-main\raw\Corporate finance.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "tax" AND "agency" AND "efficiency" in close proximity, or specific terms like "tax argument"
print(f"Total content length: {len(content)}")

# Find all matches of words like "tax", "agency", "efficiency" near each other
# Let's define a regex that looks for sentences containing "tax" and "agency" and "efficiency" within 1000 characters
pattern = re.compile(r"(?i)(?:tax|agency|efficiency).{0,500}(?:tax|agency|efficiency).{0,500}(?:tax|agency|efficiency)")
matches = list(pattern.finditer(content))
print(f"Found {len(matches)} proximity matches.")

for i, m in enumerate(matches[:20]):
    start = max(0, m.start() - 200)
    end = min(len(content), m.end() + 200)
    print(f"\n--- Match {i+1} at index {m.start()} ---")
    print(content[start:end].strip().replace("\n", " "))
