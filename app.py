from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'japan'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)