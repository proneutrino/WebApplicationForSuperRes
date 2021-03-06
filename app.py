import os
import PIL
from flask import Flask, render_template, request
import flask_resize
from PIL import Image
from io import BytesIO



app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    basewidth = 128
    baseheight = 128              
   
    file.save(f)
    img = Image.open(f)
    img = img.resize((basewidth, baseheight), PIL.Image.ANTIALIAS)
    img.save('./uploads/resized_image.jpg')

    return render_template('output.html')

# @app.route('/showOutput', methods=['POST', 'GET'])
# def showOutput():
    
#     if request.method == 'POST':
#         return redirect(url_for('output.html'))

#     if request.method == 'GET':
#         return render_template('output.html')

if __name__ == '__main__':
    app.run(debug=True)