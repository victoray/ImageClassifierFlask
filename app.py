from flask import Flask, render_template, request
from classifier.predict import predict
import wget

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        print(request.form)
        model = request.form['model']
        gpu = True if request.form.get('gpu') else False
        url = request.form['image']
        image_path = download(url)

        print(model, gpu, image_path)

    return render_template('index.html')


def download(url):
    name = url.rsplit('/')
    path = f'images/{name[-1]}'
    wget.download(url, path)
    return path


if __name__ == '__main__':
    app.run(debug=True)
