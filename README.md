# Parkinson Study: 파킨슨병 및 이상운동질환 논문 연속 학습 프로젝트

본 저장소는 파킨슨병(Parkinson's Disease) 및 파킨슨 증후군, 이상운동질환(Movement Disorders) 관련 학술 논문 아카이브를 바탕으로, 매일 1편씩 무작위로 논문을 선정하여 체계적인 학술 분석 학습서(Study Guide)를 구축·축적하는 저장소입니다.

---

## 1. 프로젝트 개요

* **목적**: 대규모 의학/신경과학 논문 아카이브로부터 무작위 샘플링을 수행하고, 표준화된 10대 학술 분석 체계에 입각한 정밀 학습서를 지속적으로 생성 및 보관함.
* **대상 저널**: *Movement Disorders* 및 유관 신경과학/신경과 학술지 논문군.
* **학습서 작성 원칙**:
  * 이모지 사용 전면 금지 (마크다운 표준 서식만을 활용한 학술 보고서 양식).
  * 엄밀하지 못한 표현 및 주관적 서술 배제 (표준 해부학적·통계학적 용어 및 정량 데이터 사용).
  * 근거 없는 주장 금지 (원문 텍스트, 통계 수치, 표, 그림에 명시된 사실에만 입각).
  * 논문 수록 시각 자료(Table 및 Figure) 전수 소개 및 관전 포인트 분석 의무화.

---

## 2. 디렉토리 구조

`
parkinson_study/
├── AGENTS.md                  # 저장소 공식 운영 및 작성 규칙 (에이전트 행동 지침)
├── README.md                  # 프로젝트 소개 문서
├── study_picker.py            # 무작위 논문 추첨 및 자동 다운로드 모듈
├── data/
│   └── papers_index.json      # 논문 메타데이터 인덱스 (로컬 전용, .gitignore 격리)
├── docs/
│   └── RULES.md               # 문서 및 학습서 작성 상세 규칙
├── downloaded_pdfs/           # 다운로드된 논문 원문 PDF 파일 저장소
└── study_guides/              # 생성된 회차별 논문 스터디 가이드 마크다운 문서
    └── 0001_MovDisord_2001_BSPDC_Manyam.md
`

---

## 3. 학습서 표준 구성 체계 (10 Chapters)

1. **논문 기본 정보 (Paper Metadata)**: 제목, 저자, 소속, 학술지, 권·호, 연도, DOI, PMID.
2. **핵심 요약 (Executive Summary)**: 4~5개 항목의 정량적 핵심 결과 요약.
3. **초록 (Abstract)**: 영문 원문 전문 및 한국어 정밀 완역문.
4. **연구 배경 및 연구 질문 (Research Questions)**: 연구 배경, Primary RQ, Secondary RQs.
5. **연구 대상 및 방법론 (Methods)**: 코호트 설계, 포함/배제 기준, 계측 기기 및 프로토콜, 통계 분석 기법.
6. **본문 수록 시각 자료 전수 분석 (Detailed Analysis of All Tables & Figures)**: Table 및 Figure 전체를 개별 심층 분석 (원문 표 참조 안내 + 집중 관전 포인트 제시).
7. **주요 연구 결과 (Key Findings)**: 인구통계, 증상별 빈도, 영상 계측치 등 데이터 중심 요약.
8. **고찰 및 임상적 한계 (Discussion & Limitations)**: 병태생리 가설, 기존 연구와의 비교, 치료적 한계, 연구 제한점.
9. **핵심 전문 용어 사전 (Terminology Glossary)**: 논문의 핵심 의학/연구 용어 정밀 정의.
10. **셀프 점검 퀴즈 및 정답 해설 (Self-Assessment Quiz)**: 객관식 문항 및 상세 해설.

---

## 4. 실행 및 활용 방법

### 무작위 논문 추첨 및 원문 다운로드
`ash
python study_picker.py
`
study_picker.py 모듈을 실행하면 data/papers_index.json에 등록된 논문 데이터베이스에서 무작위로 1편을 선정하고 원문 PDF를 downloaded_pdfs/ 디렉토리에 자동으로 다운로드합니다.
