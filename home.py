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
    .profile-container {
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    
    .profile-icon-button {
        margin-left: 8px; 
    }

    .profile-icon-button .stButton>button {
        border: none;
        background-color: transparent;
        padding: 0;
        width: 24px;  
        height: 24px;
        color: transparent; 

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

left_col, right_col = st.columns([.9, .1])

with left_col:
    st.write("Ph.D. Dissertation")

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
with st.container(border=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🤖 Step 1:")
        st.markdown("#### Teacher Feedback Generation")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        Automatically generates a large volume of feedback based on **pedagogical criteria** using LLMs.
        """)
        st.success("✅ **Benefit:** Drastically reduces feedback generation time.")

    with col2:
        st.markdown("#### 🏷️ Step 2:")
        st.markdown("#### Automatic Annotated Teacher Feedback Construction")
        st.markdown("")
        st.markdown("""
        Automatically builds preference datasets for training ranking models **without human annotation**.
        """)
        st.info("✅ **Benefit:** Minimizes data labeling costs.")

    with col3:
        st.markdown("#### 🎯 Step 3:")
        st.markdown("#### Teacher Feedback Selection")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        Trains a **ranking model** on the DIRECT-Generated to select the most effective feedback from multiple candidates.
        """)
        st.warning("✅ **Benefit:** Ensures consistent, high-quality feedback.")


st.markdown("##")
st.header("Publications")
papers = [
    {
        "title": "FEAT: A Preference Feedback Dataset through a Cost-Effective Auto-Generation and Labeling Framework for English AI Tutoring",
        "authors": "**Hyein Seo**, Taewook Hwang, Yohan Lee, Sangkeun Jung",
        "venue": "ACL 2025",
        "url": "https://aclanthology.org/2025.acl-short.45",
        "preview": "./image/preview/preview_ACL.png"
    },
    {
        "title": "Large Language Models as Evaluators in Education: Verification of Feedback Consistency and Accuracy",
        "authors": "**Hyein Seo**, Taewook Hwang, Jeesu Jung, Hyeonseok Kang, Hyuk Namgong, Yohan Lee, Sangkeun Jung",
        "venue": "Applied Sciences (SCIE, IF: 2.5)",
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
    {
        "title": "Interactive User Interface for Dialogue Summarization",
        "authors": "Jeesu Jung, **Hyein Seo** (Co-1st Author),  Sangkeun Jung, Riwoo Chung, Hwijung Ryu, Du-Seong Chang",
        "venue": "IUI 2023",
        "url": "https://doi.org/10.1145/3581641.3584057",
        "preview": None 
    },
    {
        "title": "Controllable Text Generation using Semantic Control Grammar",
        "authors": "**Hyein Seo**, Sangkeun Jung, Jeesu Jung, Taewook Hwang, Hyuk Namgung, Yoon-Hyung Roh",
        "venue": "IEEE Access (SCIE, IF: 3.6)",
        "url": "https://doi.org/10.1109/ACCESS.2023.3252017",
        "preview": None 
    },
     {
        "title": "Syntax Vector Learning Using Correspondence for Natural Language Understanding",
        "authors": "**Hyein Seo**, Sangkeun Jung, Taewook Hwang, Hyunji Kim, and Yoon-Hyung Roh",
        "venue": "IEEE Access (SCIE, IF: 3.6)",
        "url": "https://doi.org/10.1109/ACCESS.2021.3087271",
        "preview": None 
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

num_papers_to_show_initially = 3
initial_papers = papers[:num_papers_to_show_initially]
remaining_papers = papers[num_papers_to_show_initially:]

for paper in initial_papers:
    with st.container(border=True):
        if paper.get("preview"):
            col_img, col_text = st.columns([1, 4])
            with col_img:
                st.image(paper["preview"])
            render_paper_details(paper, col_text)
        else:
            render_paper_details(paper, st)

if remaining_papers:
    with st.expander(f"Show {len(remaining_papers)} More Publications..."):
        for paper in remaining_papers:
            with st.container(border=True):
                if paper.get("preview"):
                    col_img, col_text = st.columns([1, 4])
                    with col_img:
                        st.image(paper["preview"])
                    render_paper_details(paper, col_text)
                else:
                    render_paper_details(paper, st)