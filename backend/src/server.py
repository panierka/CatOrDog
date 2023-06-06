import datetime

from flask import Flask, request, Response
from clsengine import classify
from logger import log

app = Flask(__name__)


@app.get('/api/test')
def test():
    log.info('test')
    return {
        'message': 'test ' + str(datetime.datetime.now())
    }


@app.post('/api/classify')
def classify_image():
    image = request.files.get('image')
    log.info('received image "{}" for classification.'.format(image.filename))
    cls = classify(image.stream)
    log.info('image "{}" was classified as "{}"'.format(image.filename, cls))
    return {
        'class': cls
    }


if __name__ == '__main__':
    log.info('starting the server...')
    app.run()
