import streamlit as st
import time

# Pengaturan halaman
st.set_page_config(page_title="Pesan Cinta Untukmu 💖", page_icon="💌", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Mengubah warna background seluruh halaman */
    .stApp {
        background-color: #FCE4EC; /* Soft pink */
    }

    /* Judul dan teks pendukung */
    .title-text {
        text-align: center;
        color: #D81B60; /* Darker pink */
        font-family: 'Comic Sans MS', cursive; /* Gaya font yang playful */
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    .subtitle-text {
        text-align: center;
        color: #AD1457; /* Slightly darker subtitle */
        font-family: 'Arial', sans-serif;
        font-size: 1.1em;
        margin-bottom: 30px;
    }

    /* Styling container pesawat kertas */
    .paper-plane-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin-top: 50px;
        position: relative; /* Untuk posisi jalur */
    }

    /* Gambar pesawat kertas sebagai tombol */
    .stButton>button {
        background: none;
        border: none;
        cursor: pointer;
        padding: 0;
        transition: transform 0.6s ease-in-out; /* Animasi lebih panjang */
        outline: none; /* Hilangkan outline saat focus */
        display: block; /* Agar gambar bisa di tengah */
        margin: 0 auto;
    }

    .stButton>button img {
        width: 150px; /* Ukuran pesawat */
        height: auto;
        display: block;
    }

    /* Animasi hover untuk pesawat */
    .stButton>button:hover {
        transform: scale(1.3) translateY(-30px) rotate(-15deg); /* Lebih dramatis */
    }
    
    /* Jalur putus-putus saat pesawat "terbang" */
    .dotted-path {
        width: 200px;
        height: 100px;
        background-image: url("https://i.imgur.com/uN8zE9A.png"); /* Placeholder dotted line image */
        background-size: contain;
        background-repeat: no-repeat;
        position: absolute;
        top: 0px; /* Sesuaikan posisi relatif terhadap container */
        left: 50%;
        transform: translateX(-50%);
        animation: pathDraw 2s forwards ease-out;
        opacity: 0;
    }

    @keyframes pathDraw {
        from { opacity: 0; transform: translateX(-50%) scaleX(0); }
        to { opacity: 1; transform: translateX(-50%) scaleX(1); }
    }


    /* Styling kotak surat */
    .letter-box {
        background-color: white;
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.15); /* Bayangan lebih halus */
        border-left: 10px solid #FF69B4; /* Hot pink */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333;
        line-height: 1.8;
        margin-top: 40px;
        animation: fadeInLetter 1.8s ease-out; /* Animasi muncul surat */
        position: relative;
        z-index: 10;
    }

    @keyframes fadeInLetter {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .letter-box h3 {
        color: #D81B60;
        font-family: 'Comic Sans MS', cursive;
        margin-bottom: 15px;
    }
    .letter-box p {
        margin-bottom: 10px;
    }
    .signature {
        text-align: right;
        font-weight: bold;
        font-size: 1.3em;
        color: #FF69B4;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALISASI STATE ---
if 'surat_terbuka' not in st.session_state:
    st.session_state.surat_terbuka = False
if 'plane_clicked' not in st.session_state:
    st.session_state.plane_clicked = False

def open_letter_and_animate():
    st.session_state.plane_clicked = True
    time.sleep(1.5) # Beri waktu untuk animasi jalur
    st.session_state.surat_terbuka = True

# --- TAMPILAN UTAMA ---

if not st.session_state.surat_terbuka:
    st.markdown("<h1 class='title-text'>Pesan Cinta Untukmu 💖</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subtitle-text'>Ada pesan spesial untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle-text'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    # Placeholder untuk jalur putus-putus
    if st.session_state.plane_clicked:
        st.markdown("<div class='dotted-path'></div>", unsafe_allow_html=True)

    # Container untuk menengahkan gambar pesawat sebagai tombol
    with st.container():
        col1, col2, col3 = st.columns([1, 0.5, 1]) # Kolom tengah lebih kecil untuk tombol
        with col2:
            if st.button("plane_button"): # ID unik untuk tombol
                open_letter_and_animate()
                st.rerun() # Refresh halaman untuk menampilkan surat
            # Trik untuk menampilkan gambar di dalam tombol Streamlit
            st.markdown(f"""
                <style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-nahz7x.ea3g5ff10 > div.block-container.st-emotion-cache-1y4qf8z.ea3g5ff2 > div:nth-child(1) > div > div.st-emotion-cache-q8sso8.e1f1d6gn3 > div > div > button.st-emotion-cache-d09v9u.ef3psqc10 > div > p 
                {{ 
                    display: none; /* Sembunyikan teks default tombol */
                }}
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-nahz7x.ea3g5ff10 > div.block-container.st-emotion-cache-1y4qf8z.ea3g5ff2 > div:nth-child(1) > div > div.st-emotion-cache-q8sso8.e1f1d6gn3 > div > div > button.st-emotion-cache-d09v9u.ef3psqc10 
                {{
                    background-image: url("https://i.imgur.com/2i767Qy.png"); /* Link gambar pesawat kertas PNG transparan */
                    background-size: 150px; /* Ukuran gambar di dalam tombol */
                    background-repeat: no-repeat;
                    background-position: center;
                    width: 150px; /* Pastikan tombol cukup besar untuk gambar */
                    height: 150px;
                }}
                </style>
                """, unsafe_allow_html=True)

else:
    # --- Tampilan setelah pesawat diklik: Surat muncul dengan balon hati ---
    st.balloons() # Efek balon bawaan Streamlit
    
    st.markdown("<h1 class='title-text'>Happy Valentine's Day Sayang!! 💖</h1>", unsafe_allow_html=True)
    
    # Efek balon hati di sudut-sudut (menggunakan CSS untuk posisi)
    st.markdown("""
        <style>
        .heart-balloon-top-left {
            position: fixed;
            top: 20px;
            left: 20px;
            font-size: 60px;
            animation: floatHearts 5s infinite ease-in-out;
            z-index: 5;
        }
        .heart-balloon-bottom-right {
            position: fixed;
            bottom: 20px;
            right: 20px;
            font-size: 60px;
            animation: floatHearts 5s infinite ease-in-out reverse;
            z-index: 5;
        }
        @keyframes floatHearts {
            0% { transform: translateY(0); }
            50% { transform: translateY(-
