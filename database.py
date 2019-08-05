from DBcm import UseDatabase


dbconfig = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpasswd',
        'database': 'vsearchlogDB',
    }
# 连接数据库
with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)

