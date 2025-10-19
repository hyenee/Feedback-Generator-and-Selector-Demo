import streamlit as st
from streamlit_option_menu import option_menu

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide", initial_sidebar_state="collapsed" )

# --- 팝업(Dialog) 함수 정의 ---
@st.dialog("About Me")
def show_profile_dialog():
    col_img, col_text = st.columns([1, 2]) 

    with col_img:
        st.image("./image/my_profile.jpg", width=120) 

    with col_text:
        st.subheader("Hyein Seo")
        st.markdown("""
        **Ph.D. Candidate**\n
        Intelligent Software Lab, Chungnam National University
        """)
    st.markdown("""
    - **Profile:** [hyenee.notion.site](https://hyenee.notion.site/hyein-seo)
    - **Github:** [github.com/hyenee](https://github.com/hyenee)
    - **Scholar:** [Google Scholar Profile](https://scholar.google.co.kr/citations?hl=ko&user=_RnSGKIAAAAJ)
    """)
    
# st.markdown("""
#     <style>
#     html, body, [class*="st-"], [class*="css-"] {
#         font-size: 1.1rem; /* 기본 폰트 크기보다 10% 크게 (이 값을 조절하세요) */
#     }
#     </style>
#     """, unsafe_allow_html=True)

st.markdown("<style> ul[data-testid='stSidebarNav'] {display: none;} </style>", unsafe_allow_html=True)
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
    default_index=0,
    orientation="horizontal",
)

if selected == "How It Works":
    st.switch_page("pages/how_it_works.py")
if selected == "Tutoring Demo":
    st.switch_page("pages/tutoring_demo.py")

# --- 페이지 콘텐츠 ---
st.title("Automatic Teacher Feedback Generation and Selection for English Education Tutoring using Large Language Models")

# --- 오른쪽 정렬 및 아이콘 버튼을 위한 CSS ---
st.markdown("""
<style>
    /* 텍스트와 아이콘 버튼을 담을 컨테이너 */
    .profile-container {
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    
    /* 아이콘 버튼을 감싸는 div에 특정 클래스 부여 */
    .profile-icon-button {
        margin-left: 8px; 
    }

    /* 아이콘 버튼의 기본 스타일 제거 및 SVG 배경 적용 */
    .profile-icon-button .stButton>button {
        border: none;
        background-color: transparent;
        padding: 0;
        width: 24px;  
        height: 24px;
        color: transparent; 

        /* URL-encoded SVG 아이콘을 배경 이미지로 설정 */
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-box-arrow-up-right' viewBox='0 0 16 16'%3E%3Cpath fill-rule='evenodd' d='M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z'/%3E%3Cpath fill-rule='evenodd' d='M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: center;
        background-size: 16px 16px;
    }
    .profile-icon-button .stButton>button:hover {
        background-color: #f0f0f0; 
        border-radius: 50%;
    }
    .profile-icon-button .stButton>button:active {
        background-color: #e0e0e0; 
    }
</style>
""", unsafe_allow_html=True)

_, right_col = st.columns([.9, .1])
with right_col:
    st.markdown('<div class="profile-link-container">', unsafe_allow_html=True)
    if st.button("By Hyein Seo", key="profile_link_button"):
        show_profile_dialog()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 연구 개요 섹션 ---
st.write("""
This research proposes a **framework that automates the entire process, from feedback generation to selection,** for English education tutoring using Large Language Models (LLMs).
""")
_, img_col, _ = st.columns([0.2, 0.6, 0.2])
with img_col:
    st.image("./image/overview.png", use_container_width =True)


st.markdown("##")
# col1, col2 = st.columns([1, 3])
# with col1:
#     st.markdown("<p style='text-align: center; font-size: 80px;'>🤖</p>", unsafe_allow_html=True)
# with col2:
#     st.subheader("Step 1: Teacher Feedback Generation")
#     st.markdown("""
#     LLM을 활용하여 교육학 기준에 맞는 피드백을 대량으로 자동 생성합니다. 
#     5가지 교육학적 기준을 명시한 **`w/ criteria`** 피드백과 일반 **`w/o criteria`** 피드백을 생성합니다.
#     """)
#     st.success("✅ **Benefit:** 교사가 수동으로 피드백을 작성하는 시간을 획기적으로 단축합니다.")


# # --- Step 2 ---
# st.markdown("###") 
# col1, col2 = st.columns([3, 1])
# with col1:
#     st.subheader("Step 2: Automatic Annotated Teacher Feedback Construction")
#     st.markdown("""
#     **인간의 개입 없이** 선호도 데이터셋을 자동으로 구축합니다. 
#     `w/ criteria` 피드백이 더 우수하다는 가설을 통해, `(w/ criteria, w/o criteria)` 형태의 선호도 쌍을 자동으로 생성하여 **`DIRECT-Generated`** 데이터셋을 완성합니다.
#     DIRECT-Generated와 소량의 DIRECT-Manual을 합한 DIRECT-Augmented를 구축합니다.
#     """)
#     st.info("✅ **Benefit:** 데이터 라벨링에 드는 비용과 시간을 '0'으로 만듭니다.")
# with col2:
#     st.markdown("<p style='text-align: center; font-size: 80px;'>🏷️</p>", unsafe_allow_html=True)


