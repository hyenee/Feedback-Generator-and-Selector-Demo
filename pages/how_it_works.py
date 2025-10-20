import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_card import card

st.set_page_config(page_title="How It Works", page_icon="⚙️", layout="wide", initial_sidebar_state="collapsed" )
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
        border: 1px solid #e1e1e1; 
        border-radius: 10px;
        padding: 20px;     
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1); 
        transition: 0.3s;
        height: 420px;        
        overflow-y: auto; 
        margin-bottom: 20px;
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



# --- 3 Steps 카드 섹션  ---
st.info("👇 Click on each step below to view the corresponding results.")
col1, col2, col3 = st.columns(3)
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
