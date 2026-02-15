import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Pesan Untukmu", page_icon="✈️", layout="centered")

# Custom CSS untuk tampilan estetik dan animasi pesawat
st.markdown("""
    <style>
    /* Mengubah warna background seluruh halaman */
    .stApp {
        background-color: #FCE4EC;
    }
    
    /* Animasi tombol pesawat terbang */
    .stButton>button {
        background: none;
        border: none;
        font-size: 100px;
        transition: transform 0.5s ease-in-out;
        cursor: pointer;
        padding: 0;
        margin-top: 50px;
    }
    
    .stButton>button:hover {
        transform: scale(1.2) translateY(-20px) rotate(10deg);
        background: none;
        border: none;
    }

    /* Styling kotak surat */
    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 8px solid #F06292;
        font-family: 'Comic Sans MS', cursive;
        color: #444;
        line-height: 1.6;
        margin-top: 20px;
        animation: fadeIn 1.5s;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .title-text {
        text-align: center;
        color: #D81B60;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """, unsafe_allow_html=True)

# Inisialisasi state untuk membuka surat
if 'surat_terbuka' not in st.session_state:
    st.session_state.surat_terbuka = False

# --- TAMPILAN UTAMA ---

if not st.session_state.surat_terbuka:
    # Tampilan awal: Hanya pesawat terbang
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada pesan spesial untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #AD1457;'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("✈️"):
            st.session_state.surat_terbuka = True
            st.rerun()

else:
    # Tampilan setelah pesawat diklik: Surat muncul
    st.balloons() # Efek balon merayakan surat terbuka
    
    st.markdown("<h1 class='title-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    # Isi Surat
    st.markdown("""
    <div class="letter-box">
        <h3 style="color: #D81B60;">Haloo my handsome, my love, my world! 🪐✨🤍</h3>
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
        <p style="text-align: right; font-weight: bold; font-size: 1.2em;">- Sayangmu ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol untuk kembali (opsional)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Tutup Pesan 📩"):
        st.session_state.surat_terbuka = False
        st.rerun()
