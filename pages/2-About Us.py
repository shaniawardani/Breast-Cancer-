import streamlit as st

def set_page_config():
    """Set the initial page configuration."""
    st.set_page_config(
        page_icon="",
        page_title="Breast Cancer Analysis",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def main():
    set_page_config()
    st.title("About Us 🌐")
    st.write("""Welcome to Breast Cancer Analysis, a website dedicated to empowering patients, healthcare professionals, 
             and researchers with advanced tools for understanding and diagnosing breast cancer. Our platform leverages 
             cutting-edge machine learning technology to analyze medical data, providing accurate and efficient breast 
             cancer classification to aid in early detection and personalized treatment plans.""")
    st.subheader("Our Mission 🎗️")
    st.write("""Our mission is to harness the power of technology to support the early diagnosis and effective management 
             of breast cancer. We believe that with the right tools and timely information, healthcare providers can make better, 
             more informed decisions, leading to improved outcomes for patients around the world.""")
    st.subheader("Why Breast Cancer Analysis? 🔬")
    st.write("""Breast cancer affects millions of people globally, and early detection is crucial for successful treatment. 
             However, accurately classifying the type of cancer can be complex and time-consuming. Our website aims to make
             this process faster and more precise through innovative AI-driven analysis. By providing healthcare providers 
             with the insights they need, we strive to make a difference in the lives of patients everywhere.""")
    st.subheader("Our Vision 👁️")
    st.write("""We envision a future where technology and healthcare work hand-in-hand to fight breast cancer more effectively.
              With continuous improvements in our algorithms and data capabilities, we aim to become a trusted resource for breast 
             cancer diagnosis and research, improving patient outcomes and supporting medical advancements.""")

if __name__=="__main__":
    main()