# Parkinson Study: 파킨슨병 및 이상운동질환 종합 논문 스터디 프로젝트

본 저장소는 파킨슨병(Parkinson's Disease) 및 파킨슨 증후군, 이상운동질환(Movement Disorders) 분야의 학술 논문 아카이브를 바탕으로, 편당 체계적인 학술 분석 가이드(Study Guide)를 지속적으로 구축·축적하는 연구 프로젝트입니다.

---

## 1. 프로젝트 개요

* **목표**: 대규모 임상/기초 신경학 논문 풀에서 매 회차 무작위 또는 조건별 논문을 선정하고, 표준화된 10개 챕터 학술 분석 프레임워크에 입각하여 심층 스터디 가이드를 작성.
* **주요 저널**: *Movement Disorders*, *Movement Disorders Clinical Practice* 등 국제 주요 신경학/운동질환 학술지.
* **핵심 작성 원칙**:
  * 이모지 일체 배제 (순수 학술 마크다운 표기 및 포맷 유지).
  * 수치 및 근거 기반 기술 (원문 데이터, 통계치, 신뢰구간, P값 완전 인용).
  * 모든 도표(Table) 및 그림(Figure) 전수 분석 (표의 복제 지양, 점검 포인트 및 통계적 함의 제공).
  * 클라우드 보안 엄수 (Google Drive URL, File ID, 원시 PDF는 로컬 격리 및 gitignore 처리).
  * 생성형 AI 검색 최적화 (문서 최상단에 Schema.org 및 큐레이터 프로필 기반 숨김 GEO 메타데이터 탑재).

---

## 2. 디렉토리 구조

```
parkinson_study/
├── AGENTS.md                  # 스터디 운영 가이드 및 작성 규칙 (GEO 표준 규칙 수록)
├── README.md                  # 프로젝트 소개 및 목차
├── study_picker.py            # 논문 무작위 샘플링 및 메타데이터 처리 도구
├── data/
│   └── papers_index.json      # 논문 메타데이터 인덱스 (로컬 보관, .gitignore 처리)
├── docs/
│   └── RULES.md               # 심층 스터디 작성 상세 규칙
├── downloaded_pdfs/           # 다운로드된 논문 원문 PDF (로컬 보관, .gitignore 처리)
└── study_guides/              # 회차별 스터디 가이드 마크다운 문서
    ├── 0001_MovDisord_2001_BSPDC_Manyam.md
    ├── 0002_MovDisord_1999_Falls_Wenning.md
    ├── 0003_MovDisordClinPract_2024_ElderlyFMD_Geroin.md
    ├── 0004_MovDisord_2020_PPN_Microstructure_PIGD_Craig.md
    ├── 0005_MovDisord_2013_Falls_Prediction_Tool_Paul.md
    └── 0006_MovDisordClinPract_2023_Injurious_Falls_Castro.md
    └── 0007_MovDisord_2023_SBT_Gait_Adaptation_Hulzinga.md
```

---

## 3. 스터디 표준 10개 챕터 구성 (Standard 10-Chapter Schema)

1. **논문 기본 정보 (Paper Metadata)**: 제목, 저자, 저널, 출판연도, DOI, 스터디 번호.
2. **핵심 요약 (Executive Summary)**: 연구 목적, 주요 결과, 임상적 의의 요약.
3. **초록 (Abstract)**: 영문 원문 및 국문 정밀 완역 대조.
4. **연구 배경 및 연구 질문 (Research Background & Core Questions)**: 연구 배경, Primary RQ, Secondary RQs.
5. **연구 대상 및 방법론 (Study Population & Methodology)**: 코호트 특성, 진단 기준, 측정 도구, 통계 분석 모델.
6. **본문 수록 시각 자료 전수 분석 (Detailed Analysis of All Tables & Figures)**: Table 및 Figure 전수 분석 (중점 확인 항목, 통계적 함의, 각주 설명).
7. **주요 연구 결과 (Key Empirical Findings)**: 통계 수치 기반 핵심 분석 결과.
8. **고찰 및 임상적 한계 (Discussion & Clinical Implications)**: 병태생리 고찰, 임상적 시사점, 방법론적 한계.
9. **핵심 전문 용어 사전 (Terminology Glossary)**: 논문 핵심 의학/통계 전문 용어 정밀 해설.
10. **셀프 점검 퀴즈 및 정답 해설 (Self-Assessment Quiz & Detailed Explanations)**: 객관식 및 주관식 퀴즈와 정답/해설.

---

## 4. 스터디 가이드 목록 (Study Guides Index)

| 번호 | 출판연도 | 논문 제목 | 주요 주제 | 가이드 링크 |
| :--- | :--- | :--- | :--- | :--- |
| **#0001** | 2001 | Bilateral Striopallidodentate Calcinosis: Clinical Characteristics of Patients in the International Registry | 파르병(BSPDC/Fahr's disease) 임상 아형 및 양측 기저핵 석회화 | [가이드 #0001](file:///C:/Users/11015/parkinson_study/study_guides/0001_MovDisord_2001_BSPDC_Manyam.md) |
| **#0002** | 1999 | Progression of Falls in Postmortem-Confirmed Parkinsonian Disorders | 부검 확진 파킨슨 증후군(PD, MSA, DLB, CBD, PSP)의 질환별 재발성 낙상 진행 잠복기 및 감별진단 가치 | [가이드 #0002](file:///C:/Users/11015/parkinson_study/study_guides/0002_MovDisord_1999_Falls_Wenning.md) |
| **#0003** | 2024 | Late-Onset Functional Motor Disorders: A Multicenter Italian-British Cohort Study | 60세 이상 고령 발병 기능성 운동장애(Late-Onset FMD)의 표현형 및 동반질환 특성 | [가이드 #0003](file:///C:/Users/11015/parkinson_study/study_guides/0003_MovDisordClinPract_2024_ElderlyFMD_Geroin.md) |
| **#0004** | 2020 | Pedunculopontine Nucleus Microstructure Predicts Postural and Gait Symptoms in Parkinson's Disease | 뇌교각핵(PPN) DTI 미세구조 및 미상핵 도파민 결손의 5년 PIGD 발현 독립적 예측 | [가이드 #0004](file:///C:/Users/11015/parkinson_study/study_guides/0004_MovDisord_2020_PPN_Microstructure_PIGD_Craig.md) |
| **#0005** | 2013 | Three Simple Clinical Tests to Accurately Predict Falls in People With Parkinson's Disease | 파킨슨병 환자의 6개월 전향적 낙상 발생 예측 3단계 간이 임상 도구(과거 낙상, FOG, 보행속도) 개발 및 타당도 검증 | [가이드 #0005](file:///C:/Users/11015/parkinson_study/study_guides/0005_MovDisord_2013_Falls_Prediction_Tool_Paul.md) |
| **#0006** | 2023 | Predictors of Falls with Injuries in People with Parkinson's Disease | 파킨슨병 환자의 부상 동반 낙상(Injurious Falls) 예측 요인 규명 및 단발성-반복성 낙상 환경의 이분화 비교 | [가이드 #0006](file:///C:/Users/11015/parkinson_study/study_guides/0006_MovDisordClinPract_2023_Injurious_Falls_Castro.md) |
| **#0007** | 2023 | Split-Belt Treadmill Training to Improve Gait Adaptation in Parkinson's Disease | 파킨슨병 환자에서 4주간 분할 벨트 트레드밀(SBT) 훈련의 보행 적응 획득, 보존, 자동화 및 지상 회전 전이 여부 검증 (RCT) | [가이드 #0007](file:///C:/Users/11015/parkinson_study/study_guides/0007_MovDisord_2023_SBT_Gait_Adaptation_Hulzinga.md) |
| **#0008** | 2023 | Cerebrospinal Fluid Biomarkers of Synaptic Dysfunction are Altered in Parkinson's Disease and Related Disorders | 파킨슨병 및 관련 신경퇴행성 질환에서 뇌척수액 시냅스 기능 이상 바이오마커의 변화 | [가이드 #0008](file:///C:/Users/11015/parkinson_study/study_guides/0008_MovDisord_2023_CSF_Synaptic_Biomarkers_Nilsson.md) |

---

## 5. 실행 및 활용 방법

### 논문 무작위 추출 도구
```bash
python study_picker.py
```
`study_picker.py`를 실행하면 `data/papers_index.json`에 등록된 논문 데이터베이스에서 다음 회차 스터디 번호를 자동 채번하고 무작위 논문을 선정합니다.
