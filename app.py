import streamlit as st

# 1. PENGATURAN HALAMAN
st.set_page_config(page_title="Pesan Untukmu 💌", page_icon="💖", layout="centered")

# 2. CUSTOM CSS (Untuk warna pink, font, dan animasi)
st.markdown("""
    <style>
    /* Background pink lembut */
    .stApp {
        background-color: #FCE4EC;
    }
    
    /* Menghilangkan border tombol agar gambar terlihat bersih */
    div.stButton > button {
        background: none;
        border: none;
        padding: 0;
        margin: auto;
        display: block;
        transition: transform 0.4s ease-in-out;
    }
    
    div.stButton > button:hover {
        transform: scale(1.15) rotate(-5deg);
        background: none;
        border: none;
    }

    /* Styling Kotak Surat */
    .letter-box {
        background-color: white;
        padding: 35px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 10px solid #F06292;
        font-family: 'Comic Sans MS', cursive;
        color: #444;
        line-height: 1.7;
        margin-top: 20px;
        animation: slideUp 1s ease-out;
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .title-text {
        text-align: center;
        color: #D81B60;
        font-family: 'Comic Sans MS', cursive;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGIKA HALAMAN (Session State)
if 'status' not in st.session_state:
    st.session_state.status = 'awal'

# --- TAMPILAN 1: PESAWAT KERTAS ---
if st.session_state.status == 'awal':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #AD1457;'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    # Menampilkan Gambar Pesawat sebagai Tombol
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Pastikan file di GitHub kamu namanya 'pesawat.png'
        try:
            st.image("pesawat.png", use_container_width=True)
        except:
            # Jika gambar belum ada, muncul emoji sebagai cadangan
            st.markdown("<h1 style='text-align:center; font-size:100px;'>✈️</h1>", unsafe_allow_html=True)
            
        if st.button("TAP DISINI ✈️"):
            st.session_state.status = 'surat'
            st.rerun()

# --- TAMPILAN 2: SURAT & BALON ---
else:
    # Efek Balon Hati/Warna-warni
    st.balloons()
    
    st.markdown("<h1 class='title-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    # Isi Surat
    st.markdown("""
    <div class="letter-box">
        <h3 style="color: #D81B60; margin-top:0;">Haloo my handsome, my love, my world! 🪐✨🤍</h3>
        <p>
            Di hari yang penuh cinta ini, aku mau bilang aku sangat amat bersyukur 
            bisa terus bersama kamu. Terima kasih banyak untuk semua yang kita lewatin bareng.
        </p>
        <p>
            Tahun ini jadi tahun pertama kita ngerayain valentine, semoga di tahun-tahun 
            berikutnya kita tetap bisa ngerayain valentine terus yaaa.
        </p>
        <p>
            Aku harap cinta kita selalu bertumbuh setiap harinya, dan rasa sayang yang 
            nggak akan pernah habiss setiap harinya...
        </p>
        <p style="text-align: right; font-weight: bold; font-size: 1.2em; color: #D81B60; margin-bottom:0;">
            - Sayangmu ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Tutup Pesan 🔄"):
        st.session_state.status = 'awal'
        st.rerun()
