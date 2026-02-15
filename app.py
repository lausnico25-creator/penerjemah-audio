import streamlit as st
import os

# 1. SETTING HALAMAN
st.set_page_config(page_title="Pesan Untukmu 💌", page_icon="💖", layout="centered")

# 2. CSS UNTUK TEKS HITAM DAN TAMPILAN
st.markdown("""
    <style>
    .stApp { background-color: #FCE4EC; }
    
    /* Memastikan semua teks berwarna hitam pekat */
    h1, h2, h3, p, div { color: #000000 !important; font-family: 'Comic Sans MS', cursive; }
    
    .letter-box {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border-left: 10px solid #F06292;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    
    /* Gaya tombol transparan untuk gambar pesawat */
    .image-button {
        background: none;
        border: none;
        padding: 0;
        cursor: pointer;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGIKA HALAMAN
if 'status' not in st.session_state:
    st.session_state.status = 'awal'

# --- TAMPILAN 1: PESAWAT SEBAGAI TOMBOL ---
if st.session_state.status == 'awal':
    st.markdown("<br><br><h2 style='text-align:center;'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Tap pesawat di bawah untuk terbang ke suratnya ✨</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    with col2:
        # Menampilkan gambar pesawat
        if os.path.exists("pesawat.png"):
            st.image("pesawat.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center; font-size:100px;'>✈️</h1>", unsafe_allow_html=True)
            
        # TOMBOL MENUJU SURAT (Letakkan tepat di bawah gambar)
        if st.button("BUKA SURAT SEKARANG ✈️", use_container_width=True):
            st.session_state.status = 'surat'
            st.rerun()

# --- TAMPILAN 2: SURAT & MUSIK ---
else:
    # MUSIK: Menggunakan audio player standar agar user bisa "Play" jika autoplay gagal
    st.write("🎵 Musik: Maliq & D'Essentials - Pilihanku")
    st.audio("https://raw.githubusercontent.com/arifianadit/temp-files/main/pilihanku.mp3", format="audio/mp3", autoplay=True)
    
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
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Mulai Lagi? 🔄"):
        st.session_state.status = 'awal'
        st.rerun()
