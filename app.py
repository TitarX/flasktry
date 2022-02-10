from flask import Flask, render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def front():  # put application's code here
    return render_template('front.html', current_time=datetime.utcnow())


@app.route('/user/<name>/')
def user(name):
    user = {
        'name': name
    }
    return render_template('user.html', user=user)


@app.route('/bootstrap/')
def bootstrap_example():
    return render_template('bootstrap_example.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run(debug=True)
