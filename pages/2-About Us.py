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
    st.subheader("Vision 👁️")
    st.write("""To integrate AI and healthcare, making breast cancer diagnosis faster and more precise, 
             ultimately improving patient outcomes worldwide.""")
    st.subheader("Mission 🎗️")
    st.write("""To leverage technology for eargly breast cancer diagnosis and personalized treatment, 
             empowering healthcare providers with accurate, data-driven insights.""")

if __name__=="__main__":
    main()