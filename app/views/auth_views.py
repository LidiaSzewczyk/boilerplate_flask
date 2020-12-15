from flask import Blueprint, request, url_for, render_template
from flask_login import login_user, logout_user
from werkzeug.utils import redirect

from app import db
from app.forms.user_forms import LoginForm, SignUpForm
from app.models.user_models import User

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.home'))
    return render_template('login.html', form=form)


@bp_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)


@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@bp_auth.route('/user/<username>')
def user(username):
    user_db = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user =user_db)
