from mango import app

@app.route('/')
def landing_page():
    return '<h1>naennit..</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
