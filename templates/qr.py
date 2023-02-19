import io
import qrcode
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/qr_code')
def generate_qr_code():
    url = request.args.get('url')
    if url:
        # Generate the QR code image
        img = qrcode.make(url)

        # Convert image to a byte stream
        img_buffer = io.BytesIO()
        img.save(img_buffer)
        img_buffer.seek(0)

        # Return the image as the API response
        return send_file(img_buffer, mimetype='image/png')
    else:
        return "Please provide a URL to generate QR code image.", 400

if __name__ == '__main__':
    app.run()
