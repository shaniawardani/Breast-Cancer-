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

def authenticate(username, password):
    
    valid_users = {
        "shania": "12345678",
        "test": "test123",
    }
    
   
    if username in valid_users and valid_users[username] == password:
        return True
    else:
        return False


def login_form():
    st.title("Sign Up")

    email = st.text_input("email")
    username = st.text_input("username")
    password = st.text_input("Password", type="password")

    
    if st.button("Sign Up"):
        st.write ("[Sign Up Succesfull](../Dashboard.py)")


def main():
    inject_custom_css()
    render_sidebar()
    login_form()
if __name__ == '__main__':
    main()