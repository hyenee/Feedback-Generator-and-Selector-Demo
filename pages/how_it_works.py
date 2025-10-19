import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_card import card

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="How It Works", page_icon="⚙️", layout="wide", initial_sidebar_state="collapsed" )

# st.markdown("""
#     <style>
#     html, body, [class*="st-"], [class*="css-"] {
#         font-size: 1.1rem; /* 기본 폰트 크기보다 10% 크게 (이 값을 조절하세요) */
#     }
#     </style>
#     """, unsafe_allow_html=True)
st.session_state.active_page = "home"

with st.sidebar:
    st.page_link("home.py", label="Home", icon="🏠")
    st.page_link("pages/how_it_works.py", label="How It Works", icon="⚙️")
    st.page_link("pages/tutoring_demo.py", label="Tutoring Demo", icon="👩‍🏫")
    st.markdown("---")

selected = option_menu(
    menu_title=None,
    options=["Home", "How It Works", "Tutoring Demo"],
    icons=["house", "gear", "chat-dots"],
    menu_icon="cast",
    default_index=1,
    orientation="horizontal",
)


if selected == "Home":
    st.switch_page("home.py")
if selected == "Tutoring Demo":
    st.switch_page("pages/tutoring_demo.py")


# --- 카드 스타일을 위한 CSS ---
st.markdown("""
<style>
    .card {
        border: 1px solid #e1e1e1; /* 테두리 */
        border-radius: 10px;       /* 둥근 모서리 */
        padding: 20px;             /* 내부 여백 */
        background-color: #f9f9f9;/* 배경색 */
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1); /* 그림자 효과 */
        transition: 0.3s;
        height: 420px;             /* 카드의 높이를 420px로 고정 (조절 가능) */
        overflow-y: auto;          /* 내용이 높이를 넘어가면 세로 스크롤바 자동 생성 */
        margin-bottom: 20px;       /* 카드 아래 여백 */
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    .card h4 {
        margin-top: 0;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# --- 연구 개요 섹션 ---
st.header("How It Works")
st.write("""
The framework proposed in this study consists of **3 steps**.
""")
col1, col2, col3 = st.columns([0.5, 2, 0.5])

with col1:
    st.write("")

with col2:
    st.image("./image/architecture.png")

with col3:
    st.write("")

st.markdown("###")



# --- 3단 레이아웃 생성 (3 Steps) ---
st.info("👇 Click on each step below to view the corresponding results.")

# col1, col2, col3 = st.columns(3)

# # --- 첫 번째 카드 (Step 1) ---
# with col1:
#     st.markdown("""
#     <div class="card">
#         <h4>Step 1. Teacher Feedback Generation</h4>
#         <p>LLM을 활용하여 교육학 기준에 맞는 피드백을 대량으로 자동 생성합니다. </p>
#         <p>5가지 교육학적 기준을 명시한 <b>w/ criteria</b> 피드백과 일반 <b>w/o criteria</b> 피드백을 생성합니다. </p>
#         <p>✅ <b>Benefit:</b> 교사가 수동으로 피드백을 작성하는 시간을 획기적으로 단축합니다. </p>
#     </div>
#     """, unsafe_allow_html=True)

# # --- 두 번째 카드 (Step 2) ---
# with col2:
#     st.markdown("""
#     <div class="card">
#         <h4>Step 2. Automatic Annotated Teacher Feedback Construction</h4>
#         <p><b>인간의 개입 없이</b> 선호도 데이터셋을 자동으로 구축합니다.</p>
#         <p>w/ criteria 피드백이 더 우수하다는 가설을 통해 <b>선호도 쌍</b>을 자동으로 생성하여 <b>DIRECT-Generated (DG)</b> 데이터셋을 구축합니다.</li>
#         <p>DIRECT-Generated와 소량의 DIRECT-Manual을 합한 DIRECT-Augmented를 구축합니다.</p>
#         <p>✅ <b>Benefit:</b> 데이터 라벨링에 드는 비용과 시간을 '0'으로 만듭니다. </p>
#     </div>
#     """, unsafe_allow_html=True)

# --- 세 번째 카드 (Step 3) ---
# with col3:
#     st.markdown("""
#     <div class="card">
#         <h4>Step 3. Teacher Feedback Selection</h4>
#         <p>자동으로 구축된 대규모 데이터셋으로 <b>랭킹 모델</b>을 훈련합니다. </p>
#         <p>훈련된 모델은 여러 피드백 후보 중, 교육학적으로 최적의 피드백을 선별하여 제공합니다. </p>
#         <p>✅ <b>Benefit:</b> 모든 학생에게 일관된 고품질의 피드백을 제공할 수 있습니다. </p>
#     </div>
#     """, unsafe_allow_html=True)


# --- 3단 레이아웃 생성 ---
col1, col2, col3 = st.columns(3)

# --- 카드 스타일 정의 (기존과 동일) ---
card_styles = {
    "card": {
        "width": "100%", "height": "250px", "background-color": "#f9f9f9",
        "border": "1px solid #e1e1e1", "border-radius": "10px",
        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.1)", "transition": "0.3s",
        "overflow-y": "auto", "padding": "15px 20px", "margin": "0"
    },
    "title": { "font-size": "1.4rem", "color": "#333", "margin-bottom": "10px" },
    "text": { "font-size": "1rem", "color": "#333" },
    "filter": { "background-color": "#f9f9f9", "box-shadow": "0 8px 16px 0 rgba(0,0,0,0.2)" }
}

# --- 첫 번째 카드 (Step 1) ---
with col1:
    def go_to_performance():
        st.switch_page("pages/generation_example.py")

    card(
        title="Step 1. Teacher Feedback Generation",
        text=[
           ],
        styles=card_styles,
        on_click=go_to_performance
    )

# --- 두 번째 카드 (Step 2) ---
with col2:
    def go_to_performance():
        st.switch_page("pages/generation_example.py")

    card(
        title="Step 2. Automatic Annotated Teacher Feedback Construction",
        text=[
            ],
        styles=card_styles,
        on_click=go_to_performance
    )

# --- 세 번째 카드 (Step 3) ---
with col3:
    def go_to_performance():
        st.switch_page("pages/performance_analysis.py")

    card(
        title="Step 3. Teacher Feedback Selection",
        text=[
            ],
        styles=card_styles,
        on_click=go_to_performance
    )
