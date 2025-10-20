import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import base64
import time

def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"이미지 파일을 찾을 수 없습니다: {file_path}")
        return None


def get_sorted_candidates(candidates, ranking_list):
    candidates_dict = {item[0].lower(): item[1] for item in candidates}
    formatted_candidates = []
    for name in ranking_list:
        feedback_text = candidates_dict.get(name.lower())
        if feedback_text:
            formatted_candidates.append(f"{name}: {feedback_text}")
    return formatted_candidates


def initialize_chat(tutoring_data):
    return [
        {"role": "teacher", "content": f"Hello! Let's start our lesson. Please read the story below.\n\n---\n\n**Story:**\n\n{tutoring_data['passage']}"},
        {"role": "teacher", "content": "Great! Now, let's check your understanding."},
        {"role": "student", "content": "Okay! I'm ready."},
        {"role": "teacher", "content": tutoring_data["history"][0][1]},
        {"role": "student", "content": tutoring_data["history"][1][1]},
    ]


st.set_page_config(page_title="Tutoring Demo", page_icon="👩‍🏫", layout="wide", initial_sidebar_state="collapsed")
components.html("""<script> window.scrollTo(0, 0); </script>""", height=0)

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


st.markdown("""
<style>
.message-row { display: flex; align-items: flex-end; margin-bottom: 15px; }
.message-row.teacher { justify-content: flex-start; }
.message-row.student { justify-content: flex-end; }
.profile-pic { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }
.teacher-bubble {
    background-color: #E7F5FF; border: 1px solid #BCE0FD; color: #333; border-radius: 10px;
    padding: 10px 15px; margin-left: 10px; max-width: 80%; font-size: 0.95rem;
}
.student-bubble {
    background-color: #F0F0F0; border: 1px solid #E0E0E0; color: #333; border-radius: 10px;
    padding: 10px 15px; margin-right: 10px; max-width: 80%; font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

teacher_image_base64 = get_base64("./image/profile_teacher.png")
student_image_base64 = get_base64("./image/profile_student.png")

TUTORING_EXAMPLES = {
    "Example 1": {
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
            ["GPT-4", "That's a good guess, but try to think about the environmental conditions in Northern Asia at that time. Why might they have needed to leave their homes?"] ],
        "ranking": ["GPT-4", "Human", "GPT-3.5", "DIRECT", "PrepTutor"]
    },
    "Example 2": {
        "passage": "A woman is at the cinema, and she is enjoying the film very much, but there is a man in the next seat, and he begins looking at the floor under her. The woman is _ and asks, \"What are you doing there?\" What are you looking for? \"A piece of chocolate\", the man says to her, \"I drop   it on the floor.\"\n \"A piece of chocolate?\" the woman says angrily, \"It is dirty now.\" Take this and be quiet, please. I am listening to the film.\" She gives the man a big piece of chocolate. But the man says, \"One of my teeth is in the chocolate!\"",
        "history": [
            ["Teacher", "Right. / Why does she give him a piece of chocolate?"],
            ["Student", "Because she likes the man."]
        ],
        "reply_candidates": [
            ["Human", "Well, she asks him to be quiet."],
            ["DIRECT", "Not at all. she wants to be quiet."],
            ["PrepTutor", "According to the story, the woman says she likes the movie because it is dirty and she does not like seeing it often. what does the woman want from the movie?"],
            ["GPT-3.5", "Not quite. Think about what she wants to do while watching the film."],
            ["GPT-4", "Hmm, not quite. Think about her reaction when the man is looking for his chocolate. Why might she want him to stop?"]
        ],
        "ranking": ["GPT-3.5", "GPT-4", "Human", "DIRECT", "PrepTutor"]
    }
}

st.title("💬 English Tutoring Chat")
tab1, tab2 = st.tabs(["Example 1", "Example 2"])

def render_tutoring_tab(example_data, key_prefix):
    msg_key = f"messages_{key_prefix}"
    anim_key = f"anim_index_{key_prefix}"
    auto_key = f"auto_feedback_sent_{key_prefix}"

    if msg_key not in st.session_state:
        st.session_state[msg_key] = initialize_chat(example_data)
        st.session_state[auto_key] = False
        st.session_state[anim_key] = 1

    col_panel, col_chat = st.columns([1, 2])

    # ---------------- Left Panel ----------------
    with col_panel:
        with st.container(border=True):
            st.markdown("#### 🧑‍🏫 Teacher's Action Panel")
            st.markdown("---")

            st.markdown("<h5>Recommended Feedbacks</h5>", unsafe_allow_html=True)
            sorted_candidates = get_sorted_candidates(example_data["reply_candidates"], example_data["ranking"])

            if sorted_candidates:
                for i, feedback in enumerate(sorted_candidates):
                    if i == 0:
                        st.markdown(f"<p style='font-weight:700;'>{feedback}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='color:#555;'>{feedback}</p>", unsafe_allow_html=True)

            if not st.session_state[auto_key] and sorted_candidates:
                top_feedback_text = sorted_candidates[0].split(":", 1)[1].strip()
                st.session_state[msg_key].append({"role": "teacher", "content": top_feedback_text})
                st.session_state[auto_key] = True
                st.rerun()

    # ---------------- Right Chat ----------------
    DELAY_SECONDS = 1.5
    with col_chat:
        chat_container = st.container(height=600, border=True)
        with chat_container:
            placeholder = st.empty()

            if teacher_image_base64 and student_image_base64:
                with placeholder.container():
                    for message in st.session_state[msg_key][:st.session_state[anim_key]]:
                        role_is_teacher = message["role"] == "teacher"
                        img_b64 = teacher_image_base64 if role_is_teacher else student_image_base64
                        bubble_class = "teacher-bubble" if role_is_teacher else "student-bubble"
                        row_class = "teacher" if role_is_teacher else "student"
                        st.markdown(f"""
                        <div class="message-row {row_class}">
                            <img class="profile-pic" src="data:image/png;base64,{img_b64}" />
                            <div class="{bubble_class}">{message["content"]}</div>
                        </div>
                        """, unsafe_allow_html=True)

                for i in range(st.session_state[anim_key] + 1, len(st.session_state[msg_key]) + 1):
                    time.sleep(DELAY_SECONDS)
                    with placeholder.container():
                        for message in st.session_state[msg_key][:i]:
                            role_is_teacher = message["role"] == "teacher"
                            img_b64 = teacher_image_base64 if role_is_teacher else student_image_base64
                            bubble_class = "teacher-bubble" if role_is_teacher else "student-bubble"
                            row_class = "teacher" if role_is_teacher else "student"
                            st.markdown(f"""
                            <div class="message-row {row_class}">
                                <img class="profile-pic" src="data:image/png;base64,{img_b64}" />
                                <div class="{bubble_class}">{message["content"]}</div>
                            </div>
                            """, unsafe_allow_html=True)
                    st.session_state[anim_key] = i


with tab1:
    render_tutoring_tab(TUTORING_EXAMPLES["Example 1"], "ex1")

with tab2:
    render_tutoring_tab(TUTORING_EXAMPLES["Example 2"], "ex2")