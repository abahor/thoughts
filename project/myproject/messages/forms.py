from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class createthought(FlaskForm):
    text = TextAreaField('Text', render_kw={'placeholder': 'what do you want to tell to the world?'})
    pri_pub = BooleanField('keep it private'
                           )
    submit = SubmitField('Post')
