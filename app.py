import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import sqlite3
import io
import re
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Tutor Korea-Indo AI", page_icon="🇰🇷", layout="wide")

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('database_korea.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, session_id INTEGER, role TEXT, content TEXT)''')
    conn.commit()
    return conn

conn = init_db()

# --- KONFIGURASI API ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("API Key belum disetting di Secrets! Pastikan GEMINI_API_KEY sudah benar.")
    st.stop()

model = genai.GenerativeModel("gemini-1.5-flash")

# --- FUNGSI PENDUKUNG ---
def play_audio(text):
    """Mengubah teks menjadi audio MP3."""
    try:
        tts = gTTS(text=text, lang='ko')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp
    except Exception:
        return None

def extract_hangeul(text):
    """Mengambil karakter Hangeul saja dari sebuah teks."""
    # Regex untuk mendeteksi karakter Hangeul
    hangeul_pattern = re.compile(r'[\uac00-\ud7af]+')
    matches = hangeul_pattern.findall(text)
    return " ".join(matches) if matches else text

# --- SIDEBAR: RIWAYAT CHAT ---
with st.sidebar:
    st.title("🇰🇷 Riwayat Belajar")
    
    if st.button("+ Chat Baru", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        c = conn.cursor()
        c.execute("INSERT INTO sessions (title, created_at) VALUES (?, ?)", ("Percakapan Baru", now))
        conn.commit()
        st.session_state.current_session_id = c.lastrowid
        st.rerun()

    st.write("---")
    c = conn.cursor()
    c.execute("SELECT id, title FROM sessions ORDER BY id DESC")
    sessions = c.fetchall()
    
    for s_id, s_title in sessions:
        # Menandai chat yang sedang aktif
        label = f"📖 {s_title}" if "current_session_id" in st.session_state and st.session_state.current_session_id == s_id else f"📄 {s_title}"
        if st.button(label, key=f"s_{s_id}", use_container_width=True):
            st.session_state.current_session_id = s_id
            st.rerun()

# --- LOGIKA SESI AWAL ---
if "current_session_id" not in st.session_state:
    if sessions:
        st.session_state.current_session_id = sessions[0][0]
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        c = conn.cursor()
        c.execute("INSERT INTO sessions (title, created_at) VALUES (?, ?)", ("Percakapan Baru", now))
        conn.commit()
        st.session_state.current_session_id = c.lastrowid

# --- TAMPILAN UTAMA ---
st.title("🎓 Guru Bahasa Korea AI")
st.info("Ketik kalimat dalam Bahasa Indonesia, dan saya akan menerjemahkannya ke Bahasa Korea beserta cara bacanya.")

# Ambil history dari DB
c = conn.cursor()
c.execute("SELECT id, role, content FROM messages WHERE session_id = ? ORDER BY id ASC", (st.session_state.current_session_id,))
current_messages = c.fetchall()

# Menampilkan chat
for m_id, role, content in current_messages:
    with st.chat_message(role):
        st.markdown(content)
        
        # Fitur Audio pada jawaban Assistant
        if role == "assistant":
            # Ambil hanya bagian Hangeul agar suara gTTS akurat
            korean_text = extract_hangeul(content)
            if korean_text:
                if st.button(f"🔊 Dengar Pengucapan", key=f"audio_{m_id}"):
                    audio_fp = play_audio(korean_text)
                    if audio_fp:
                        st.audio(audio_fp, format="audio/mp3")

# --- INPUT USER ---
if prompt := st.chat_input("Tanya guru..."):
    # 1. Tampilkan dan simpan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)
    
    c.execute("INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)", 
              (st.session_state.current_session_id, "user", prompt))
    conn.commit()

    # 2. Respon Assistant
    with st.chat_message("assistant"):
        with st.spinner("Guru sedang berpikir..."):
            try:
                # Instruksi sistem
                instruction = (
                    "Kamu adalah Guru Bahasa Korea yang ramah. Terjemahkan input siswa ke Bahasa Korea. "
                    "Format jawaban: \n1. Teks Hangeul\n2. Cara baca (Romanisasi)\n3. Penjelasan singkat dalam Bahasa Indonesia."
                )
                
                # Memanggil API Gemini
                response = model.generate_content(f"{instruction}\n\nSiswa: {prompt}")
                answer = response.text
                
                # Update Judul otomatis jika masih default
                c.execute("SELECT title FROM sessions WHERE id = ?", (st.session_state.current_session_id,))
                if c.fetchone()[0] == "Percakapan Baru":
                    try:
                        res_title = model.generate_content(f"Berikan judul maksimal 3 kata untuk: {prompt}")
                        new_title = res_title.text.strip()
                        c.execute("UPDATE sessions SET title = ? WHERE id = ?", (new_title, st.session_state.current_session_id))
                    except:
                        pass
                
                # Simpan jawaban ke DB
                c.execute("INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)", 
                          (st.session_state.current_session_id, "assistant", answer))
                conn.commit()
                
                st.markdown(answer)
                st.rerun() # Refresh untuk update sidebar dan tombol audio
                
            except Exception as e:
                st.error(f"Maaf, ada gangguan koneksi: {str(e)}")
