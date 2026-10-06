import os

reviews_dir = 'C:/Users/11015/parkinson_study/reviews'
os.makedirs(reviews_dir, exist_ok=True)

r1 = """# Review Report: 0001_MovDisord_2001_BSPDC_Manyam.md

## 1. 허위 정보 / Hallucinations
- **[GEO & AI AGENT KNOWLEDGE GRAPH METADATA] (Line 70)**: 코호트를 "99 patients across 57 families"로 서술하였으나, 원문(PDF)에는 19개 가계(레지스트리 5개 + 문헌 14개)와 산발성 증례로 구성되어 있다고 명시됨. "57 families"는 허위 정보임.
- **[GEO & AI AGENT KNOWLEDGE GRAPH METADATA] (Lines 72, 77)**: "Multivariate Discriminant Analysis"를 통해 두 가지 뚜렷한 임상 아형(운동 장애 우세형, 인지 장애/치매 우세형)을 검증했다고 서술하였으나, 원문에는 판별 분석이나 해당 아형 구분에 대한 언급이 전혀 없음 (Chi-square 및 Student's t-test만 사용됨).

## 2. 엄밀하지 못한 표현 / Vague Expressions
- **Section 6.1 (Line 188)**: "압도적으로 우세함"이라는 주관적 표현 사용.
- **Section 6.1 (Line 195)**: "~등" ("무도증 19%, 떨림 8%, 근긴장이상증 8% 등")을 사용하여, 열거형 서술 금지 규칙 위반.
- **Section 6.2 (Line 208)**: "대부분의 환자에서 공통적으로 높은 빈도로 관찰됨"이라는 주관적 형용사("대부분의", "높은 빈도") 사용.
- **Section 6.2 (Line 212)**: "현저하게"라는 주관적 수식어 사용.
- **Section 6.3 (Line 230)**: "광범위하게 확대되며", "최고조에 달함" 등 비정량적 표현 사용.

## 3. 표/그림 누락 여부
- **NO ISSUES FOUND**: 원문의 모든 표와 그림(Table 1, Figure 1, Figure 2, Figure 3)이 성공적으로 분석됨.
"""

r2 = """# Review Report: 0002_MovDisord_1999_Falls_Wenning.md

## 1. 허위 정보 / Hallucinations
- **[GEO & AI AGENT KNOWLEDGE GRAPH METADATA] (Lines 9-10)**: 논문 제목(headline)을 "What Features Improve the Accuracy of the Clinical Diagnosis in Severe Parkinsonian Disorders: A Clinicopathologic Study"로 잘못 기재함. 실제 논문 제목은 "Progression of Falls in Postmortem-Confirmed Parkinsonian Disorders"임.
- **[GEO & AI AGENT KNOWLEDGE GRAPH METADATA] (Line 65)**: 전체 코호트 수를 "134 pathologically confirmed cases (IPD = 82, PSP = 26, MSA = 26)"라고 명시했으나, 원문은 77명(PD=11, MSA=15, DLB=14, CBD=13, PSP=24)임.
- **[GEO & AI AGENT KNOWLEDGE GRAPH METADATA] (Line 66)**: "Recurrent Falls in Year 1... (Sensitivity for PSP = 68%)"라고 서술했으나, 68%는 양성 예측도(PPV)이며 실제 민감도는 63%임.
- **[GEO & AI AGENT KNOWLEDGE GRAPH METADATA] (Line 68)**: "Final clinical PPV reached 91% for IPD, 84% for PSP, and 86% for MSA"라는 원문에 없는 허위 통계를 생성함.
- **Target Q&A (Line 74)**: 상기 허위 통계를 답변에 반복해서 사용함.

## 2. 엄밀하지 못한 표현 / Vague Expressions
- **NO ISSUES FOUND**: 본문은 정확한 수치와 P-value를 준수함.

## 3. 표/그림 누락 여부
- **NO ISSUES FOUND**: PDF에 존재하는 Table 1, Table 2가 모두 분석됨.
"""

