from myproject.models import Users
from flask import Blueprint,render_template,abort
from flask_login import login_required,LoginManager,login_user,logout_user
from myproject.users.forms import *

users = Blueprint("users",__name__,template_folder='temp')



@users.route('/login')
def login():
    form = Login()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            flash("Password is wrong or email doesn't exists")
        elif user.check_password(form.password.data):
            login_user(current_user)
            return redirect(url_for('messages.create_thought'))
        else:
            flash("Password is wrong or email doesn't exists")

    return render_template('login.html',form=form)

@users.route('/register')
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email= form.email.data),first()
        if user:
            flash('this email exist try {{ users.login }}')
        else:
            session['username'] = form.username.data
            session['password'] = form.password.data
            session['email'] = form.email.data
            session['confirmation_code'] = randnum()
            session['confirm']= True
            redirect(url_for('users.confirm'))
    return render_template('register.html',form=form)


@users.route('/confirm')
def confirm()
    if session['confirm']:
        form= confirmationForm()
        if form.validate_on_submit():
            if form.password.data == session['confirmation_code']:
                user = Users(email=session['email'],password=session['password'],username=session['username'])
                try:
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('users.login'))
                except Exception as e:
                    db.session.rollback()
                    return render_template('something_went_wrong.html')
        return render_template('confirm.html',form=form)
    else:
        try:
            session['username'] = None
            session['password'] = None
            session['email'] = None
            session['confirm'] = None
            abort(404)
        except:
            abort(404)
    return ''


def randnum():
    return digits = "".join( [random.choice(string.digits) for i in xrange(9)] )
