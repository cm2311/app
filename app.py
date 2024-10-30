from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']

    # Buat gambar dengan PIL
    image = Image.new('RGB', (800, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_position = (10, 10)
    draw.text(text_position, text, fill=(0, 0, 0), font=font)

    # Simpan gambar ke buffer
    buf = io.BytesIO()
    image.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png', as_attachment=True, download_name='generated_image.png')

if __name__ == '__main__':
    app.run(debug=True)
