from flask import Flask
from logger import log

app = Flask(__name__)


@app.get('/api/test')
def test():
    return {
        'message': 'test'
    }


if __name__ == '__main__':
    log.info('starting the server...')
    app.run()