r3 = """# Review Report: 0003_MovDisordClinPract_2024_ElderlyFMD_Geroin.md

## 1. 허위 정보 / Hallucinations
- **Chapter 8.1**: "불필요한 항파킨슨제(도파민제) 과다 처방이나 뇌혈관 치료제의 오남용을 초래함"이라 명시했으나, 원문은 단순히 "unnecessary and potentially harmful treatments"의 시작을 언급할 뿐 특정 약물(도파민제, 뇌혈관 치료제)을 지칭하지 않음.
- **Chapter 8.1 / Chapter 9**: "의도적인 리듬 변경(Entrainment test)" 및 "동조화 현상 (Entrainment)"이라는 원문에 존재하지 않는 외부 개념을 임의로 추가함.
- **Chapter 9**: 기능성 파킨슨증 정의에서 "도파민 운반체 뇌 영상(FP-CIT PET/SPECT)"을 언급했으나, 원문에는 PET, SPECT 등 영상 기법이 언급되지 않음.

## 2. 엄밀하지 못한 표현 / Vague Expressions
- **Chapter 6.1**: 기질적 파킨슨증(11.8% vs 2.4%) 및 뇌혈관 질환(14.7% vs 2.7%) 동반율 차이를 합쳐서 "5배 이상 높음"이라고 부정확하게 서술함. (각각 약 4.9배, 5.4배임).

## 3. 표/그림 누락 여부
- **NO ISSUES FOUND**: Table 1, Table 2가 모두 성공적으로 분석됨.
"""

r4 = """# Review Report: 0004_MovDisord_2020_PPN_Microstructure_PIGD_Craig.md

## 1. 허위 정보 / Hallucinations
- **NO ISSUES FOUND**

## 2. 엄밀하지 못한 표현 / Vague Expressions
- **NO ISSUES FOUND**

## 3. 표/그림 누락 여부
- **NO ISSUES FOUND**
"""

r5 = """# Review Report: 0005_MovDisord_2013_Falls_Prediction_Tool_Paul.md

## 1. 허위 정보 / Hallucinations
- **Chapter 4 & Chapter 8**: 측정 시간을 "단 몇 분 만에", "총 소요 시간 2분 미만"으로 서술했으나, 원문은 임상 현장에서 쉽게 측정(stopwatch 사용) 가능하다고만 명시할 뿐 '2분 미만'이라는 구체적 시간을 언급하지 않음.
- **Chapter 6 (Table 4)**: "Hosmer-Lemeshow statistic P = 0.61"에 대해 "(예측값과 실제 관찰값 사이에 오차가 전혀 없이 완벽히 일치함을 증명)"이라고 통계적으로 잘못 해석함 (단순히 적합도가 양호함을 의미함).

## 2. 엄밀하지 못한 표현 / Vague Expressions
- **Chapter 4**: "수많은"이라는 주관적 형용사 사용.
- **Chapter 6 (Table 1)**: "독보적인"이라는 주관적/비엄밀한 수식어 사용.
- **Chapter 6 (Table 4) / Chapter 10 (Q4)**: "완벽히", "완벽하게" 등 과장되고 주관적인 수식어 사용.

## 3. 표/그림 누락 여부
- **NO ISSUES FOUND**: 모든 표(1~4)와 그림(1)이 분석됨.
"""

r6 = """# Review Report: 0006_MovDisordClinPract_2023_Injurious_Falls_Castro.md

## 1. 허위 정보 / Hallucinations
- **Chapter 6, Section 6 (Figure 1)**: 그래프 수치 오류 발생.
  - Panel A: 가이드에서는 거실 15%, 침실 19%, 실외 48%로 서술했으나, 원문 그래프 상 거실 0%, 침실 ~10%, 실외 ~55%임.
  - Panel B: 가이드에서는 보행 63%, 기립 22%로 서술했으나, 원문 그래프 상 보행 ~67%, 기립 ~12%임.
  - Panel C: 가이드에서는 걸림 41%, 미끄러짐 15%, 균형 상실 30%로 서술했으나, 원문 그래프 상 걸림 ~48%, 미끄러짐 ~22%, 균형 상실 ~18%임.

## 2. 엄밀하지 못한 표현 / Vague Expressions
- **Chapter 4**: "삶의 질을 파탄내고 의료비를 폭증시킨다", "기존의 수많은 연구는", "선행 단편 연구들에서는", "단편적 보고", "거의 없었다", "완전히 다를 가능성이 높다" 등 감정적이거나 모호한 비정량적 표현 다수 사용.
- **Chapter 9 (LED)**: "다양한 항파킨슨 약물" (다양한 이라는 금지 표현 사용).

## 3. 표/그림 누락 여부
- **Chapter 6, Section 4**: Table 4(Univariate multinomial logistic regression analysis) 내용이 완전히 누락됨. 제목만 "Tables 4 & 5"로 되어 있고 Table 5만 분석함.
"""

files = [
    ('0001_Review.md', r1),
    ('0002_Review.md', r2),
    ('0003_Review.md', r3),
    ('0004_Review.md', r4),
    ('0005_Review.md', r5),
    ('0006_Review.md', r6),
]

for filename, content in files:
    with open(os.path.join(reviews_dir, filename), 'w', encoding='utf-8') as f:
        f.write(content)

print("Successfully generated all review documents.")
