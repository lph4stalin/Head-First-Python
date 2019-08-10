from flask import Flask, render_template, request, escape, session
from vsearch import search4letters
from DBcm import  UseDatabase
from checker import check_logged_in
import mysql.connector
from threading import Thread
import time


app = Flask(__name__)

# 将连接属性字典增加到 Web 应用的配置中
app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB',
    }

app.secret_key = 'YouWillNeverGuess'

# 这里修饰器的作用是：当访问路径是 '/' 的时候，返回 hello 函数
# route 方法已经具有作为服务器的功能：输入 path，返回给定的内容，并自动用 http 协议包装
# @app.route('/')
# def hello():
#     return redirect('/entry')
@app.route('/search4', methods=['GET', 'POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging failed with this error:', str(err))
    return render_template('results.html', the_title=title, the_results=results, the_phrase=phrase, the_letters=letters,)


# 对 entry_page 绑定两个地址
@app.route('/')
# flask 默认模板 html 是放在当前文件同一级目录的 templates 文件夹里面的，层级和文件夹名称一定不能错
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log():
    contents = []
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            # 执行 SQL 语句
            cursor.execute(_SQL)
            # 获取执行内容
            contents = cursor.fetchall()
    except mysql.connector.errors.InterfaceError as err:
        print('Is your database switched on? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents,)


def log_request(req, res):
    """Log details of the web request and the results."""
    time.sleep(15)
    # 连接数据库
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log 
          (phrase, letters, ip, browser_string, results) 
          values 
          (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out.'


if __name__ == '__main__':
    # app.run(port) 可以指定一个端口，默认端口是 5000
    app.run(debug=True)
