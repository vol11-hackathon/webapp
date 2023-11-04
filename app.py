from flask import Flask, render_template, redirect, url_for, session 
from bingo import make_bingo, make_number
from datetime import timedelta 

app = Flask(__name__, template_folder='templates')
app._static_folder = 'static'

app.secret_key = 'abcdefg'
app.permanent_session_lifetime = timedelta(minutes=5) 

selected_number = set(i for i in range(1, 101))
unselected_number = set()

@app.route('/')
def index():
    if "selected_number" in session or "unselected_number" in session:
        context = {
            "your_card": session["selected_number"],
        }
        return render_template('body.html', name='BINGO', context=context)
    else:
        ind_to_num, num_to_ind = make_bingo()
        session.permanent = True
        session["selected_number"] = ind_to_num
        session["unselected_number"] = num_to_ind
        context = {
            "your_card": ind_to_num,
        }
    return render_template('body.html', name='BINGO', context=context)

@app.route('/reset')
def reset():
    session.pop('selected_number', None)
    session.pop('unselected_number', None)
    session.clear()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
