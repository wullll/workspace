#!/usr/lib/python
# coding=utf-8

from flask import Flask, request, session, jsonify

USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
app.secret_key = 'pithy'


# 登录接口定义
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # post方法
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = "Invalid username"
        elif request.form['password'] != PASSWORD:
            error = "Invalid password"
        else:
            session['logged_in'] = True
            return jsonify({'code': 200, 'msg': 'success'})
    return jsonify({'code': 401, 'msg': error}), 401


@app.route('/info', methods=['GET'])
def info():
    if not session.get('logged_in'):
        return jsonify({'code': 401, 'msg': 'Please login !!'})
    return jsonify({'code': 200, 'msg': 'success', 'data': 'info'})


if __name__ == "__main__":
    app.run(debug=True)
