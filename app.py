from flask import Flask, render_template, session, redirect, url_for, request, flash
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '40cb6d98fe04b2a41e2959c453d422ae'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def front():  # put application's code here
    return render_template('front.html', current_time=datetime.utcnow())


@app.route('/user/', methods=['GET', 'POST'])
def user():
    form = NameForm()

    name = session.get('user_name')
    if name is None:
        name = ''

    if request.method == 'POST':
        name = request.form.get('name')
        name = name.strip()

        if name:
            flash('Имя задано')
            session['user_name'] = name
            return redirect('/user/%s/' % name)
        else:
            flash('Имя не задано')

    form.name.data = name

    return render_template('user_form.html', form=form, name=name)


@app.route('/user/<name>/')
def user_name(name):
    user = {
        'name': name
    }
    return render_template('user_name.html', user=user)


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
