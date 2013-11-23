#!/usr/bin/python

from flask import Flask, request, render_template, redirect, session, url_for, flash
import utils, json

app = Flask(__name__)
app.secret_key = 'abcd'
app.debug = True

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
        username = get_form_value('username')
        password = get_form_value('password')
        flash(utils.login_user(username, password))
        return redirect(url_for('index'))

@app.route('/register', methods = ['POST'])
def register():
        username = get_form_value('username')
        password = get_form_value('password')
        password2 = get_form_value('password2')
        flash(utils.register_user(username, password, password2))
        return redirect(url_for('index'))

@app.route('/logout', methods = ['POST'])
def logout():
        utils.logout_user()
        return redirect(url_for('index'))

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
