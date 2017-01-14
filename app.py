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

@app.route('/create_units', methods = ['POST','GET'])
@login_required
def create_unit():
    if request.method == 'POST':
        if db.session.query(Unit).filter(Unit.unit_name == request.form['unit_name']).count() > 0:
                flash('***Unit already in EAM***')
        else:
            db.session.add(Unit(request.form['unit_name'], request.form['description']))
            db.session.commit()
            flash('Unit was Created')
    return render_template('create_units.html')

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

@app.route('/create_parts', methods = ['POST','GET'])
@login_required
def create_parts():
    if request.method == 'POST':
        if db.session.query(Parts).filter(Parts.name == request.form['name']).count() > 0:
                flash('***Unit already in EAM***')
        else:
            db.session.add(Parts(request.form['name'], request.form['description'], request.form['quantity_on_hand'], request.form['unit_id']))
            db.session.commit()
            flash('Part was Created')
    return render_template('create_parts.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error=''
    user_lookup=db.session.query(User).all()
    if request.method == 'POST':
        if db.session.query(User).filter(User.username == request.form['username']).count() == 0:
            error = 'Invalid credentials. Please try again or Register.'
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
