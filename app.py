import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Pesan Spesial Untukmu", page_icon="💌", layout="centered")

# 2. CSS untuk Desain dan Animasi
st.markdown("""
    <style>
    /* Background Halaman Pink Lembut */
    .stApp {
        background-color: #FCE4EC;
    }

    /* Menghilangkan border default tombol streamlit agar gambar terlihat seperti tombol asli */
    div.stButton > button {
        background: none;
        border: none;
        padding: 0;
        transition: transform 0.3s ease-in-out;
    }
    
    div.stButton > button:hover {
        transform: scale(1.1) rotate(-5deg);
        background: none;
        border: none;
    }

    /* Desain Kotak Surat */
    .letter-box {
        background-color: white;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 10px solid #F06292;
        font-family: 'Comic Sans MS', cursive;
        color: #444;
        line-height: 1.8;
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

# 3. Logika Session State
if 'surat_terbuka' not in st.session_state:
    st.session_state.surat_terbuka = False

# --- TAMPILAN UTAMA ---

if not st.session_state.surat_terbuka:
    # Tampilan Awal: Pesawat Kertas
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #AD1457;'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    # Tombol menggunakan Gambar Pesawat Kertas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Gunakan URL gambar pesawat kertas transparan (PNG)
        if st.button("✈️", key="pesawat_btn", help="Klik untuk membuka"):
            # Kita menggunakan emoji atau gambar lokal. 
            # Jika ingin menggunakan gambar seperti di screenshot kamu:
            # st.image("pesawat_kertas.png")
            st.session_state.surat_terbuka = True
            st.rerun()
    
    # Catatan: Karena kita tidak bisa upload file gambar ke sini, 
    # di atas saya gunakan tombol emoji. Jika kamu punya file 'pesawat.png', 
    # kamu bisa menggantinya dengan st.image di dalam button.

else:
    # Tampilan Setelah Diklik: Balon Hati & Surat
    st.snow() # Menggunakan efek bawaan (seperti salju/balon beterbangan)
    
    # Kamu juga bisa menggunakan st.balloons() untuk balon warna-warni
    st.balloons()
    
    st.markdown("<h1 class='title-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    # Isi Surat Sesuai Gambar Kamu
    st.markdown(f"""
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
            Aku harap cinta kita selalu bertumbuh setiap harinya, dan rasa sayang yang 
            nggak akan pernah habiss setiap harinya...
        </p>
        <p style="text-align: right; font-weight: bold; font-size: 1.2em; color: #D81B60;">
            - Sayangmu ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Mulai Lagi? 🔄"):
        st.session_state.surat_terbuka = False
        st.rerun()
