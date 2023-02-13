from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
