import streamlit as st

def set_page_config():
    """Set the initial page configuration."""
    st.set_page_config(
        page_icon="",
        page_title="Breast Cancer Analysis",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def analysis_form():
    st.header("Input Your Information")

    name = st.text_input("Name:")
    address = st.text_input("Address:")

    if st.button("Submit"):
        st.write(f"Name: {name}")
        st.write(f"Address: {address}")


def main():
    set_page_config()
    st.title("Breast Cancer Analysis")
    analysis_form()

if __name__=="__main__":
    main()