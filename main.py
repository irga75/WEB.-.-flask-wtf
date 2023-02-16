import json

from flask import Flask, render_template, redirect

from emergency_access import AccessForm
from loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index<title>')
def main_page(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def prof_practice(prof):
    return render_template('prof.html', prof=prof)


@app.route('/list_prof/<list>')
def return_list_prof(list):
    prof_list = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                 'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template("prof_list.html", list_type=list, prof_list=prof_list)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def select_astronauts():
    form = LoginForm()
    if form.validate_on_submit():
        with open('data.json', mode='w', encoding='utf-8') as f:
            json.dump(form.data, f)
        return redirect('/auto_answer')
    return render_template('selector.html', title='Анкета', form=form)


@app.route('/auto_answer')
@app.route('/answer')
def return_select_answer():
    with open('data.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)
        data.pop('csrf_token')
        data.pop('submit')
        data['prof'] = ', '.join(data['prof'])
    return render_template("auto_answer.html", title="Анкета", data=data)


@app.route('/login', methods=['GET', 'POST'])
def return_login_page():
    form = AccessForm()
    if form.validate_on_submit():
        return redirect('/login_succeed')
    return render_template('emergency_access.html', title='Аварийный доступ', form=form)


@app.route('/login_succeed')
def return_login_succeed():
    return render_template('login_succeed.html', title='Секретные данные')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
