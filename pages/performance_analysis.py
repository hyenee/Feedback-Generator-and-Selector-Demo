import streamlit as st
from streamlit_option_menu import option_menu
import base64

def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"이미지 파일을 찾을 수 없습니다: {file_path}")
        return None

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="Performance Analysis", page_icon="📊", layout="wide", initial_sidebar_state="collapsed" )

# st.markdown("""
#     <style>
#     html, body, [class*="st-"], [class*="css-"] {
#         font-size: 1.1rem; /* 기본 폰트 크기보다 10% 크게 (이 값을 조절하세요) */
#     }
#     </style>
#     """, unsafe_allow_html=True)

# st.session_state.active_page = "performance_analysis"

col1, _ = st.columns([0.3, 0.7]) 
with col1:
    if st.button("⬅️ Back to How It Works"):
        st.switch_page("pages/how_it_works.py")

with st.sidebar:
    st.page_link("home.py", label="Home", icon="🏠")
    st.page_link("pages/how_it_works.py", label="How It Works", icon="⚙️")
    st.page_link("pages/tutoring_demo.py", label="Tutoring Demo", icon="👩‍🏫")
    st.markdown("---")

# selected = option_menu(
#     menu_title=None,
#     options=["Home", "How It Works", "Tutoring Demo"],
#     icons=["house", "gear", "chat-dots"],
#     menu_icon="cast",
#     default_index=1,
#     orientation="horizontal",
# )

# if selected == "Home":
#     st.switch_page("home.py")
# if selected == "How It Works":
#     st.switch_page("pages/how_it_works.py")
# if selected == "Tutoring Demo":
#     st.switch_page("pages/tutoring_demo.py")

# --- 페이지 콘텐츠 ---
st.title("📊 Ranking Model Performance Analysis")
st.info("Click the tabs below to view the experimental results.")

# --- 탭 생성 ---
tab1, tab2, tab3, tab4 = st.tabs([
    "1️⃣ RQ1: Overall Performance", 
    "2️⃣ RQ2: Hybrid Training Analysis", 
    "3️⃣ RQ3: Criteria Impact Analysis",
    "🔍 Case Study"
])


# --- RQ1 탭 ---
with tab1:
    st.subheader("RQ1: Comparison of Ranking Model Performance")
    st.write("This compares the overall performance of models trained on DIRECT-Generated with those trained on DIRECT-Manual.")
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        st.image('./image/performance/performance.png') 
        
# --- RQ2 탭 ---
with tab2:
    st.subheader("RQ2: Performance Analysis by DM Ratio in the DA→DM Scenario")
    st.write("This analyzes the effective ratio of DIRECT-Manual data within the DIRECT-Augmented dataset.")

    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        st.image('./image/performance/performance.ratio.Llama-1B.png', caption='Llama-1B')
        st.image('./image/performance/performance.ratio.Llama-1B-IT.png', caption='Llama-1B-IT')
        st.image('./image/performance/performance.ratio.Llama-3B.png', caption='Llama-3B')
        st.image('./image/performance/performance.ratio.Llama-3B-IT.png', caption='Llama-3B-IT')
        st.image('./image/performance/performance.ratio.Qwen-3B-IT.png', caption='Qwen-3B-IT')

