from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request

from styx.core.users.forms import (RegistrationForm, LoginForm,
                                   UpdateAccountForm)
from flask_login import login_user, current_user, logout_user, login_required

from styx.utils import save_image

from styx.services.users import user_service
from styx.dao.users import user_dao


users = Blueprint('users', __name__)


@users.route("/register",
             methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user_service.create_user(username, email, password)

        flash('Account created! You can now log in.', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html',
                           title='Register',
                           form=form)


@users.route("/login",
             methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = user_dao.get_by_email(email=form.email.data.casefold())
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page \
                else redirect(url_for('main.home'))
        else:
            flash("Login unsuccessful!", 'danger')

    return render_template('login.html',
                           title='Log in',
                           form=form)


@users.route("/logout",
             methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account",
             methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        if form.image.data:
            image_file = save_image(form.image.data, path="profile_pictures")
        else:
            image_file = None

        new_username = form.username.data
        new_email = form.email.data

        user_id = current_user.id
        user_service.update_user(user_id=user_id, username=new_username,
                                 email=new_email, image_file=image_file)

        flash("Your account has been successfully updated!", 'success')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static',
                         filename=f"profile_pictures/"
                                  f"{current_user.image_file}")

    return render_template('account.html',
                           title='Account',
                           image_file=image_file, form=form)
