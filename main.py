import streamlit as st

st.set_page_config(page_title="🎉 MBTI 진로 추천 🌟", page_icon="🧭", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>
        🎭 MBTI로 알아보는 나만의 <br>✨✨진로 추천✨✨
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# MBTI 리스트
valid_mbti = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

career_data = {
    "INTJ": {
        "🔬 연구원": {
            "과정": "대학에서 자연과학 또는 공학 전공, 대학원 진학 추천",
            "연봉": "평균 연봉 약 5,500만원",
            "전망": "과학기술 발전에 따라 수요 꾸준히 증가"
        },
        "🧑‍💻 소프트웨어 개발자": {
            "과정": "컴퓨터공학 전공 또는 코딩 부트캠프 수료",
            "연봉": "평균 연봉 약 6,000만원",
            "전망": "IT산업 성장에 따라 지속적 고용 증가"
        },
        "📊 데이터 분석가": {
            "과정": "통계학, 데이터 사이언스 관련 전공 및 실무 경험",
            "연봉": "평균 연봉 약 5,800만원",
            "전망": "빅데이터 활용 증가로 전망 밝음"
        }
    },
    "INFP": {
        "🎭 예술가": {
            "과정": "예술 관련 대학 전공 또는 전문 교육기관 수료",
            "연봉": "평균 연봉 매우 다양 (경력에 따라 다름)",
            "전망": "창의력과 개성이 중요, 개인 능력에 따라 다름"
        },
        "✍️ 시인": {
            "과정": "문예창작, 국문학 등 관련 전공",
            "연봉": "수입 불규칙, 출판과 강연 활동 병
