import pandas as pd
import streamlit as st

st.title("Streamlit text input")

name = st.text_input("Enter your name : ")

age = st.slider("Select age: ", 0, 100, 29)
st.write(f"Your age is {age}")

options = ["Java", "Python", "Javascript"]
choice = st.selectbox("Select favourite language : ", options)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}")

uploaded_file = st.file_uploader("Choose a csv file : ", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
