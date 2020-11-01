from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "<h1>Hello, Admin</h1>"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "<h1>Hello,%s <h1>"%guest

@app.route('/rara')
def rara():
    return "<legend>raraPOoka</legend>"

@app.route('/hello/<name>')
def hello(name):
    if name=="admin":
        return redirect(url_for('hello_admin'))
    elif name=="satya":
        return redirect(url_for('rara'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ =="__main__":
    app.run(debug=True)