import streamlit as st

def set_page_config():
    """Set the initial page configuration."""
    st.set_page_config(
        page_icon="",
        page_title="Breast Cancer Analysis",
        layout="wide",
        initial_sidebar_state="expanded",
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
    
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    
    if st.session_state['logged_in']:
        st.write ("[Login Successful](./pages/1-Home.py)") 
    else:
        login_form()

if __name__ == '__main__':
    main()