from flask import Flask, render_template, url_for, redirect, request, flash
from config import Config
from project.forms import WalkForm, CreateForm
from project.find_exit import FindExit
choise = []
posI = 0
posJ = 0
m = ''

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/create', methods=["POST", "GET"])
def create():
    global posJ, posI
    posI = 0
    posJ = 0
    FindExit()
    FindExit().counter = 0
    FindExit().table = []
    form = CreateForm()
    if form.validate_on_submit():
        width = form.width.data
        height = form.height.data

        return render_template("create.html", form=form, width=width, height=height, count=0)
    else:
        return render_template("create.html", form=form,)

@app.route('/lab/', methods=["POST", "GET"])
@app.route('/lab/<count>', methods=["POST", "GET"])
def lab(count=0):
    global posJ, posI, choise, m
    form = WalkForm()
    gamer = FindExit()
    if gamer.counter == 0:
        gamer = FindExit(int(request.form['width']), int(request.form['height']))
        gamer.current_pos()
    gamer.counter += 1
    #for i in range(1, int(request.form['width'])*int(request.form['height'])):
     #   choise.append((i, i))
    #form.escape.choices = sorted(choise)
    if form.validate_on_submit():
        direct = form.direct.data
        step = form.step.data
        if direct == 0:
            posI -= step
            if gamer.current_pos(posI, posJ) == 'Fail':
                flash('Вы не можете сюда идти!')
                posI += step
        elif direct == 1:
            posI += step
            if gamer.current_pos(posI, posJ) == 'Fail':
                flash('Вы не можете сюда идти!')
                posI -= step
        elif direct == 2:
            posJ -= step
            if gamer.current_pos(posI, posJ) == 'Fail':
                flash('Вы не можете сюда идти!')
                posJ += step
        else:
            posJ += step
            if gamer.current_pos(posI, posJ) == 'Fail':
                flash('Вы не можете сюда идти!')
                posJ -= step

    gamer.current_pos(posI, posJ)

    if gamer.current_pos(posI, posJ) == 'Congratulation':
        if (gamer.counter-1)%10 == 1:
            m = ''
        elif (gamer.counter-1)%10 in [2,3,4]:
            m = 'а'
        else:
            m = 'ов'
        flash(f'Поздравляю Вы вышли за {gamer.counter-1} шаг{m}!')
    return render_template("lab.html", form=form, table=gamer.table, count=gamer.counter, m=m)

if __name__ == '__main__':
    app.run(debug=True)