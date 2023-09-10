#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'


@app.route('/count/<int:parameter>')
def count(parameter):
    return ''.join([f'{str(i)}\n' for i in range(parameter)])


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        if num1 == 0 and num2 == 0:
            return '0'
        return f'{num1 / num2}' if num2 != 0 else f'{num2 / num1}'
    elif operation == '%':
        if num1 == 0 and num2 == 0:
            return '0'
        return f'{num1 % num2}' if num2 != 0 else f'{num2 % num1}'
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
