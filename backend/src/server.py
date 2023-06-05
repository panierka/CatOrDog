from flask import Flask, request, Response
from logger import log
from clsengine import classify

app = Flask(__name__)


@app.get('/api/test')
def test():
    return {
        'message': 'test'
    }


@app.post('/api/classify')
def classify_image():
    image = request.files.get('image')
    log.info('received image "{}" for classification.'.format(image.filename))
    cls = classify(image)
    log.info('image "{}" was classified as "{}"'.format(image.filename, cls))
    return {
        'class': cls
    }


if __name__ == '__main__':
    log.info('starting the server...')
    app.run()
