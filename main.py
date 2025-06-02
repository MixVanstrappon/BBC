import streamlit as st

st.set_page_config(page_title="🎉 MBTI 진로 추천 🌟", page_icon="🧭", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>
        🎭 MBTI로 알아보는 나만의 <br>✨✨진로 추천✨✨
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# MBTI 리스트 (대문자 4자리만 체크)
valid_mbti = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 추천 직업 및 상세 정보 데이터 구조
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
            "연봉": "수입 불규칙, 출판과 강연 활동 병행",
            "전망": "문화예술 분야에서 꾸준한 수요"
        },
        "🌸 심리치료사": {
            "과정": "심리학 전공, 전문 상담사 자격증 취득 필요",
            "연봉": "평균 연봉 약 4,500만원",
            "전망": "정신건강에 대한 관심 증가로 수요 증가"
        }
    },
    # 나머지 MBTI는 간단하게 한 직업씩 예시로 넣었어요.
    "ENTP": {
        "💡 창업가": {
            "과정": "경영학 전공 또는 창업 경험, 네트워킹 중요",
            "연봉": "매우 다양, 성공 시 고수익 가능",
            "전망": "혁신적 아이디어와 도전 정신 중요"
        },
        "🎙️ 마케터": {
            "과정": "마케팅, 광고 관련 전공 또는 실무 경험",
            "연봉": "평균 연봉 약 4,800만원",
            "전망": "디지털 마케팅 확산에 따라 성장 중"
        }
    },
    # 기본값으로 비어있는 것도 넣어두기
}

st.write("👉 **당신의 MBTI를 입력해 주세요!** (예: INFP, ENTJ)")

mbti_input = st.text_input("MBTI 입력 (대문자 4자리):").strip().upper()

if mbti_input:
    if mbti_input not in valid_mbti:
        st.error("❌ 올바른 MBTI를 입력해 주세요! 예) INFP, ENTJ")
    else:
        st.success(f"✅ {mbti_input} 유형에 맞는 추천 직업을 보여드릴게요!")
        jobs_for_mbti = career_data.get(mbti_input, {})
        
        if not jobs_for_mbti:
            st.warning("해당 MBTI에 대한 직업 정보가 아직 준비되지 않았어요. 😢")
        else:
            selected_job = st.selectbox("💼 추천 직업 중 하나를 선택해 주세요!", list(jobs_for_mbti.keys()))
            if selected_job:
                st.markdown(f"### 📝 **{selected_job}** 직업 정보")
                info = jobs_for_mbti[selected_job]
                st.markdown(f"- **과정:** {info['과정']}")
                st.markdown(f"- **연봉:** {info['연봉']}")
                st.markdown(f"- **전망:** {info['전망']}")

st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 14px; color: #888;'>
    Made with ❤️ by YourName | MBTI & Career Guidance
</div>
""", unsafe_allow_html=True)
