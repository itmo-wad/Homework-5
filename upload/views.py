from flask import Flask, render_template, request

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/static/img/uploads'
app.config['SECRET_KEY'] = 'donteventhinkaboutit'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            return render_template('success.html')
        else:
            return render_template('failed.html')
    return render_template('form.html')



if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)