# # --- Step 3 ---
# st.markdown("###")
# col1, col2 = st.columns([1, 3])
# with col1:
#     st.markdown("<p style='text-align: center; font-size: 80px;'>🎯</p>", unsafe_allow_html=True)
# with col2:
#     st.subheader("Step 3: Teacher Feedback Selection")
#     st.markdown("""
#     자동으로 구축된 대규모 데이터셋으로 **랭킹 모델**을 훈련합니다. 
#     훈련된 모델은 여러 피드백 후보 중, 교육학적으로 최적의 피드백을 선별하여 제공합니다.
#     """)
#     st.warning("✅ **Benefit:** 모든 학생에게 일관된 고품질의 피드백을 제공할 수 있습니다.")


with st.container(border=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🤖 Step 1: Teacher Feedback Generation")
        st.markdown("""
        Automatically generates a large volume of feedback based on **pedagogical criteria** using an LLM.
        """)
        st.success("✅ **Benefit:** Drastically reduces feedback generation time.")

    with col2:
        st.subheader("🏷️ Step 2: Automatic Annotated Teacher Feedback Construction")
        st.markdown("""
        Automatically builds a preference dataset for training ranking models **without human annotation**.
        """)
        st.info("✅ **Benefit:** Minimizes data labeling costs.")

    with col3:
        st.subheader("🎯 Step 3: Teacher Feedback Selection")
        st.markdown("""
        Trains a **ranking model** on the DIRECT-Generated to select the most effective feedback from multiple candidates.
        """)
        st.warning("✅ **Benefit:** Ensures consistent, high-quality feedback.")


# st.markdown("""
# <style>
#     /* 캐러셀 전체를 감싸는 컨테이너의 높이를 지정 */
#     .carousel-container {
#         height: 20px; /* 슬라이드 높이 */
#         margin-bottom: 2rem;
#     }
    
#     /* 캐러셀 내부의 각 슬라이드 아이템을 카드처럼 스타일링 */
#     .carousel-container .carousel-item-container {
#         border: 1px solid #e1e1e1;
#         border-radius: 10px;
#         background-color: #F0F2F6; /* <-- 배경색을 연한 회색으로 변경 */
#         box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
#         padding: 0 25px;
#         height: 100%; 
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#     }
# </style>
# """, unsafe_allow_html=True)

# carousel_items = [
#     # Step 1
#     dict(
#         title="Step 1. Teacher Feedback Generation",
#         text="LLM을 활용하여 교육학 기준에 맞는 피드백을 대량으로 자동 생성합니다.",
#         img="./image/dummy.png"
#     ),
#     # Step 2
#     dict(
#         title="Step 2. Automatic Annotated Teacher Feedback Construction",
#         text="인간의 개입 없이 선호도 데이터셋을 자동으로 구축합니다.",
#         img="./image/dummy.png"
#     ),
#     # Step 3
#     dict(
#         title="Step 3. Teacher Feedback Selection",
#         text="자동으로 구축된 대규모 데이터셋으로 랭킹 모델을 훈련하고, 교육학적으로 최적의 피드백을 선별하여 제공합니다.",
#         img="./image/dummy.png"
#     )
# ]

# st.markdown('<div class="carousel-container">', unsafe_allow_html=True)
# carousel(items=carousel_items, width=0.7)
# st.markdown('</div>', unsafe_allow_html=True)


st.markdown("##")
st.header("Publications")
papers = [
    {
        "title": "FEAT: A Preference Feedback Dataset through a Cost-Effective Auto-Generation and Labeling Framework for English AI Tutoring",
        "authors": "**Hyein Seo**, Taewook Hwang, Yohan Lee, Sangkeun Jung",
        "venue": "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025 Short)",
        "url": "https://aclanthology.org/2025.acl-short.45",
        "preview": "./image/preview/preview_ACL.png"
    },
    {
        "title": "Large Language Models as Evaluators in Education: Verification of Feedback Consistency and Accuracy",
        "authors": "**Hyein Seo**, Taewook Hwang, Jeesu Jung, Hyeonseok Kang, Hyuk Namgong, Yohan Lee, Sangkeun Jung",
        "venue": "Applied Sciences (MDPI)",
        "url": "https://doi.org/10.3390/app15020671",
        "preview": "./image/preview/preview_MDPI.png"
    },
    {
        "title": "Automatic Teacher Feedback Generation and Selection for English Education Tutoring using Large Language Models",
        "authors": "**Hyein Seo**",
        "venue": "Ph.D. Dissertation",
        "url": "",
        "preview": "./image/preview/preview_PhD.png"
    },
]

def render_paper_details(paper, container):
    if paper.get("url"):
        container.markdown(f"<h4><a href='{paper['url']}' target='_blank'>{paper['title']}</a></h4>", unsafe_allow_html=True)
    else:
        container.markdown(f"<h4>{paper['title']}</h4>", unsafe_allow_html=True)
        container.caption("🔗 Link will be available soon.")
        
    container.markdown(paper["authors"])
    container.caption(f"*{paper['venue']}*")

for paper in papers:
    with st.container(border=True):
        if paper.get("preview"):
            col_img, col_text = st.columns([1, 4])
            with col_img:
                st.image(paper["preview"])
            render_paper_details(paper, col_text)
        else:
            render_paper_details(paper, st)