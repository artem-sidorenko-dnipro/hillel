from flask import Flask
app = Flask(__name__)
print('test')
@app.route('/')


def hello_world():
    return 'Hello, World!'


def test():
    pass