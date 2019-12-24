from flask import Blueprint, render_template, url_for, redirect, abort
from myproject.models import Users, Thoughts
from myproject.messages.forms import createthought
from flask_login import login_required, current_user

messages = Blueprint('messages', __name__,
                     template_folder='temp')  # ----------------- use two encrytion in the chat app over encrytion


@messages.route('/create')
@login_required
def create_thought():
    form = createthought()
    if form.validate_on_submit():
        text = form.text.data
        d = Thoughts(text=form.text.data, user_id=current_user.id, private=form.pri_pub.data)

    return render_template('createthought.html', form=form)

@messages.route('/main')
def main_page():
    return ''

