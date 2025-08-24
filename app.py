import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="🚀", layout="centered")

st.title("🚀 Streamlit on Hugging Face")
st.write("This is a demo Streamlit app deployed on Hugging Face Spaces.")

# Simple interactive input
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}! 🎉 Welcome to your Hugging Face Space.")
