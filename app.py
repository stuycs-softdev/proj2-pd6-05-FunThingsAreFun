from flask import Flask, render_template
from py import *
import randomuser

app = Flask(__name__)
app.config.from_object('py.config')

env = app.jinja_env
env.line_statement_prefix = '='
env.globals.update(utils=utils)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/profile")
def profile():
	user=getUser()
	return render_template("template.profile.html",picture=user["picture"],name=user["name"],age=user["age"],email=user["email"])
			       
			       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5007)
