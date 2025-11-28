import string
from random import choice, randint

from myproject import mail
from flask import Blueprint, render_template, abort, redirect, url_for, session, flash, Markup
from flask_login import current_user, login_required, logout_user, login_user
from myproject.models import Users
from flask_mail import *
from myproject.users.forms import RegisterationForm, formRecover, verifyForm, yourEmail, confirmationForm, Login
from myproject import db

users = Blueprint('users', __name__, template_folder='temp')


@users.route('/')
def main():
    return render_template('main.html')


@users.route('/create')
@login_required
def create():
    return render_template('create.html')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.create'))
    form = Login()
    if form.validate_on_submit():
        print(form.email.data)
        print(Users.query.filter(Users.email == form.email.data))
        user = Users.query.filter(Users.email == form.email.data).first()
        print(user)
        if user and user.check_password(form.password.data):
            login_user(user)
            print('--------------------')
            return redirect(url_for('users.create'))
    print(form.errors)
    return render_template('login.html', form=form)


@users.route('/register', methods=['post', 'get'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.create'))
    form = RegisterationForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            flash(Markup('this email already exist login instead'))
        else:
            session['email'] = form.email.data
            session['password'] = form.password.data
            session['username'] = form.username.data
            session['code'] = randomcode()
            session['confirm'] = True
            message = Message('confirmation code',
                              sender="jousefgamal46@gmail.com",
                              recipients=[form.email.data])
            message.body = f'here is the confirmation code {session["code"]}'
            message.html = render_template('confirmation.html')
            print(session['code'])
            try:
                mail.send(message)
            except:
                return abort(404)
            return redirect(url_for('users.confirm'))

    return render_template('register.html', form=form)


@users.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if current_user.is_authenticated:
        return abort(404)
    if session['confirm'] is None:
        return abort(404)
    form = confirmationForm()
    if form.validate_on_submit():
        if form.code.data == session['code']:
            new = Users(email=session['email'], password=session['password'], username=session['username'])
            try:
                db.session.add(new)
                db.session.commit()
            except Exception as e:
                abort(404)
            session['email'] = None
            session['password'] = None
            session['code'] = None
            session['confirm'] = None
    print(form.errors)
    return render_template('confirm.html', form=form)


def randomcode():
    s = "".join(choice(string.digits) for x in range(randint(1, 8)))
    return s


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@users.route('/about')
def about():
    return render_template('about.html')


@users.route('/account')
@login_required
def account():
    return render_template('account.html')
