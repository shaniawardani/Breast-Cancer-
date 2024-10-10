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
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }

        /* Styling for header title */
        .header-title {
            font-size: 48px;
            font-weight: bold;
            color: #000000;
        }
        </style>
        
        <!-- Adding an image in the header -->
        <img src='https://github.com/shaniawardani/Breast-Cancer-/blob/main/asset/aboutus.png?raw=true' class='header-image'/>
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
            """, 
            unsafe_allow_html=True
        )

def main():
    set_page_config()
    inject_custom_css()
    render_sidebar()
    
    # Main content area
    st.markdown("<h1 class='header-title'>About Us 🌐</h1>", unsafe_allow_html=True)
    st.write("""
        Welcome to Breast Cancer Analysis, a website dedicated to empowering patients, healthcare professionals, 
        and researchers with advanced tools for understanding and diagnosing breast cancer. Our platform leverages 
        cutting-edge machine learning technology to analyze medical data, providing accurate and efficient breast 
        cancer classification to aid in early detection and personalized treatment plans.
    """)
    
    st.subheader("Vision 👁️")
    st.write("""
        To integrate AI and healthcare, making breast cancer diagnosis faster and more precise, 
        ultimately improving patient outcomes worldwide.
    """)
    
    st.subheader("Mission 🎗️")
    st.write("""
        To leverage technology for early breast cancer diagnosis and personalized treatment, 
        empowering healthcare providers with accurate, data-driven insights.
    """)
    
    # Creating two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <h1 style="font-size: 30px; color: #AF0B56;">Column 1 Title</h1>
            <p>This is content for the first column. You can add more details or content here.</p>
            """, 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <h1 style="font-size: 30px; color: #AF0B56;">Column 2 Title</h1>
            <p>This is content for the second column. You can place different information or widgets here.</p>
            """, 
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
