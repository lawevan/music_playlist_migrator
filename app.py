from flask import Flask

from spotify import authorize

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HELLOWORLD'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login')
def login():
    return authorize()


if __name__ == '__main__':
    app.run()
