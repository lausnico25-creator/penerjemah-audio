import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Pesan Untukmu", page_icon="💌", layout="centered")

# Custom CSS untuk tampilan estetik
st.markdown("""
    <style>
    .main {
        background-color: #FFF0F5;
    }
    .stButton>button {
        background: none;
        border: none;
        font-size: 80px;
        transition: transform 0.3s;
        cursor: pointer;
    }
    .stButton>button:hover {
        transform: scale(1.2) rotate(-10deg);
        background: none;
        border: none;
    }
    .paper-plane-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
    }
    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #FF69B4;
        font-family: 'serif';
        color: #444;
        line-height: 1.6;
    }
    .title-text {
        text-align: center;
        color: #D81B60;
        font-family: 'cursive';
    }
    </style>
    """, unsafe_allow_html=True)

# Inisialisasi state
if 'buka_surat' not in st.session_state:
    st.session_state.buka_surat = False

def open_letter():
    st.session_state.buka_surat = True

# --- TAMPILAN UTAMA ---

if not st.session_state.buka_surat:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada surat untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #888;'>Klik pesawatnya untuk membuka</p>", unsafe_allow_html=True)
    
    # Kolom untuk menengahkan tombol
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("✈️"): # Menggunakan emoji agar aman tidak akan 'Not Available'
            open_letter()
            st.rerun()

else:
    # Efek perayaan saat surat dibuka
    st.balloons()
    
    st.markdown("<h2 class='title-text'>Happy Valentine's Day Sayang!! 💖</h2>", unsafe_allow_html=True)
    
    # Kotak Surat
    st.markdown("""
    <div class="letter-box">
        <h4>Haloo my handsome, my love, my world! 🪐✨</h4>
        <p>
            Di hari yang penuh cinta ini, aku mau bilang aku sangat amat bersyukur 
            bisa terus bersama kamu. Terima kasih banyak untuk semua yang kita lewatin bareng.
        </p>
        <p>
            Tahun ini jadi tahun pertama kita ngerayain valentine, semoga di tahun-tahun 
            berikutnya kita tetap bisa ngerayain bareng terus yaaa.
        </p>
        <p>
            Aku harap cinta kita selalu bertumbuh setiap harinya, dan rasa sayang ini 
            nggak akan pernah habiss...
        </p>
        <p style="text-align: right; font-weight: bold;">- Sayangmu 🤍</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Tutup Surat"):
        st.session_state.buka_surat = False
        st.rerun()
