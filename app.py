from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Проверка</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Привет, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
