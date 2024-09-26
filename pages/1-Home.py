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

    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write(f"Halo, {st.session_state['username']}!")
        
        st.title("Fighting Breast Cancer Takes Everyone")
        st.write("""
             Breast cancer is one of the most common types of cancer affecting women worldwide.
             Though it may seem frightening, early detection and proper treatment greatly increase
             the chances of recovery and improving quality of life.""")
        st.write("""On this page, we provide a technology-based tool to help classify breast cancer quickly and accurately. 
             By utilizing valid medical data, this tool aids in identifying the type of breast cancer, 
             making it easier for healthcare providers to determine the best course of treatment.""")
        st.subheader("What is Breast Cancer? 🩺")
        st.write("""Breast cancer occurs when cells in the breast tissue start growing uncontrollably. 
             It can form in the ducts (ductal carcinoma) or in the lobules (lobular carcinoma), 
             two key components of the breast.""")
        st.subheader("The Importance of Early Detection ⏳")
        st.write("""Early detection of breast cancer through routine screenings like mammograms can help
            catch the disease at an earlier stage, when treatment is more effective. 
            Educating the public about the early signs of breast cancer is crucial for raising awareness.""")
        st.subheader("Types of Breast Cancer 🧬")
        st.write("""There are various types of breast cancer, including:Invasive Ductal Carcinoma (IDC): 
            Cancer that starts in the milk ducts and spreads to surrounding tissue. Invasive Lobular Carcinoma (ILC):
            A type of cancer that begins in the milk-producing glands and spreads to other areas. Triple-Negative Breast Cancer: 
            ne of the more aggressive forms that is harder to treat because it doesn’t respond to hormone therapy.""")
        st.subheader("How Does This Tool Work? ⚙️")
        st.write("""Our application uses machine learning algorithms to analyze data and classify the type of breast cancer 
             based on patterns identified in the data. This allows for accurate and reliable results 
             in a short amount of time.""")
    else:
        st.warning("You are not logged in. Please log in first.")
        st.write("[Click here to login](/)") 
   
    
if __name__=="__main__":
    main()