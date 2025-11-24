import streamlit as st

st.set_page_config(page_title = "DnD!")


st.title("Welcome to the Party")
st.sidebar.header("Choose a Character ⤴︎")
st.divider()

st.header("The story so far...")


st.write(
    "Bogart, Dank, Greenik, and Zetze found themselves at the start of another"
    "adventure. Instructed they were, to enter a cave and find some missing folks"
    "- as well as some bad apples. They encountered a suspiciously helpful goblin"
    ", Grob, and decided to bring him along. Rooms were explored, fights were fought,"
    "& foot wine was had by all. [Big Bad] was tracked down to his lair. Hijinks ensued."
)

st.write(
    "After a gruelling final battle with [Big Bad], the team has finally completed the mission that"
    "brought them into the dungeon in the first place. They have found themselves back"
    "in the little town they'd started in."
)
