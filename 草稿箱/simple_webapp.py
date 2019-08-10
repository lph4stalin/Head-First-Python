from flask import Flask, session
from checker import check_logged_in


app = Flask(__name__)


@app.route('/page1')
@check_logged_in
def page1():
    return 'This is page 1.'


@app.route('/page2')
@check_logged_in
def page2():
    return 'This is page 2.'


@app.route('/page3')
@check_logged_in
def page3():
    return 'This is page 3.'


@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in.'


app.secret_key = 'YouWillNeverGuess'


@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out.'



@app.route('/status')
def check_status():
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'


if __name__ == '__main__':
    app.run(debug=True)
