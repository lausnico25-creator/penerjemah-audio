import streamlit as st
import os

# 1. SETTING HALAMAN
st.set_page_config(page_title="Pesan Untukmu 💌", page_icon="💖", layout="centered")

# 2. CUSTOM CSS
st.markdown("""
    <style>
    .stApp { background-color: #FCE4EC; }
    
    /* Teks Hitam Pekat */
    h1, h2, h3, p, span, div { 
        color: #000000 !important; 
        font-family: 'Comic Sans MS', cursive; 
    }
    
    /* Tombol Transparan Menutupi Gambar Pesawat */
    div.stButton > button {
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        width: 100%;
        height: 280px; 
        position: relative;
        z-index: 10;
        cursor: pointer;
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

# --- TAMPILAN 1: PESAWAT ---
if not st.session_state.terbuka:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Klik pada pesawat untuk membukanya ✨</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.1, 1, 0.1])
    with col2:
        if os.path.exists("pesawat.png"):
            st.image("pesawat.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center; font-size:100px;'>✈️</h1>", unsafe_allow_html=True)

        if st.button("BUKA"):
            st.session_state.terbuka = True
            st.rerun()

# --- TAMPILAN 2: SURAT & MUSIK ---
else:
    # EFEK BALON
    st.balloons()
    
    # MUSIK: Menggunakan st.audio agar browser HP memberikan izin suara
    # Link ini adalah file audio langsung (direct link)
    st.write("🎵 Memutar: Maliq & D'Essentials - Pilihanku")
    st.audio("https://files.catbox.moe/9f9v3k.mp3", format="audio/mp3", autoplay=True)
    
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
    
    st.markdown("<p style='text-align:center; font-size:12px;'>NB: Jika lagu belum berbunyi, tekan tombol play pada kotak musik di atas.</p>", unsafe_allow_html=True)
    
    if st.button("Tutup Pesan 📩", key="tutup"):
        st.session_state.terbuka = False
        st.rerun()
