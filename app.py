# Create a flask app with a button to upload an image, display that image, and use the model to predict the image
#
# Path: app.py

from flask import Flask, render_template, request
from model import predict_image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(os.path.dirname(__file__), 'static', secure_filename(f.filename)))
        img_name = (f.filename)
        with open('static/'+img_name, 'rb') as f:
            img_bytes = f.read()
            class_name = predict_image(img_bytes)
        return render_template('index.html', class_name=class_name, img_name=img_name)

if __name__ == '__main__':
    app.run(host="localhost", port="3000",debug=True, threaded=True)  