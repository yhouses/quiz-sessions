import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"]; 
@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/retakeQuiz')
def retakeQuiz():
    session.clear()
    return redirect(url_for('renderMain'))

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if request.form['firstName']=="" or request.form['lastName']=="":
        return redirect('/page1')
    session["firstName"]=request.form['firstName']
    session["lastName"]=request.form['lastName']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if request.form['wordDef']=="":
        return redirect('/page2')
    session["wordDef"]=request.form['wordDef']
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False)
