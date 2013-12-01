#!/usr/bin/python

from flask import Flask, request, render_template, redirect, session, url_for, flash
import utils, json

app = Flask(__name__)
app.secret_key = 'abcd'
app.debug = True

@app.route("/profile")
def profile():
	#user=getUser()
	#return render_template("template.profile.html",picture=user["picture"],name=user["name"],age=user["age"],email=user["email"])
    return render_template("template.profile.html")
			       
			       
@app.route('/')
def index():
    if 'username' in session:
	print 'loggedi n'
	return redirect("/profile")
    else:
	return redirect("/login")

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
        app.run(host='0.0.0.0', port=5000)
