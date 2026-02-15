import streamlit as st
import os

# 1. SETTING HALAMAN
st.set_page_config(page_title="Pesan Untukmu 💌", page_icon="💖", layout="centered")

# 2. CUSTOM CSS (Teks Hitam & Perbaikan Visual)
st.markdown("""
    <style>
    .stApp {
        background-color: #FCE4EC;
    }
    
    /* Mengubah semua teks utama menjadi hitam agar jelas */
    .title-text {
        text-align: center;
        color: #000000 !important; /* Hitam Pekat */
        font-family: 'Comic Sans MS', cursive;
        font-weight: bold;
    }

    p, span, label {
        color: #000000 !important; /* Hitam Pekat */
    }

    /* Tombol transparan agar gambar bisa diklik */
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
    }

    /* Kotak Surat dengan Teks Hitam */
    .letter-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 8px solid #F06292;
        font-family: 'Comic Sans MS', cursive;
        color: #000000 !important; /* Teks dalam surat jadi hitam */
        line-height: 1.6;
        animation: fadeIn 1.2s;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGIKA HALAMAN
if 'terbuka' not in st.session_state:
    st.session_state.terbuka = False

# --- BAGIAN 1: TAMPILAN PESAWAT ---
if not st.session_state.terbuka:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    with col2:
        if os.path.exists("pesawat.png"):
            st.image("pesawat.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align:center; font-size:100px;'>✈️</h1>", unsafe_allow_html=True)

        if st.button("TERBANGKAN PESAN ✨", use_container_width=True):
            st.session_state.terbuka = True
            st.rerun()

# --- BAGIAN 2: TAMPILAN SURAT & LAGU ---
else:
    # LAGU: Maliq & D'Essentials - Pilihanku
    # Menggunakan Embed Player yang lebih kompatibel dengan browser mobile
    st.markdown("""
        <iframe style="border-radius:12px" 
        src="https://open.spotify.com/embed/track/6XybtFpQ8pW2593fW8Hclp?utm_source=generator&autoplay=1" 
        width="100%" height="80" frameBorder="0" allowfullscreen="" 
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy">
        </iframe>
        <p style='text-align:center; font-size: 12px; color: black;'>NB: Jika lagu tidak berbunyi otomatis, klik tombol Play pada pemutar di atas.</p>
    """, unsafe_allow_html=True)
    
    st.balloons()
    
    st.markdown("<h1 class='title-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    # Isi Surat (Semua Teks Hitam)
    st.markdown("""
    <div class="letter-box">
        <h3 style="color: #000000; margin-top:0;">Haloo my handsome, my love, my world! 🪐✨🤍</h3>
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
    
    if st.button("Tutup Pesan 📩"):
        st.session_state.terbuka = False
        st.rerun()
