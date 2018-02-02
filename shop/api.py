from shop import app

@app.route('/api/<argument>')
def api(argument):
    return 'arg: {}'.format(argument)

@app.route('/api/string/<string:argument>', methods=['post'])
def api_string(argument):
    return 'arg: {}'.format(argument)
