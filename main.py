from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    gender              = request.form.get('gender')
    nilai_smp           = float(request.form['nilai_smp'])
    nilai_sma           = float(request.form['nilai_sma'])
    nilai_sarjana       = float(request.form['nilai_sarjana'])
    pengalaman_kerja    = request.form.get('pengalaman_kerja')
    nilai_tes_kelayakan = float(request.form['nilai_tes_kelayakan'])
    spesialisasi_magang = request.form.get('spesialisasi_magang')
    nilai_magang        = float(request.form['nilai_magang'])

    if not (gender and nilai_smp and nilai_sma and nilai_sarjana and pengalaman_kerja and nilai_tes_kelayakan and spesialisasi_magang and nilai_magang):
        error_message = 'Data Anda belum lengkap!'
        return render_template('index.html', error_message=error_message)
 
    df_test = pd.DataFrame(data={
        'Gender'             : [gender],
        'Nilai SMP'          : [nilai_smp],
        'Nilai SMA'          : [nilai_sma],
        'Nilai Sarjana'      : [nilai_sarjana],
        'Pengalaman Kerja'   : [pengalaman_kerja],
        'Nilai Tes Kelayakan': [nilai_tes_kelayakan],
        'Spesialisasi Magang': [spesialisasi_magang],
        'Nilai Magang'       : [nilai_magang]
    })
    
    # Lakukan prediksi dengan model
    prediction = model.predict(df_test[0:1])

    # Kembalikan hasil prediksi
    if prediction == 0:
        return render_template('index.html', pred = 'Maaf, Anda belum berpeluang untuk mendapatkan penempatan kerja. Tetap semangat!')
    else:
        return render_template('index.html', pred = 'Selamat, Anda berpeluang untuk mendapatkan penempatan kerja.')

if __name__ == '__main__':

    app.run(host='localhost', port=5000, debug=True)