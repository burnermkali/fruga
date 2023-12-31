from flask import session, Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user,logout_user,login_required

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('please check your login details and try again')
        return redirect(url_for('auth.login'))
    
    login_user(user)
    

    return redirect(url_for('main.dashboard'))
                
    


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    team = request.form.get('team')
    password = request.form.get('password')

    team_nospace = team.replace(" ", "")

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    user1 = User.query.filter_by(team=team).first()
    if user1:
        flash('Team already has an account')
        return redirect(url_for('auth.signup'))
    
    
    new_user = User(email=email, name=name, team=team, team_nospace=team_nospace, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


