# --- TAMPILAN 1: PESAWAT KERTAS ---
if st.session_state.status == 'awal':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 class='title-text'>Ada pesan special untukmu...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #AD1457;'>Klik pesawatnya untuk menerbangkan pesan</p>", unsafe_allow_html=True)
    
    # Membuat wadah kolom agar gambar berada di tengah
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    
    with col2:
        # Menampilkan gambar pesawat asli agar ukurannya besar
        # Jika file di github kamu namanya bukan pesawat.png, sesuaikan di sini
        st.image("pesawat.png", use_container_width=True)
        
        # Tombol transparan yang diletakkan tepat di bawah gambar
        # CSS di atas akan membuat tombol ini terlihat lebih menyatu
        if st.button("TERBANGKAN PESAN ✨", use_container_width=True):
            st.session_state.status = 'surat'
            st.rerun()