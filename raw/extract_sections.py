import os

input_file = r'c:\Users\Haroun_Jaafar\Desktop\llm_wiki\raw\Corporate finance.md'
output_dir = r'c:\Users\Haroun_Jaafar\Desktop\llm_wiki\raw\extracted'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to find headers or keywords
import re

# Split by common header patterns like "Chapter X" or "Topic X" or something similar
# Looking at the content, it seems to have "Chapter 1", "Chapter 29", "Chapter 30", "Chapter 2", "Chapter 6"
sections = re.split(r'(Chapter \d+|Topic \d+)', content)

for i in range(1, len(sections), 2):
    header = sections[i]
    body = sections[i+1] if i+1 < len(sections) else ""
    filename = header.replace(" ", "_") + ".md"
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"# {header}\n\n{body.strip()}")

print(f"Extracted {len(sections)//2} sections.")
