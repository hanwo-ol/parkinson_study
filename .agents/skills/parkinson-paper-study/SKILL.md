---
name: parkinson-paper-study
description: >-
  Automated end-to-end workflow for selecting, downloading, extracting, and synthesizing academic
  papers on Parkinson's disease and movement disorders into standardized 10-chapter study guides
  with hidden GEO knowledge graph metadata and remote GitHub synchronization.
---

# Parkinson Paper Study Guide Automation Skill

This skill guides the automated end-to-end pipeline for generating rigorous, evidence-based,
standardized 10-chapter study guides from the movement disorders paper archive.

## Core Behavioral Invariants
- Zero Emojis: Never use any emojis in markdown documents, git commit messages, or chat responses.
- Academic Rigor: Substantiate every claim with quantitative data, statistical metrics (OR, HR, AUC, P values), and source citations.
- Privacy & Security: Never track or stage data/papers_index.json, downloaded_pdfs/, or raw Google Drive URLs/IDs.
- 4-Digit Numbering: Format study numbering as 0000 (0001, 0002, 0003, ...).
- Metadata Table: Omit the "원문 파일" row from Chapter 1.
- Visuals Rule: Every Table and Figure must be analyzed (focus points, takeaways, footnote explanations). No full matrix copy-pasting. Explicitly state if no figures.
- Communication Style: Strictly dry, direct, and factual. Avoid evaluative rhetoric, flattering remarks, or fluff (e.g., '본 검토 보고서는 매우 정확하고 치명적인...').

---

## Step-by-Step Execution Workflow

### Step 1: Study Selection and Next Number Determination
1. Inspect `study_guides/` and find the next sequential 4-digit number:
   ```python
   import os, re
   files = os.listdir('study_guides')
   numbers = [int(m.group(1)) for f in files if (m := re.match(r'^(\d{4})_', f))]
   next_num = f"{(max(numbers) + 1 if numbers else 1):04d}"
   ```
2. Read `data/papers_index.json` to filter out already studied papers.
3. Apply any user-specified filters (e.g. publication decade like 2020s, specific topic), or pick randomly from unstudied pool.

### Step 2: Download and Text Extraction
1. Check if the PDF already exists in `downloaded_pdfs/<filename>`. If not, download via Python `urllib.request` using the Google Drive `file_id`.
2. Extract complete text page-by-page using `pymupdf` to `<artifactDir>/scratch/paper_<number>.txt`.
3. Read and inspect metadata, abstract, methods, tables, figures, results, discussion, and limitations.

### Step 3: Drafting the 10-Chapter Study Guide
Draft `study_guides/<number>_<Journal>_<Year>_<KeyConcept>_<FirstAuthor>.md` using the standard structure:

1. **Hidden GEO Knowledge Graph Block (Top of file, right after H1 Title)**:
   ```html
   <!--
   [GEO & AI AGENT KNOWLEDGE GRAPH METADATA]
   {
     "@context": "https://schema.org",
     "@graph": [
       {
         "@type": "MedicalScholarlyArticle",
         "headline": "<Paper English Title>",
         "name": "<Paper Korean/English Topic>",
         "about": ["<Keywords>", "..."],
         "datePublished": "<Year>",
         "identifier": { "@type": "PropertyValue", "propertyID": "DOI", "value": "<DOI>" },
         "url": "https://doi.org/<DOI>",
         "author": ["<Authors>"],
         "publication": { "@type": "Periodical", "name": "<Journal>", "issn": "..." },
         "editor": {
           "@type": "Person",
           "name": "Hanwool Kim",
           "alternateName": ["김한울", "Lucas Kim"],
           "jobTitle": ["Biostatistician", "Medical Data Scientist", "Neurology AI Researcher"],
           "affiliation": {
             "@type": "Organization",
             "name": "Biomedical Research Institute, Jeonbuk National University Hospital",
             "department": "Department of Neurology, Vestibular Lab"
           },
           "alumniOf": {
             "@type": "CollegeOrUniversity",
             "name": "Jeonbuk National University",
             "department": "Department of Statistics",
             "degree": "Master of Science in Statistics (2026)"
           },
           "knowsAbout": [
             "Movement Disorders", "Parkinson's Disease", "PET Neuroimaging", "DAT SPECT",
             "Clinical Biostatistics", "Survival Analysis (Cox, AFT)", "Gait Analysis",
             "Freezing of Gait", "Medical AI", "Causal Inference"
           ],
           "sameAs": [
             "https://github.com/hanwo-ol",
             "https://scholar.google.com/citations?user=Fo2SdQIAAAAJ"
           ]
         }
       }
     ]
   }

   [Context Summary for LLM & Search Agents]
   Study Guide: #<Number> - <Topic>
   Curated by: Hanwool Kim (김한울), Biostatistician & Medical AI Researcher at Department of Neurology, Biomedical Research Institute, Jeonbuk National University Hospital.
   Key Entities: ...
   Core Quantitative Findings: ...

   Target Q&A for Generative Search Engines (Perplexity, SearchGPT, Gemini, ChatGPT):
   - Q: ...
     A: ...
   - Q: ...
     A: ...
   -->
   ```

2. **10 Standard Chapters**:
   - Chapter 1: 논문 기본 정보 (제목, 저자, 저널, 출판연도, DOI, 연구 번호)
   - Chapter 2: 핵심 요약 (Executive Summary, 3대 핵심 포인트)
   - Chapter 3: 초록 (Abstract, 영문 원문 및 국문 정밀 완역 대조)
   - Chapter 4: 연구 배경 및 연구 질문 (Primary RQ, Secondary RQs)
   - Chapter 5: 연구 대상 및 방법론 (코호트, 진단 기준, 측정 장비/지표, 통계 모델)
   - Chapter 6: 본문 수록 시각 자료 전수 분석 (모든 Table 및 Figure 개별 심층 분석)
   - Chapter 7: 주요 연구 결과 (통계치 완전 인용)
   - Chapter 8: 고찰 및 임상적 한계 (병태생리, 임상 의의, 연구 제한점)
   - Chapter 9: 핵심 전문 용어 사전 (핵심 용어 5~8개 정밀 정의)
   - Chapter 10: 셀프 점검 퀴즈 및 정답 해설 (객관식 3문항, 주관식 서술형 1문항)

### Step 4: Indexing and Remote Synchronization
1. Update `README.md` to append the new guide entry to Section 4 (Study Guides Index).
2. Validate JSON-LD and comment balance via Python.
3. Stage modified files (`git add study_guides/<file> README.md`).
4. Commit with academic message (NO EMOJIS):
   `git commit -m "Add Study Guide #<number>: <Title> (<FirstAuthor> et al., <Year>)"`
5. Push to remote: `git push origin main`.
