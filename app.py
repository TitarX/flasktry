from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def front():  # put application's code here
    return render_template('front.html')


@app.route('/user/<name>/')
def user(name):
    user = {
        'name': name
    }
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
