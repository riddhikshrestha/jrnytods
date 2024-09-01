## 4.
## Variable Rule
## Jinja 2 Template Engine
## Building URL Dynamically



## Jinja2 Template Engine
'''
{{ }}   : expression to print output in html
{%...%}  : conditions, for loops
{#...#}  : this is for comments
'''

from flask import Flask, render_template,request,redirect,url_for



## WSGI Application
app=Flask(__name__)

@app.route("/")  
def welcome():
    return "<html><h1>Welcome to html integration with flask.</h1></html>"

@app.route("/index",methods=['GET'])  
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


# Variable Rule
# @app.route('/success/<score>')
# def success(score):
#     return "The mark you got is "+ score

## When we apply some rule that user can only provide some int value or float i.e. basically called a Variable Rule
## Here we are restricting paramter with the datatype int
# @app.route('/success/<int:score>')
# def success(score):
#     return "The mark you got is "+ str(score)

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html',results=res)

## For Loop result in JINGA2
@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp = {'score': score,"res":res}
    return render_template('result1.html',results=exp)


## IF Condition Result: in JINGA2
@app.route('/successif/<int:score>')
def successif(score):
       
    return render_template('result2.html',results=score)


## Build url dynamically
@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')  # At /submit url's i.e. get request, after the form filled it wil be post request

    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)   
