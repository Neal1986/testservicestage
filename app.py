# !/usr/bin/python3

from bottle import Bottle, run

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
def main_page():
    return "main page"

if __name__ == '__main__':
    run(app, host='localhost', port=8080)