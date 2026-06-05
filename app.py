import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Mahindra University - School of Management",
    page_icon="🎓",
    layout="centered"
)

# Header
st.title("🎓 Mahindra University")
st.subheader("School of Management")

# Welcome message
st.write("Welcome to the School of Management Streamlit App!")

# Simple interaction
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}! Welcome to Mahindra University School of Management.")

# Footer
st.markdown("---")
st.caption("Built with Streamlit")