#!/usr/bin/python

from flask import Flask, request, render_template, redirect, session, url_for, flash
import utils, json
import randomuser 
from pymongo import MongoClient

db = MongoClient().ARSS

app = Flask(__name__)
app.secret_key = 'abcd'
app.debug = True

@app.route("/profile", methods=['GET','POST'])
def profile():
    if request.method=="GET":
	return render_template("template.profile.html",db=db.fakes.find({'user':session.get('username')}))
    else:
	print(session['username'] + "hello")
	utils.addRandUser(session['username']);
	return render_template("template.profile.html",db=db.fakes.find({'user':session['username']}))
	
			       
@app.route('/')
def index():
    if request.method == "GET":
        if 'username' in session:
            return redirect("/profile")
        else:
            return render_template("index.html")

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method=="GET":
	return render_template("login.html")
    else:
	button=request.form['submit']
	print button
	if button=='Login':
            username = request.form['username']
	    password = request.form['password']
	    flash(utils.login_user(username, password))
	    return redirect("/")
	else:
	    username = request.form['username']
	    password = request.form['password']
	    print utils.register_user(username, password)
	    return redirect("/")

@app.route('/logout', methods = ['POST'])
def logout():
        utils.logout_user()
        return redirect(url_for('index'))

if __name__ == '__main__':
	app.debug=True
        app.run(host='0.0.0.0', port=6005)
