from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('body.html', name='sample')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)