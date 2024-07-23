# TUTORIAL: https://www.techwithtim.net/tutorials/flask/html-templates/  completed 8/29/21
# TRY ME: https://medium.com/geekculture/how-to-architect-your-flask-rest-api-abf95637d9f5


# For multiple apps on the website use flask Blueprints

# html templates must be placed in directory 'templates' in the same folder as this file
# static css/js files must be placed in directory namded 'static' in the same folder as this file
# USE: <link rel="stylesheet" href="{{ url_for(static, filename='style.css') }}"> in your html template



# Requires: pip install flask
from flask import Flask, redirect, url_for, render_template, request, session, flash

# Requries pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta  # Used to set permanent sessions
app = Flask(__name__)
app.secret_key = "sdklfjeiosdlsjdfkl#$8jdsio**2kjdl"   # this is necessary for sessions
app.permanent_session_lifetime = timedelta(days=5)     # if you use permanent sessions then can set a duration
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'


# Define database table
db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
       self.name = name
       self.city = city
       self.addr = addr
       self.pin = pin




# http://127.0.0.1:5000/ or http://127.0.0.1:5000/home
@app.route("/")
@app.route("/home")
def home():
    return "<h1>HELLO</h1>"


# http://127.0.0.1:5000/admin
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Administrator"))  # Now when we go to /admin we will redirect to user with the argument "Admin!"


# http://127.0.0.1:5000/t1 THIS PASSES PARAMETERS TO THE TEMPLATE
@app.route("/t1")
def template():
    print('GOING to t1.html', flush=True) # THIS WILL PRINT TO THE OUTPUT SCREEN
    return render_template("t1.html", value="Testing", other="MAD")


# http://127.0.0.1:5000/t2  THIS USES INHERITANCE
@app.route("/t2")
def template2():
    return render_template("t2.html")


# http://127.0.0.1:5000/login
@app.route("/login", methods=["POST", "GET"]) # -   specify that a page works with both POST and GET requests
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")


# http://127.0.0.1:5000/user/fred
@app.route("/user/<name>")  # parameter 'name' gets passed to functon
def user(name):
    return f"<h2>Hello {name}!</h2>"


# http://127.0.0.1:5000/session1  # Store values for duration of session on client side
@app.route("/session1")
def session1():
    if 'value1' in session:
        return f"Session value1 = {session['value1']}"
    else:
        session['value1'] = 'xyz'   # use session.pop('value1', None) to remove session value
        return f"value stored in session"


# http://127.0.0.1:5000/session2  # Store values permanent session on client side
@app.route("/session2")
def session2():
    session.permanent = True  # <--- makes the session permanent
    if 'value2' in session:
        return f"Session value2 = {session['value2']}"
    else:
        session['value2'] = 'abc'
        return f"value stored in session"


# http://127.0.0.1:5000/flash-test
@app.route("/flash-test")  # parameter 'name' gets passed to functon
def flash_test():
    flash('test flash message', 'warning')  # flash info message passed to the next template rendered
    return render_template("flash.html")

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


# db.session.delete (object)  # to delete records from a table
# model.query.all () # retrieves all records (corresponding to SELECT queries) from the table.
# students.query.filter_by(city = ’Tokyo’).all()  # retrieved record set by using the filter attribute


@app.route('/show_all')
def show_all():
    print(students.query.all(), type(students.query.all()))
    return render_template('show_all.html', students=students.query.all())


# Run this to start the  program
if __name__ == "__main__":
    db.create_all() # Sets up database if it doesn't already exist
    app.run(debug=True)
