from flask import Flask

app = Flask(__name__)
app.secret_key = "never_tell_you"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def html_hello():
    return "hello from bonfy"

if __name__ == '__main__':
    app.run(port=8888, debug=True)
