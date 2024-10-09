import streamlit as st

def set_page_config():
    """Set the initial page configuration."""
    st.set_page_config(
        page_icon="",
        page_title="Breast Cancer Analysis",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def inject_custom_css():
    """Inject custom CSS for styling."""
    st.markdown(
        """
        <style>
        /* Styling the header image */
        .header-image {
            width: 100%;
            height: auto;
        }
        
        /* Change the background color of the sidebar */
        [data-testid="stSidebar"] {
            background-color: #FFB3D9;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_sidebar():
    """Render the sidebar with navigation."""
    with st.sidebar:
        st.markdown(
            "![Logo](https://github.com/shaniawardani/Breast-Cancer-/blob/main/asset/logo.png?raw=true)"
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
    inject_custom_css()
    render_sidebar()
    st.title("Breast Cancer Analysis")
    analysis_form()

if __name__=="__main__":
    main()