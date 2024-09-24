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
    st.title("About")

if __name__=="__main__":
    main()