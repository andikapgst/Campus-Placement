import pickle
import streamlit as st

# Membaca model
model = pickle.load(open('model.pkl', 'rb'))

# Judul web
st.title('Prediksi Penempatan Kerja')
st.write('')

# Link untuk kembali sebagai tombol
#st.markdown("""
#    <style>
#    .button {
#       display: inline-block;
#       padding: 10px 20px;
#       font-size: 16px;
#       cursor: pointer;
#       text-align: center;
#       background-color: #A1B2B9;
#       border: none;
#       border-radius: 15px;
#       padding: 0.25em 0.75em;
#    }
#    </style>
#    <a href="https://undira.netlify.app/" class="button">Kembali ke halaman utama</a>""", unsafe_allow_html=True)

# Inisialisasi session state
if 'Gender' not in st.session_state:
    st.session_state['Gender'] = ''
if 'Nilai SMP' not in st.session_state:
    st.session_state['Nilai SMP'] = ''
if 'Nilai SMA' not in st.session_state:
    st.session_state['Nilai SMA'] = ''
if 'Nilai Sarjana' not in st.session_state:
    st.session_state['Nilai Sarjana'] = ''
if 'Pengalaman Kerja' not in st.session_state:
    st.session_state['Pengalaman Kerja'] = ''
if 'Nilai Tes Kelayakan' not in st.session_state:
    st.session_state['Nilai Tes Kelayakan'] = ''
if 'Spesialisasi Magang' not in st.session_state:
    st.session_state['Spesialisasi Magang'] = ''
if 'Nilai Magang' not in st.session_state:
    st.session_state['Nilai Magang'] = ''

# Kolom
col1, col2 = st.columns(2)

with col1:
    gender_options = ['Laki-laki', 'Perempuan']
    Gender = st.radio('Gender', gender_options)
    gender_numeric = 1 if Gender == 'Laki-laki' else 2
    NilaiSMP = st.text_input('Input Nilai SMP', key='Nilai SMP')
    NilaiSMA = st.text_input('Input Nilai SMA', key='Nilai SMA')
    NilaiSarjana = st.text_input('Input Nilai Sarjana', key='Nilai Sarjana')

with col2:
    workex_options = ['Tidak', 'Ya']
    PengalamanKerja = st.radio('Pengalaman Kerja', workex_options)
    pengalamankerja_numeric = 1 if PengalamanKerja == 'Tidak' else 2
    NilaiTesKelayakan = st.text_input('Input Nilai Tes Kelayakan', key='Nilai Tes Kelayakan')
    spesialisasi_options = ['Pilih Spesialiasi', 'Pengabdian Masyarakat', 'Industri Bisnis']
    SpesialisasiMagang = st.selectbox('Spesialisasi Magang', spesialisasi_options)
    spesialisasi_numeric = 1 if SpesialisasiMagang == 'Pengabdian Masyarakat' else 2 if SpesialisasiMagang == 'Industri Bisnis' else 0
    NilaiMagang = st.text_input('Input Nilai Magang', key='Nilai Magang')

# Button Prediksi
if st.button('Prediksi'):
    # Validasi input
    try:
        df_input = [gender_numeric, float(NilaiSMP), float(NilaiSMA), float(NilaiSarjana), pengalamankerja_numeric, 
                  float(NilaiTesKelayakan), spesialisasi_numeric, float(NilaiMagang)]
        
        if all(df_input):
            prediction = model.predict([df_input])
            if prediction[0] == 1:
                st.success('Selamat, Anda berpeluang untuk mendapatkan penempatan kerja.')
            else:
                st.warning('Maaf, Anda belum berpeluang untuk mendapatkan penempatan kerja. Tetap semangat!')
        else:
            st.error('Silakan isi semua nilai sebelum melakukan prediksi.')
    except ValueError as e:
        st.error(f'Ada kesalahan dalam input: {e}')
