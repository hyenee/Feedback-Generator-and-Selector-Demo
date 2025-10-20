import streamlit as st
import pandas as pd
import base64 

def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

st.set_page_config(page_title="DIRECT-Generated", page_icon="📄", layout="wide", initial_sidebar_state="collapsed" )

col1, _ = st.columns([0.3, 0.7]) 
with col1:
    if st.button("⬅️ Back to How It Works"):
        st.switch_page("pages/how_it_works.py")

with st.sidebar:
    st.page_link("home.py", label="Home", icon="🏠")
    st.page_link("pages/how_it_works.py", label="How It Works", icon="⚙️")
    st.page_link("pages/tutoring_demo.py", label="Tutoring Demo", icon="👩‍🏫")
    st.markdown("---")


# --- 채팅 UI를 위한 CSS ---
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
</style>
""", unsafe_allow_html=True)


# --- 페이지 콘텐츠 ---
st.title("📄 Teacher Feedback Generation")
st.info("Here are some real examples from the DIRECT-Generated dataset created in this study.")


with st.container(border=True):
    st.markdown("**Story:**")
    st.markdown("""
    Lisa has a pet cat named Whiskers. Whiskers is black with a white spot on her chest. 
    Whiskers also has white paws that look like little white mittens.
    Whiskers likes to sleep in the sun on her favorite chair. 
    Whiskers also likes to drink creamy milk.
    Lisa is excited because on Saturday, Whiskers turns two years old.
    After school on Friday, Lisa rushes to the pet store. She wants to buy Whiskers' birthday presents. 
    Last year, she gave Whiskers a play mouse and a blue feather.
    For this birthday, Lisa is going to give Whiskers a red ball of yarn and a bowl with a picture of a cat on the side. 
    The picture is of a black cat. It looks a lot like Whiskers.
    """)
    st.markdown("---")

    teacher_img_path = "./image/profile_teacher.png" 
    student_img_path = "./image/profile_student.png"
    teacher_image_base64 = get_base64(teacher_img_path)
    student_image_base64 = get_base64(student_img_path)

    answer_options = {
        "A": "Today",
        "B": "Last year",
        "C": "Friday",
        "D": "Saturday"
    }

    options_str = ""
    for key, value in answer_options.items():
        options_str += f"- <b>{key}</b>: {value}<br>"

    context_chat = [
        {"role": "teacher", "text": "What day is Whisker's Birthday?"},
        {"role": "teacher", "text": f"""{options_str}"""},
        {"role": "student", "text": f"The answer is B: {answer_options['B']}"}
    ]

    # 채팅 UI 렌더링
    if teacher_image_base64 and student_image_base64:
        for msg in context_chat:
            if msg["role"] == "teacher":
                st.markdown(f"""
                <div class="message-row teacher">
                    <img class="profile-pic" src="data:image/png;base64,{teacher_image_base64}" />
                    <div class="teacher-bubble">{msg["text"]}</div>
                </div>
                """, unsafe_allow_html=True)
            else: # role == "student"
                st.markdown(f"""
                <div class="message-row student">
                    <div class="student-bubble">{msg["text"]}</div>
                    <img class="profile-pic" src="data:image/png;base64,{student_image_base64}" />
                </div>
                """, unsafe_allow_html=True)

st.markdown("##")

st.subheader("Educational Feedback Criteria Definition")
criteria_list = [
    {
        "icon": "✅",
        "title": "Correct",
        "description": "Ensures feedback is factually accurate and directly relevant to the student's response and the question."
    },
    {
        "icon": "💡",
        "title": "Revealing",
        "description": "Avoids explicitly stating the answer, instead guiding the student to arrive at it on their own."
    },
    {
        "icon": "🗺️",
        "title": "Guidance",
        "description": "Provides specific directions or hints to help the student correct their errors and move toward the correct answer."
    },
    {
        "icon": "🩺",
        "title": "Diagnostic",
        "description": "Clearly identifies and corrects the student's misunderstandings or misconceptions, pointing out what was wrong and why."
    },
    {
        "icon": "👍",
        "title": "Encouragement",
        "description": "Uses a positive and supportive tone to encourage active participation without fear of making mistakes."
    }
]

with st.container(border=True):
    for i, criterion in enumerate(criteria_list):
        st.markdown(f"**{criterion['icon']} {criterion['title']}**: {criterion['description']}")


DG_examples = [
    {
        "Model": "GPT-4o",
        "Feedback with criteria (fʷ)": "Remember to find the specific day mentioned in the story for Whiskers' birthday, rather than focusing on past events.",
        "Feedback without criteria (fʷᵒ)": "Revisit the passage to determine the exact day Whiskers will turn two years old."
    },
    {
        "Model": "Claude-3",
        "Feedback with criteria (fʷ)": "Let's take another look at the story and focus on the specific day mentioned for Whiskers' upcoming birthday celebration.",
        "Feedback without criteria (fʷᵒ)": "While the story mentions `last year', it clearly states that Whiskers' birthday is on Saturday, so let's look for that specific day in the text."
    },
    {
        "Model": "Llama-3.1-70B",
        "Feedback with criteria (fʷ)": "Let's take another look at the story and see if we can find a specific day of the week when Whiskers' birthday is mentioned.",
        "Feedback without criteria (fʷᵒ)": "To answer this question correctly, look for the specific day mentioned in the story when Whiskers turns two years old, which is actually mentioned as Saturday."
    }
]

st.markdown("##")
st.subheader("Teacher Feedback Generation using Large Language Models")
st.markdown("""
In this study, using the **five feedback criteria** established above, we generated feedback in two different ways for the same tutoring scenario using LLMs:
- **Feedback with criteria (fʷ):** Feedback generated by explicitly including the five criteria in the prompt.
- **Feedback without criteria (fʷᵒ):** General feedback generated without any specific criteria.

