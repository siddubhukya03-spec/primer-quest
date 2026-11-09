
import streamlit as st
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio.SeqUtils import MeltingTemp as mt

st.set_page_config(
    page_title="Primer Quest",
    page_icon="🧬"
)

st.title("🧬 PRIMER QUEST")
st.subheader("The Bioinformatics Adventure")

st.write("Welcome to the world of DNA!")
st.write("Complete 15 levels to become a DNA Master.")

# Game questions
levels = [
    ("Complement of ATGC", "TACG"),
    ("Reverse complement of AAGC", "GCTT"),
    ("Length of ATGCGTAC", "8"),
    ("GC percentage of GCGCATAT", "50"),
    ("Count G in ATGCGG", "3"),
    ("Convert ATGC into RNA", "AUGC"),
    ("Is ATGB valid DNA? YES or NO", "NO"),
    ("Tm of ATGC using Wallace rule", "12"),
    ("Complement of CGTA", "GCAT"),
    ("GC percentage of GGGCCC", "100"),
    ("Reverse complement of AGTC", "GACT"),
    ("Length of GATTACA", "7"),
    ("Tm of GCGCGC using Wallace rule", "24"),
    ("Translate ATGGCTTAA into protein", "MA*"),
    ("GC percentage and Tm of ATGCGC (GC,Tm)", "100,24")
]

# Store game progress
if "level" not in st.session_state:
    st.session_state.level = 0
    st.session_state.score = 0

# Display current level
if st.session_state.level < 15:

    number = st.session_state.level
    question, answer = levels[number]

    st.progress(number / 15)

    st.header("Level " + str(number + 1))
    st.write("🎯 Mission:", question)

    user = st.text_input(
        "Enter your answer",
        key="answer_" + str(number)
    )

    if st.button("Submit Answer"):

        if user.strip().upper() == answer:
            st.success("Correct! +10 points!")
            st.session_state.score += 10
            st.session_state.level += 1
            st.rerun()

        else:
            st.error("Incorrect! Try again.")

    st.metric("Your Score", str(st.session_state.score) + "/150")

else:

    st.balloons()
    st.title("🏆 DNA MASTER!")
    st.success("Congratulations! All 15 levels completed.")

    st.write("Final Score:", st.session_state.score, "/150")

    if st.button("Play Again"):
        st.session_state.level = 0
        st.session_state.score = 0
        st.rerun()
