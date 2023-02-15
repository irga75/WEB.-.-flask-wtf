from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, RadioField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    surname = StringField('Введите фамилию', validators=[DataRequired()])
    name = StringField('Введите имя', validators=[DataRequired()])
    email = StringField('Введите адрес почты', validators=[DataRequired()])
    education = SelectField('Какое у вас образование', choices=['Начальное', 'Среднее', 'Высшее'])
    prof = SelectMultipleField('Какие у Вас есть профессии?',
                               choices=['инженер-исследователь', 'пилот',
                                        'строитель', 'экзобиолог', 'врач',
                                        'инженер по терраформированию', 'климатолог',
                                        'специалист по радиационной защите',
                                        'астрогеолог', 'гляциолог',
                                        'инженер жизнеобеспечения', 'метеоролог',
                                        'оператор марсохода', 'киберинженер', 'штурман',
                                        'пилот дронов'])
    sex = RadioField('Укажите пол', choices=['Мужской', 'Женский'])
    motivation = TextAreaField('Почему вы хотите принять участие в миссии?')
    agree = BooleanField('Готовы остаться на Марсе?')
    submit = SubmitField('Отправить')
