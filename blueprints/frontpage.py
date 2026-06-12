from flask import Blueprint, render_template, request, redirect, url_for, session
from connection.login_account import login_account
from connection.register_account import register_account

frontpage = Blueprint('frontpage', __name__)

@frontpage.route('/', methods=['GET', 'POST'])
def front():
    warning = None
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        register_username = request.form.get('register-username')
        register_password = request.form.get('register-password')

        if username and password:
            login = login_account(username, password)
            if login:
                session['logged_in'] = True
                session['user_id'] = login.account_id
                session['username'] = login.username
                return redirect(url_for('homepage.home'))
            else:
                warning = "Wrong Password or Username"
        elif register_username and register_password:
            register = register_account(register_username, register_password)
            if register:
                session['logged_in'] = True
                return redirect(url_for('homepage.home'))
        warning = "Something Went Wrong"    
    return render_template('frontpage.html', warning=warning)