import streamlit as st


def set_page_config():
    """Set the initial page configuration."""
    st.set_page_config(
        page_icon="./asset/logo.png",
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
        <img src='https://github.com/shaniawardani/Breast-Cancer-/blob/main/asset/jumbotronnew.png?raw=true' class='header-image'/>
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
        
def main():
    set_page_config()
    render_sidebar()
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write(f"Halo, {st.session_state['username']}!")
        
        col1,col2=st.columns(2)
        with col1:
            
            st.markdown(
                """
                <h1 style='color: #1E1E1E;'>
                    Fighting 
                    <span style='color: #AF0B56;'>Breast Cancer</span> 
                    Takes Everyone
                </h1>
                """,
                unsafe_allow_html=True
            )
            st.write("Cancer may challenge your body but it can never break your spirit.")
        with col2:
            inject_custom_css()
    else:
        st.warning("You are not logged in. Please log in first.")
        st.write("[Click here to login](http://localhost:8501/Login)") 
   
    
if __name__=="__main__":
    main()