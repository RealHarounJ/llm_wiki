import zipfile
import xml.etree.ElementTree as ET
import re
import os

pptx_path = r"c:\Users\jaafa\Downloads\llm_wiki-main\raw\group 11.pptx"
output_path = r"c:\Users\jaafa\Downloads\llm_wiki-main\raw\group_11_extracted.txt"

def extract_text_from_pptx(pptx_file):
    texts = []
    with zipfile.ZipFile(pptx_file, 'r') as archive:
        # Find all slide files
        slide_files = sorted(
            [f for f in archive.namelist() if re.match(r'ppt/slides/slide\d+\.xml', f)],
            key=lambda x: int(re.search(r'\d+', x).group())
        )
        
        for slide_file in slide_files:
            slide_num = re.search(r'\d+', slide_file).group()
            slide_text = []
            xml_content = archive.read(slide_file)
            root = ET.fromstring(xml_content)
            
            # Extract text from all <a:t> elements
            namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
            for t_elem in root.findall('.//a:t', namespaces):
                if t_elem.text:
                    text_val = t_elem.text.strip()
                    if text_val:
                        slide_text.append(text_val)
            
            texts.append(f"=== SLIDE {slide_num} ===\n" + "\n".join(slide_text) + "\n")
            
    return "\n".join(texts)

try:
    extracted_text = extract_text_from_pptx(pptx_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(extracted_text)
    print("Success! Extracted text written to group_11_extracted.txt")
except Exception as e:
    print(f"Error: {e}")
