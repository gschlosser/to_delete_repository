from functools import wraps
from flask import request
from pprint import pprint

def logger(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        pprint(request.json)
        return func(*args, **kwargs)
    return new_func