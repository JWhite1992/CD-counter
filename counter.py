from flask import Flask, render_template, request, redirect,session 
app = Flask(__name__)
app.secret_key = "keep it simple"

@app.route('/')
def index():
    if 'number' not in session:
        session['number']=0
    session['number']+=1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session['number']=0
    return redirect('/')

@app.route('/addtwo')
def addtow():
    session['number']+=1
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)