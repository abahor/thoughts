from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class createthought(FlaskForm):
    text = TextAreaField('Text', render_kw={'placeholder': 'What do want to tell to the world?'})
    pri_pub = BooleanField('keep it private',
                           validators=[DataRequired()])
    submit = SubmitField('Post')
