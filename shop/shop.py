from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<Html><h1>home page</h1></Html>'

@app.route('/hw')
def hw():
    return 'Hello, world'

@app.route('/api/<argument>')
def api(argument):
    return 'arg: {}'.format(argument)

@app.route('/api/string/<string:argument>', methods=['post'])
def api_string(argument):
    return 'arg: {}'.format(argument)