# --- RQ3 탭 ---
with tab3:
    st.subheader("RQ3: Performance Analysis by Number of Feedback Criteria")
    st.write("This analyzes the impact of the number of feedback criteria on the ranking model's performance.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image('./image/performance/criteria_comparison.Llama-1B.png', caption='Llama-1B')
        st.image('./image/performance/criteria_comparison.Llama-3B.png', caption='Llama-3B')
        st.image('./image/performance/criteria_comparison.Qwen-3B-IT.png', caption='Qwen-3B-IT')
    with col2:
        st.image('./image/performance/criteria_comparison.Llama-1B-IT.png', caption='Llama-1B-IT')
        st.image('./image/performance/criteria_comparison.Llama-3B-IT.png', caption='Llama-3B-IT')


# --- Case Study 탭 ---
with tab4:
    st.subheader("🔍 Case Study")

    st.markdown("""
    <style>
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
        
        .ranking-card {
            border: 1px solid #e1e1e1; border-radius: 10px;
            padding: 15px; background-color: #f9f9f9;
        }
    </style>
    """, unsafe_allow_html=True)

    teacher_img_path = "./image/profile_teacher.png" 
    student_img_path = "./image/profile_student.png"
    
    teacher_image_base64 = get_base64(teacher_img_path)
    student_image_base64 = get_base64(student_img_path)

    story_text = """
        Hundreds of years ago, life was much harder than it is today. People didn't have modern machines. There was no modern medicine, either. Life today has brought new problems. One of the biggest is pollution. Water pollution has made our rivers and lakes dirty. It kills our fish and pollutes our drinking water. Noise pollution makes us talk louder and become angry more easily. Air pollution is the most serious kind of pollution. It's bad to all living things in the world. Cars, planes and factories all pollute our air every day. Sometimes the polluted air is so thick that it is like a quilt over a city. This kind of quilt is called smog. Many countries are making rules to fight pollution. Factories must now clean their water before it is thrown away and they mustn't blow dirty smoke into the air. We need to do many other things. We can put waste things in the dustbin and do not throw them on the ground, there will be less pollution. Rules are not enough. Every person must help to fight pollution.
    """
    
    feedback_candidates = {
        "Human": "It costs 20,000 to 30,000 or more dollars if you add all the expenses of a year.",
        "DIRECT": "No, the cost of tuition is over us$10, 000 per year.",
        "PrepTutor": "Good effort! frankly, a college education is not cheap. but, students who attend college earn many years of free education. how much will a college student spend on his or her education?",
        "GPT-3.5": "That's close, but it's actually higher than that. Can you think of any other expenses that students have to pay for?",
        "GPT-4": "That's a good start, but remember, the $10,000 is just the average cost of tuition. There are other expenses a student needs to consider like books, housing, and personal expenses. Try to add all these up for a full picture of the annual cost."
    }
    
    predicted_ranking_list = ["GPT-4", "GPT-3.5", "PrepTutor", "Human", "DIRECT"]
    ground_truth_ranking_list = ["GPT-4", "GPT-3.5", "DIRECT", "Human", "PrepTutor"]
    
    # --- [핵심 수정 2] 1등 피드백 텍스트 추출 ---
    top_ranked_feedback_name = predicted_ranking_list[0] # "GPT-4"
    top_ranked_feedback_text = feedback_candidates[top_ranked_feedback_name]

    # --- 2단 레이아웃 생성 ---
    col1, col2 = st.columns([3, 2])

    # --- 왼쪽 컬럼: Story 및 Chat Simulation ---
    with col1:
        st.subheader("📝 Story")
        st.container(height=200).markdown(story_text)
        st.subheader("💬 Chat Simulation")
        
        # --- 1등 피드백을 채팅 기록에 동적으로 추가 ---
        chat_history = [
            {"role": "teacher", "text": "Why was a life much harder than it is today hundreds of years ago?"},
            {"role": "student", "text": "Because there were not any modern machines."},
            {"role": "teacher", "text": top_ranked_feedback_text}
        ]
        
        if teacher_image_base64 and student_image_base64:
            for msg in chat_history:
                if msg["role"] == "teacher":
                    st.markdown(f"""
                    <div class="message-row teacher">
                        <img class="profile-pic" src="data:image/png;base64,{teacher_image_base64}" />
                        <div class="teacher-bubble">{msg["text"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="message-row student">
                        <div class="student-bubble">{msg["text"]}</div>
                        <img class="profile-pic" src="data:image/png;base64,{student_image_base64}" />
                    </div>
                    """, unsafe_allow_html=True)

    # --- 오른쪽 컬럼: Feedback Candidates 및 Ranking Analysis ---
    with col2:
        st.subheader("🧑‍🏫 Feedback Candidates")
        for name, text in feedback_candidates.items():
            st.markdown(f"- **{name}**: {text}")

        st.subheader("📊 Ranking Analysis")
        
        with st.container(border=True):
            ground_truth_str = " > ".join(ground_truth_ranking_list)
            predicted_str = " > ".join(predicted_ranking_list)
            
            st.success(f"**Ground-truth Ranking:**\n{ground_truth_str}")
            st.warning(f"**Predicted Ranking:**\n{predicted_str}")
            st.metric(label="RBO Score", value="0.8833", help="Values closer to 1 indicate higher similarity between the two rankings.")
