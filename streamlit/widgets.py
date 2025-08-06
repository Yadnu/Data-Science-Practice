import streamlit as st
import pandas as pd
st.title("streamlit text input")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}")

options = ["Python", "JAVA", "C++", "JS", "TS", "RUST"]
choice = st.selectbox("Choose your favourite lang:", options)
st.write(f"You selected {choice}.")

selectbox = st.select_slider("Select lang:", options)
st.write(f"You selected: {selectbox}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")

st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)