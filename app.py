import streamlit as st
import os

# 1. SETTING HALAMAN
st.set_page_config(page_title="Pesan Untukmu 💌", page_icon="💖", layout="centered")

# Fungsi untuk memutar musik Maliq & D'Essentials - Pilihanku
def play_pilihanku():
    # Link audio (Menggunakan sumber pihak ketiga yang mendukung pemutaran langsung)
    # Catatan: Jika link ini mati, kamu bisa menggantinya dengan link .mp3 lainnya
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" # Placeholder audio
    
    # Teknik embed audio tersembunyi
    audio_html = f"""
        <iframe src="https://open.spotify.com/embed/track/6Uo7LzOnr86j6yS27U3V6K?utm_source=generator&autoplay=1" 
        width="0" height="0" frameborder="0" allowfullscreen="" 
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
        loading="lazy"></iframe>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
    st.info("🎵 Mendengarkan: Maliq & D'Essentials - Pilihanku")

# 2. CUSTOM CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #FCE4EC;
    }
    
    div.stButton > button {
        background: none;
        border: none;
        padding: 0;
        display: block;
        margin: 0 auto;
        transition: transform 0.3s ease-in-out;
    }
    
    div.stButton > button:hover {
        transform: scale(1.1) rotate(-5deg);
        background: none;
        border: none;
    }

    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 8px solid #F06292;
        font-family: 'Comic Sans MS', cursive;
        color: #444;
        line-height: 1.6;
    }

    .title-text {
        text-align: center;
        color: #D81B60;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGIKA HALAMAN
if 'terbuka' not in st.session_state:
    st.session_state.terbuka = False

# --- BAGIAN 1: TOMBOL PESAWAT ---
if not st.session_state.terbuka:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #AD1457;'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    with col2:
        if os.path.exists("pesawat.png"):
            st.image("pesawat.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center; font-size:100px;'>✈️</h1>", unsafe_allow_html=True)

        if st.button("TERBANGKAN PESAN ✨", use_container_width=True):
            st.session_state.terbuka = True
            st.rerun()

# --- BAGIAN 2: SURAT & LAGU ---
else:
    # Memutar Lagu "Pilihanku" saat surat terbuka
    play_pilihanku()
    
    # Efek Balon Hati
    st.balloons()
    
    st.markdown("<h1 class='title-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="letter-box">
        <h3 style="color: #D81B60;">Haloo my handsome, my love, my world! 🪐✨🤍</h3>
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
            nggak akan pernah habiss...
        </p>
        <p style="text-align: right; font-weight: bold; font-size: 1.2em;">- Sayangmu ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Tutup Pesan 📩"):
        st.session_state.terbuka = False
        st.rerun()
