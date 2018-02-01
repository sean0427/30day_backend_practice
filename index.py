from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<Html><h1>home page</h1></Html>'

@app.route('/hw')
def hw():
    return 'Hello, world'
