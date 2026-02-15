import streamlit as st
import time

# Pengaturan halaman
st.set_page_config(page_title="Happy Valentine!", page_icon="💖", layout="centered")

# Custom CSS untuk background pink dan styling teks
st.markdown("""
    <style>
    .main {
        background-color: #FCE4EC;
    }
    .stButton>button {
        background-color: #f06292;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
    }
    .stButton>button:hover {
        background-color: #ec407a;
        color: white;
    }
    .big-text {
        font-family: 'Comic Sans MS', cursive;
        color: #d81b60;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Inisialisasi state untuk alur cerita
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

# --- ALUR CERITA ---

if st.session_state.step == 0:
    st.markdown("<h1 class='big-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHIybmt6am44eHF3eXl1bmxwaW5mZGN6Znd4eXp5eHF6eHF6eHF6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/vNEXy33u93wV39Hh0K/giphy.gif", use_column_width=True)
    st.write("there's more waiting... click to find out ✨")
    if st.button("tap <3"):
        next_step()
        st.rerun()

elif st.session_state.step == 1:
    st.markdown("<h3 class='big-text'>Terima kasih telah hadir dan selalu mengisi hari-hariku penuh cinta 🥺💖</h3>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd4eXp5eHF6eHF6eHF6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/MDJ9NmJpL19w4/giphy.gif")
    if st.button("open it <3"):
        next_step()
        st.rerun()

elif st.session_state.step == 2:
    st.markdown("<h3 class='big-text'>Remember that everytime I look at you, I fall in love all over again</h3>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd4eXp5eHF6eHF6eHF6ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/KztT2c4u8mYYUiCiS7/giphy.gif")
    if st.button("next..."):
        next_step()
        st.rerun()

elif st.session_state.step == 3:
    st.balloons() # Efek balon saat sampai di pesan utama
    st.markdown("<h2 class='big-text'>I still want u to be my partner forever together 🥺</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Tahun ini jadi tahun pertama kita ngerayain valentine, semoga tahun berikutnya tetap bareng ya!</p>", unsafe_allow_html=True)
    
    # Menampilkan pesan panjang seperti di video
    pesan_cinta = """
    Haloo my handsome, my love, my world! 🪐✨🤍
    Di hari yang penuh cinta ini, aku mau bilang aku sangat amat bersyukur bisa terus bersama kamu. 
    Terima kasih banyak untuk semua yang kita lewatin bareng. 
    Semoga kita selalu bertumbuh setiap harinya dan rasa sayang ini nggak akan pernah habis...
    """
    st.info(pesan_cinta)
    
    if st.button("Mulai Lagi?"):
        st.session_state.step = 0
        st.rerun()
