from shop import app

@app.route('/')
def hello_world():
    return '<Html><h1>home page</h1></Html>'

@app.route('/hw')
def hw():
    return 'Hello, world'
