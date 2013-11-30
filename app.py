from flask import Flask, render_template
import randomuser

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("template.profile.html")
	#return render_template("index.html")

@app.route("/profile")
def profile():
	#user=getUser()
	#return render_template("template.profile.html",picture=user["picture"],name=user["name"],age=user["age"],email=user["email"])
	return render_template("template.profile.html")
			       
			       
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5007)
