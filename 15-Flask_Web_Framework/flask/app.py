from flask import Flask

'''
  It creates an instance of the Flask class,
  which will be your WSGI (Web Server Gateway Interface) application.
'''

## WSGI Application
app=Flask(__name__)

@app.route("/")  #decorator/route
def welcome():
    return "Welcome to Flask example. Hello all learner. Hope it will help you all."

@app.route("/index")  #decorator/route
def index():
    return "Welcome to index page."

if __name__=="__main__":
    app.run(debug=True)   ## debug=True: if your server is in runnng mode, and if you chnage something and want to reflect it without re-running your server it again