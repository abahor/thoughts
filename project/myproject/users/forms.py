from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired
from myproject.models import Users


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Log In')


class RegisterationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Email'})
    username = StringField('username', validators=[InputRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6, message='your password is too short'),
                                         EqualTo('pass_confirm', message='Passwords must match')],
                             render_kw={'placeholder': 'Password'})

    pass_confirm = PasswordField('Confirm Password',
                                 validators=[InputRequired()], render_kw={'placeholder': 'confirm password'})
    submit = SubmitField('Register')

    def check_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already exists login instead')


class formRecover(FlaskForm):
    password = PasswordField('The new password',
                             validators=[DataRequired(), Length(min=6, message='your password is too short')],
                             render_kw={'placeholder': 'your new '
                                                       'password'})
    submit = SubmitField('Change')


class verifyForm(FlaskForm):
    password = PasswordField('your current password', validators=[DataRequired()],
                             render_kw={'placeholder': 'current password'})
    submit = SubmitField('Verify')


class yourEmail(FlaskForm):
    email = StringField('your email', validators=[DataRequired(), Email()], render_kw={"placeholder": 'your Email'})
    submit = SubmitField('send')


class confirmationForm(FlaskForm):
    password = PasswordField('the code', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('confirm')
