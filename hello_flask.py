from flask import Flask, render_template, request, escape
from vsearch import search4letters


app = Flask(__name__)

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
    log_request(request, results)
    return render_template('results.html', the_title=title, the_results=results, the_phrase=phrase, the_letters=letters,)


# 对 entry_page 绑定两个地址
@app.route('/')
# flask 默认模板 html 是放在当前文件同一级目录的 templates 文件夹里面的，层级和文件夹名称一定不能错
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log():
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            content = []
            for item in line.split('|'):
                item = escape(item)
                content.append(item)
            contents.append(content)
    titles = ('From Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents,)


def log_request(req, res):
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


if __name__ == '__main__':
    # app.run(port) 可以指定一个端口，默认端口是 5000
    app.run(debug=True)
