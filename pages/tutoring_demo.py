import streamlit as st
from streamlit_option_menu import option_menu
import base64
import streamlit.components.v1 as components

def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"이미지 파일을 찾을 수 없습니다: {file_path}")
        return None

def get_sorted_candidates(candidates, ranking_list):
    """
    미리 정렬된 랭킹 리스트의 순서에 따라 피드백 후보를 포맷팅합니다.
    """
    candidates_dict = {item[0].lower(): item[1] for item in candidates}
    formatted_candidates = []
    for name in ranking_list:
        feedback_text = candidates_dict.get(name.lower())
        if feedback_text:
            formatted_candidates.append(f"{name}: {feedback_text}")
            
    return formatted_candidates


# --- 페이지 기본 설정 ---
st.set_page_config(page_title="Tutoring Demo", page_icon="👩‍🏫", layout="wide", initial_sidebar_state="collapsed")

# st.markdown("""
#     <style>
#     html, body, [class*="st-"], [class*="css-"] {
#         font-size: 1.1rem; /* 기본 폰트 크기보다 10% 크게 (이 값을 조절하세요) */
#     }
#     </style>
#     """, unsafe_allow_html=True)

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
    default_index=2,
    orientation="horizontal",
)

if selected == "Home":
    st.switch_page("home.py")
if selected == "How It Works":
    st.switch_page("pages/how_it_works.py")
if selected == "Performance Analysis":
    st.switch_page("pages/performance_analysis.py")

# --- 채팅 UI를 위한 CSS ---
st.markdown("""
<style>
    ul[data-testid='stSidebarNav'] {display: none;}
    .message-row { display: flex; align-items: flex-end; margin-bottom: 15px; }
    .message-row.teacher { justify-content: flex-start; }
    .message-row.student { justify-content: flex-end; }
    .profile-pic { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }
    .teacher-bubble { 
        background-color: #E7F5FF; border: 1px solid #BCE0FD;
        color: #333; border-radius: 10px; padding: 10px 15px; 
        margin-left: 10px; max-width: 80%; font-size: 0.95rem;
    }
    .student-bubble { 
        background-color: #F0F0F0; border: 1px solid #E0E0E0;
        color: #333; border-radius: 10px; padding: 10px 15px; 
        margin-right: 10px; max-width: 80%; font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)


# --- 데이터 및 프로필 이미지 ---
TUTORING_DATA = {
    "passage": "Over 30 000 years ago,people from northern Asia went to America.Today we can tell these people Indians. The Indians went to America because the weather began to change.Northern Asia became very cold.Everything froze.They had to move or they would die.How did the first Indians go to America? They walked! Later Columbus found the New World in 1492.At first,only a few Europeans followed.They traveled to America in boats.For the next 300 years,about 500 000 people went there.Then the number grew very quickly. From 1815 to 1915,over 32 000 000 Europeans left their countries for the United States.The biggest groups went from Germany and Italy.These Europeans spoke many different languages. Most of them took almost no money.They went to America to find a better life.",
    "history": [
        ["Teacher", "You are right. Do you know why the Indians went to America?"],
        ["Student", "They were interested in America."]
    ],
    "reply_candidates": [
        ["Human", "Are you sure? It was related to the weather change."],
        ["DIRECT", "No, it is related to the weather."],
        ["PrepTutor", "According to the story, the north american islands were cold and windy. so the people of the north america decided to go to america. where did they go?"],
        ["GPT-3.5", "That's not quite right. Think about the weather in northern Asia."],
        ["GPT-4", "That's a good guess, but try to think about the environmental conditions in Northern Asia at that time. Why might they have needed to leave their homes?"]
    ],
    "ranking": ["GPT-4", "Human", "GPT-3.5", "DIRECT", "PrepTutor"]
}

teacher_img_path = "./image/profile_teacher.png"
student_img_path = "./image/profile_student.png"
teacher_image_base64 = get_base64(teacher_img_path)
student_image_base64 = get_base64(student_img_path)


# --- 세션 상태 초기화 함수 ---
def initialize_chat():
    st.session_state.messages = [
        {"role": "teacher", "content": f"Hello! Let's start our lesson. Please read the story below.\n\n---\n\n**Story:**\n\n{TUTORING_DATA['passage']}"},
        {"role": "teacher", "content": "Great! Now, let's check your understanding."},
        {"role": "teacher", "content": TUTORING_DATA["history"][0][1]},
        {"role": "student", "content": TUTORING_DATA["history"][1][1]}
    ]
    st.session_state.feedback_sent = False

if "messages" not in st.session_state:
    initialize_chat()

if st.session_state.get("active_page") != "tutoring_demo":
    initialize_chat()
    st.session_state.active_page = "tutoring_demo"


st.title("💬 English Tutoring Chat")
col_panel, col_chat = st.columns([1, 2])


# --- 왼쪽 컬럼: 교사 액션 패널 ---
with col_panel:
    with st.container(border=True):
        st.subheader("🧑‍🏫 Teacher's Action Panel")
        st.markdown("---")
        
        if not st.session_state.feedback_sent:
            st.markdown("<h5>Recommended Feedbacks</h5>", unsafe_allow_html=True)
            st.info("These are the recommended feedbacks, ranked in order. The top feedback is the most recommended.")            
            sorted_candidates = get_sorted_candidates(
                TUTORING_DATA["reply_candidates"],
                TUTORING_DATA["ranking"]
            )
            
            selected_feedback = st.radio(
                "Feedback Candidates:",
                sorted_candidates,
                index=0,
                label_visibility="collapsed"
            )

            if st.button("🚀 Send Feedback", use_container_width=True):
                feedback_text_to_send = selected_feedback.split(":", 1)[1].strip()
                st.session_state.messages.append({"role": "teacher", "content": feedback_text_to_send})
                st.session_state.feedback_sent = True
                st.rerun()
        else:
            st.success("Feedback sent successfully.")
            st.info("Waiting for the student's next response. You can also reset the simulation.")
            
        if st.button("🔄 Reset Simulation", use_container_width=True):
            initialize_chat()
            st.rerun()

# --- 오른쪽 컬럼: 채팅창 ---
with col_chat:
    chat_container = st.container(height=600, border=True)
    with chat_container:
        if teacher_image_base64 and student_image_base64:
            for message in st.session_state.messages:
                role_is_teacher = message["role"] == "teacher"
                img_b64 = teacher_image_base64 if role_is_teacher else student_image_base64
                
                if role_is_teacher:
                    st.markdown(f"""
                    <div class="message-row teacher">
                        <img class="profile-pic" src="data:image/png;base64,{img_b64}" />
                        <div class="teacher-bubble">{message["content"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="message-row student">
                        <div class="student-bubble">{message["content"]}</div>
                        <img class="profile-pic" src="data:image/png;base64,{img_b64}" />
                    </div>
                    """, unsafe_allow_html=True)

    if student_response := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "student", "content": student_response})
        st.rerun()

# --- 자동 스크롤 방지를 위한 JavaScript ---
components.html(
    """<script> window.scrollTo(0, 0); </script>""",
    height=0 
)