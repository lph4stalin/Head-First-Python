from flask import Flask, session


app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'


# user 是个变量，由网页传进来
@app.route('/setuser/<user>')
def setuser(user):
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser():
    return 'User value is currently set to: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
