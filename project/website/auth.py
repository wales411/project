from xmlrpc.client import boolean
from flask import Blueprint, render_template, request, flash, redirect, url_for

#blueprint helps with the organization of app url

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template ("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        numberPlate = request.form.get('numberPlate')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 character', category='error')
        elif len(firstName) < 2:
            flash('firstname must be greater than 1 character', category='error')
        elif password1 != password2:
           flash('Password do not match', category='error')
        elif len(password1) < 4:
            flash('password must be atleast 4 character', category='error')
        else:
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
            
            # add user to database

    return render_template ("sign_up.html")