The table below shows the feedback generated by the **GPT-4o, Claude-3, and Llama-3.1-70B** models for each approach.
""")

df = pd.DataFrame(DG_examples)    
st.dataframe(
    df,
    height=150,
    use_container_width=True,
    hide_index=True
)

st.markdown("##")
st.title("Automatic Annotated Teacher Feedback Construction")
st.markdown("""
Based on the hypothesis that `w/ criteria` feedback is superior, we automatically create preference pairs in the `(chosen, rejected)` format to complete the **`DIRECT-Generated`** dataset.
""")

preference_pair = [
    {
        "chosen":"You may want to re-read the passage and look for the person who is mentioned alongside John in several activities, including starting a peach farm, to find his best friend.",
        "rejected":"The text states 'John and his best friend, Rick, shared their love for peaches,' indicating that Rick is John's best friend, not Stephanie, who is actually John's mother."
    },
    {
        "chosen":"You provided the name of one of Harry's friends, but think back to the beginning of the story where Harry's pet is introduced, what was its name?",
        "rejected":"Reread the story carefully to see which character Bird flew to visit after talking to Fox."
    },
    {
        "chosen":"Consider what the zoo worker did that directly improved the monkey's feeling after eating the napkins.",
        "rejected":"You might want to reconsider the number of trips Jim made to the store, as the passage mentions him driving back to the store after realizing he had forgotten something."
    },
    {
        "chosen":"Remember to carefully read the last part of the story, which describes what the brothers found when they looked under the cups.",
        "rejected":"While the white cup was involved initially, the story clearly states that a green ball was found inside the green cup at the end of the trick."
    },
    {
        "chosen":"Remember to refer to the beginning of the story where Tom's pet is explicitly mentioned.",
        "rejected":"Re-read the passage to identify the specific activity George was engaged in when Laura found him at the park."
    },
    {
        "chosen":"Consider re-examining the passage where it describes John and Rick waiting for their peach trees to bear fruit, as the timeframe mentioned might not be the same as the one you chose.",
        "rejected":"Consider re-examining the timeline in the story, as the first peach grew after 6 years of waiting, not 17 years."
    },
    {
        "chosen":"Consider Mary's actual explanation when her family asked why she felt sick, paying attention to what she specifically said caused her sickness.",
        "rejected":"Remember to review the part of the story where Mary explains her sickness to her family; she lied about being stung by a bee."
    },
    {
        "chosen":"Consider revisiting the story to find where the family went and what activities they did to correctly identify the main event of the day.",
        "rejected":"Let's revisit the story carefully and focus on the part that describes Jim's previous sighting, as it contains important information about his location at that time."
    },
    {
        "chosen":"Re-examine the passage to find the specific types of food Brendan gives to his cats, considering the distinction he makes between food suitable for cats and food that isn't.",
        "rejected":"While Brendan does give his cats special treats, it's specified that he doesn't feed them candy, and it's implied that he feeds them regular cat food, so the correct answer should reflect both."
    },
    {
        "chosen":"Remember to refer back to the part of the story that mentions the witch's best treat specifically named in the text.",
        "rejected":"Remember, the story specifies that the witch's best treat is strawberry eggs, not blueberry sandwiches."
    }
]

table_data = []
for item in preference_pair:
    table_data.append({
        "Chosen Feedback (fʷ)": item["chosen"],
        "Rejected Feedback (fʷᵒ)": item["rejected"]
    })

df = pd.DataFrame(table_data)
st.dataframe(
    df,
    height=400, 
    use_container_width=True,  
    hide_index=True
)
