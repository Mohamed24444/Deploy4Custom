from werkzeug.wrappers import request


import sqlite3
def add(Num1,Num2):
    try:
        Result = Num1 + Num2
        return Result
    except:
        pass

