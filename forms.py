from wtforms import Form, StringField, SubmitField
from wtforms.validators import InputRequired


class NameForm(Form):
    name = StringField('Введите ваше имя:', validators=[InputRequired()])
    submit = SubmitField('Отправить')
