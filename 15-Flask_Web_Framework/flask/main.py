"""
2. Integrate HTML file with Flask
"""
from flask import Flask, render_template

'''
  It creates an instance of the Flask class,
  which will be your WSGI (Web Server Gateway Interface) application.
'''

## WSGI Application
app=Flask(__name__)

@app.route("/")  #decorator/route
def welcome():
    return "<html><h1>Welcome to html integration with flask.</h1></html>"

@app.route("/index")  #decorator/route
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)   ## debug=True: if your server is in runnng mode, and if you chnage something and want to reflect it without re-running your server it again