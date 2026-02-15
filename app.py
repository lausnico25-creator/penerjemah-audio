import streamlit as st
import os

# 1. SETTING HALAMAN
st.set_page_config(page_title="Pesan Untukmu 💌", page_icon="💖", layout="centered")

# 2. CUSTOM CSS (Tombol Transparan & Teks Hitam)
st.markdown("""
    <style>
    .stApp { background-color: #FCE4EC; }
    
    /* Membuat teks hitam pekat agar jelas */
    h1, h2, h3, p, span, div { 
        color: #000000 !important; 
        font-family: 'Comic Sans MS', cursive; 
    }
    
    /* TRIK TOMBOL TRANSPARAN DI ATAS GAMBAR */
    div.stButton > button {
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        width: 100%;
        height: 250px; /* Menyesuaikan tinggi gambar pesawat */
        position: absolute;
        top: -260px; /* Menggeser tombol tepat ke atas gambar */
        z-index: 999;
        cursor: pointer;
    }
    
    div.stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.1) !important;
    }

    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 8px solid #F06292;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGIKA HALAMAN
if 'terbuka' not in st.session_state:
    st.session_state.terbuka = False

# --- TAMPILAN 1: PESAWAT (Klik Gambar untuk Buka) ---
if not st.session_state.terbuka:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Klik pada pesawat untuk membukanya ✨</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    with col2:
        if os.path.exists("pesawat.png"):
            st.image("pesawat.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center; font-size:100px;'>✈️</h1>", unsafe_allow_html=True)

        # Tombol ini sekarang transparan dan menutupi area gambar
        if st.button("BUKA"):
            st.session_state.terbuka = True
            st.rerun()

# --- TAMPILAN 2: SURAT & YOUTUBE MUSIC ---
else:
    # YouTube Music Embed (Pilihanku - Maliq & D'Essentials)
    st.markdown("""
        <iframe width="100%" height="180" src="https://www.youtube.com/embed/Q1-pK_UelkA?autoplay=1" 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen></iframe>
        <p style='text-align:center; font-size: 12px;'>Klik tombol Play di atas jika lagu tidak otomatis berputar 🎵</p>
    """, unsafe_allow_html=True)
    
    st.balloons()
    
    st.markdown("<h1 style='text-align:center;'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="letter-box">
        <h3 style="margin-top:0;">Haloo my handsome, my love, my world! 🪐✨🤍</h3>
        <p>
            Di hari yang penuh cinta ini, aku mau bilang aku sangat amat bersyukur 
            bisa terus bersama kamu. Terima kasih banyak untuk semua yang kita lewatin bareng.
        </p>
        <p>
            Tahun ini jadi tahun pertama kita ngerayain valentine, semoga di tahun-tahun 
            berikutnya kita tetap bisa ngerayain valentine terus yaaa.
        </p>
        <p>
            Aku harap cinta kita selalu bertumbuh setiap harinya, dan rasa sayang ini 
            nggak akan pernah habis...
        </p>
        <p style="text-align: right; font-weight: bold; font-size: 1.2em;">- Sayangmu ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Tutup Pesan 📩", key="tutup"):
        st.session_state.terbuka = False
        st.rerun()
