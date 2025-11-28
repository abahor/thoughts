from flask import Blueprint, render_template, url_for, redirect, abort, Response, session, request
from myproject.models import Users, Thoughts
from myproject.messages.forms import createthought
from flask_login import login_required, current_user
from myproject import db

messages = Blueprint('messages', __name__,
                     template_folder='temp')

@messages.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = createthought()
    if form.validate_on_submit():
        text = form.text.data
        print(form.pri_pub.data)
        d = Thoughts(text=form.text.data, user_id=current_user.id, pri=form.pri_pub.data)
        try:
            db.session.add(d)
            db.session.commit()
        except Exception as e:
            raise

        return redirect(url_for('messages.main_page'))
    print(form.errors)
    return render_template('createthought.html', form=form)


@messages.route('/main')
def main_page():
    return render_template('main_page.html')


@messages.route('/load', methods=['POST'])
def load():
    quantity = 10
    more = int(request.args.get('c'))
    # try:
    # more = session['more']
    # session['more'] += 3
    # except Exception as e:
    # session['more'] = 0
    # more = 0

    d = Thoughts.query.order_by(Thoughts.date.desc()).all()
    td = d[more: more + quantity]
    print(td)

    resp = Response(render_template('load.html', messages=td))

    return resp
