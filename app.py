from flask import Flask, render_template, redirect, url_for
from bingo import make_bingo, make_number

app = Flask(__name__, template_folder='templates')

selected_number = set(i for i in range(1, 101))
unselected_number = set()

@app.route('/')
def index():
    global selected_number, unselected_number
    ind_to_num, num_to_ind = make_bingo()
    # new_number = make_number(selected_number, unselected_number)
    context = {
        "your_card": ind_to_num,
    }
    return render_template('body.html', name='ビンゴ', context=context)

@app.route('/reset')
def reset():
    global selected_number, unselected_number
    selected_number = set(i for i in range(1, 101))
    unselected_number = set()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
