from functools import wraps
from flask import session


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper


# check_logged_in（修饰器，page1函数作为参数传入） → 返回 wrapper → page1 → 参数是？（没有参数，在return wrapper 可以传入参数）
# *args 和 **kwargs 是运行 func 需要的参数。它从哪里被传进来？调用被修饰函数的时候
