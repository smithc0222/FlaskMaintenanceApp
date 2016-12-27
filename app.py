from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy


#create app object
app = Flask(__name__)


#config
import os
app.config.from_object('config.DevelopmentConfig')


#create sqlalchemy object
db = SQLAlchemy(app)


from models import *
# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    units=db.session.query(Unit).all()
    parts=db.session.query(Parts).all()
    return render_template('index.html', units=units, parts=parts)

@app.route('/create', methods = ['POST','GET'])
@login_required
def create_unit():
    if request.method == 'POST':
        if db.session.query(Unit).filter(Unit.unit == request.form['unit']).count() > 0:
                flash('***Unit already in EAM***')
        else:
            db.session.add(Unit(request.form['unit'], request.form['description']))
            db.session.commit()
            flash('Unit was Created')
    return render_template('create.html')

@app.route('/units')
@login_required
def units():
    units=db.session.query(Unit).all()
    return render_template('units.html', units=units)

@app.route('/parts')
@login_required
def parts():
    parts=db.session.query(Parts).all()
    return render_template('parts.html', parts=parts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()
