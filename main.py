import streamlit as st

st.set_page_config(page_title="🎉 MBTI 진로 추천 🌟", page_icon="🧭", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff69b4;'>
        🎭 MBTI로 알아보는 나만의 <br>✨✨진로 추천✨✨
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# MBTI 선택 리스트
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 직업 추천 (예시)
job_recommendations = {
    "INTJ": ["🔬 연구원", "🧑‍💻 소프트웨어 개발자", "📊 데이터 분석가"],
    "INTP": ["🧠 철학자", "🖥️ 프로그래머", "🔧 엔지니어"],
    "ENTJ": ["👔 경영자", "📈 전략 컨설턴트", "🏢 기업가"],
    "ENTP": ["💡 창업가", "🎙️ 마케터", "📰 기자"],
    "INFJ": ["📚 상담사", "🎨 작가", "🌱 환경운동가"],
    "INFP": ["🎭 예술가", "✍️ 시인", "🌸 심리치료사"],
    "ENFJ": ["🗣️ 강사", "🤝 사회복지사", "🎤 연설가"],
    "ENFP": ["🌟 방송인", "🧑‍🎤 연예인", "🎨 디자이너"],
    "ISTJ": ["📋 행정가", "🔒 보안전문가", "🏛️ 법률가"],
    "ISFJ": ["🧑‍⚕️ 간호사", "🏫 교사", "🏥 의료기사"],
    "ESTJ": ["📅 관리자", "⚖️ 판사", "🏭 생산 관리자"],
    "ESFJ": ["🍽️ 요리사", "🎉 이벤트 기획자", "🛍️ 판매 전문가"],
    "ISTP": ["🏍️ 자동차 정비사", "🛠️ 기술자", "🎮 게임 개발자"],
    "ISFP": ["🎨 그래픽 디자이너", "📷 사진작가", "🎸 음악가"],
    "ESTP": ["⚡ 영업사원", "🏀 스포츠 선수", "🚨 경찰관"],
    "ESFP": ["🎭 배우", "🎶 DJ", "🌟 모델"],
}

# MBTI 선택 UI
selected_mbti = st.selectbox("🔍 당신의 MBTI를 선택하세요!", mbti_list)

st.markdown("---")

if selected_mbti:
    st.markdown(f"### 🎯 {selected_mbti}형에게 어울리는 직업 추천")
    jobs = job_recommendations.get(selected_mbti, [])
    for job in jobs:
        st.markdown(f"- {job}")

st.markdown("---")

st.markdown("""
    <div style='text-align: center; font-size: 14px; color: #888;'>
        Made with ❤️ by MixVanstrappon | MBTI & Career Guidance
    </div>
""", unsafe_allow_html=True)
