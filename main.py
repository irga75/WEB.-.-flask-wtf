from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index<title>')
def main_page(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def prof_practice(prof):
    return render_template('prof.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
