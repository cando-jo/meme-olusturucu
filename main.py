# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form sonuçları 
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        ust_metin = request.form['textTop']
        alt_metin = request.form['textBottom']
        # Görev #3. Metnin konumunu almak
        ust_metin_y = request.form['textTop_y']
        alt_metin_y = request.form['textBottom_y']

        # Görev #3. Metnin rengini almak
        metin_rengi = request.form.get('color-selector')

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                                ust_metin=ust_metin,
                                alt_metin=alt_metin,
                               # Görev #3. Rengi görüntüleme
                               metin_rengi=metin_rengi,
                               
                               # Görev #3. Metnin konumunu görüntüleme
                                alt_metin_y=alt_metin_y,
                                ust_metin_y=ust_metin_y,
                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True, port=2222)
