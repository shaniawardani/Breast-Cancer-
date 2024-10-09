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
            """
            <div style="text-align: center;">
                <img src='https://github.com/shaniawardani/Breast-Cancer-/blob/main/asset/logo.png?raw=true' class='sidebar-logo'/>
            </div>
            """, unsafe_allow_html=True
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
    st.title("Login")

    
    username = st.text_input("username")
    password = st.text_input("Password", type="password")

    
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state['logged_in'] = True  
            st.session_state['username'] = username 
            st.success("Login Successful!")
        else:
            st.error("Username or Password false!")


def main():
    inject_custom_css()
    render_sidebar()
    
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    
    if st.session_state['logged_in']:
        st.write ("[Login Successful](http://localhost:8501/)") 
    else:
        login_form()

if __name__ == '__main__':
    main()