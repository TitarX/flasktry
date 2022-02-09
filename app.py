from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def front():  # put application's code here
    return render_template('front.html')


@app.route('/user/<name>/')
def user(name):
    user = {
        'name': name
    }
    return render_template('user.html', user=user)


@app.route('/bootstrap/')
def bootstrap_example():
    return render_template('bootstrap_example.html')


if __name__ == '__main__':
    app.run(debug=True)
