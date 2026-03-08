import streamlit as st

st.title("Personalized Study Plan Generator")

marks = st.number_input("Enter your marks", 0, 100)
hours = st.number_input("Available study hours", 1, 12)

if st.button("Generate Plan"):

    if marks < 40:
        st.write("Focus on basics and study", hours, "hours daily")

    elif marks < 70:
        st.write("Revise topics and practice problems for", hours, "hours")

    else:
        st.write("Solve advanced problems and take mock tests for", hours, "hours")



