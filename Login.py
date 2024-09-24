import streamlit as st

def set_page_config():
    """Set the initial page configuration."""
    st.set_page_config(
        page_icon="",
        page_title="Breast Cancer Analysis",
        layout="wide",
        initial_sidebar_state="expanded",
    )

# Fungsi untuk memeriksa autentikasi pengguna
def authenticate(username, password):
    # Database pengguna sederhana (contoh)
    valid_users = {
        "shania": "12345678",
        "test": "test123",
    }
    
    # Cek apakah username dan password cocok
    if username in valid_users and valid_users[username] == password:
        return True
    else:
        return False

# Fungsi untuk form login
def login_form():
    st.title("Login")

    # Input untuk username dan password
    username = st.text_input("Masukkan Username")
    password = st.text_input("Masukkan Password", type="password")

    # Tombol login
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state['logged_in'] = True  # Simpan status login
            st.session_state['username'] = username  # Simpan username
            st.success("Login berhasil!")
        else:
            st.error("Username atau Password salah!")

# Fungsi utama untuk aplikasi
def main():
    # Cek apakah pengguna sudah login
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Jika sudah login, redirect ke halaman Home.py
    if st.session_state['logged_in']:
        st.write ("[Login Berhasil](./pages/1-Home.py)")  # Pengaturan untuk alihkan ke halaman Home
    else:
        login_form()  # Tampilkan form login jika belum login

if __name__ == '__main__':
    main()