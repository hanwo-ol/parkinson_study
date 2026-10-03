import os
import json
import random
import re
import urllib.request
import pymupdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPERS_JSON = os.path.join(BASE_DIR, "data", "papers_index.json")
STUDY_GUIDES_DIR = os.path.join(BASE_DIR, "study_guides")
PDF_DIR = os.path.join(BASE_DIR, "downloaded_pdfs")

os.makedirs(STUDY_GUIDES_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

def load_papers():
    with open(PAPERS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def get_next_study_number():
    existing_files = os.listdir(STUDY_GUIDES_DIR)
    numbers = []
    for f in existing_files:
        m = re.match(r"^(\d{4})_", f)
        if m:
            numbers.append(int(m.group(1)))
    next_num = max(numbers) + 1 if numbers else 1
    return f"{next_num:04d}"

def pick_random_paper():
    papers = load_papers()
    selected = random.choice(papers)
    next_id = get_next_study_number()
    print(f"Next Study Guide Number: #{next_id}")
    print(f"Selected paper: {selected['filename']}")
    print(f"Google Drive ID: {selected['file_id']}")
    return selected

def download_paper(paper):
    filename = paper["filename"]
    file_id = paper["file_id"]
    pdf_path = os.path.join(PDF_DIR, filename)
    if os.path.exists(pdf_path):
        print(f"File already exists: {pdf_path}")
        return pdf_path
    
    url = f"https://drive.google.com/uc?id={file_id}&export=download"
    print(f"Downloading from {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        with open(pdf_path, "wb") as f:
            f.write(data)
    print(f"Downloaded {len(data)} bytes to {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    p = pick_random_paper()
    # download_paper(p)
