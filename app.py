from flask import Flask, render_template, redirect, url_for, session 
from bingo import make_bingo, make_number, count
from datetime import timedelta 

from random import sample

app = Flask(__name__, template_folder='templates')
app._static_folder = 'static'

app.secret_key = 'abcdefg'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def index():
    if "your_num" in session or "num_index" in session:
        context = set_context(session)
    else:
        your_num, num_index = make_bingo()
        session.permanent = True
        init_session(session, your_num, num_index)
        context = set_context(session)
    return render_template('body.html', context=context)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

@app.route('/draw')
def draw():
    number_order = session["number_order"]
    opened = session["opened"]
    new_number, opened = make_number(number_order, opened)
    session["opened"] = opened
    session["result"] = {
        "new_number": new_number,
    }
    print(new_number)
    cnt_to_ind = (
        ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)),
        ((1, 0), (1, 1), (1, 2), (1, 3), (1, 4)),
        ((2, 0), (2, 1), (2, 2), (2, 3), (2, 4)),
        ((3, 0), (3, 1), (3, 2), (3, 3), (3, 4)),
        ((4, 0), (4, 1), (4, 2), (4, 3), (4, 4)),
        ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0)),
        ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1)),
        ((0, 2), (1, 2), (2, 2), (3, 2), (4, 2)),
        ((0, 3), (1, 3), (2, 3), (3, 3), (4, 3)),
        ((0, 4), (1, 4), (2, 4), (3, 4), (4, 4)),
        ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4)),
        ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))
    )
    row, line = count(new_number, session["num_index"], session["check"], cnt_to_ind)
    if row != -1 and line != -1:
        id = F"cell_{5 * row + line}"
        session["open_cell"].append(id)
    new_entry = F"{new_number} " if opened % 10 != 0 else F"{new_number} <br>"
    session["drawed_num"] += new_entry
    return redirect(url_for('index'))

# debug
@app.route('/page')
def page():
    return render_template('a.html')

def set_context(ses):
    context = {
        "your_num": ses["your_num"],
        "num_index": ses["num_index"],
        "opened": ses["opened"],
        "number_order": ses["number_order"],
        "check": ses["check"],
        "result": ses.get('result', None),
        "open_cell": ses["open_cell"],
        "drawed_num": ses["drawed_num"]
    }
    return context

def init_session(ses, your_num, num_index):
    ses["your_num"] = your_num
    ses["num_index"] = num_index
    ses["opened"] = 0
    ses["number_order"] = sample([i for i in range(1, 101)], 100)
    ses["check"] = [0 for _ in range(12)]
    ses["open_cell"] = []
    ses["drawed_num"] = ""

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
