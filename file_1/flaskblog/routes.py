from flask import  render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm , BarcodeForm
from flaskblog.models import User , Product , Warehouse
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/barcode", methods=['GET', 'POST'])
def barcode():
    form = BarcodeForm()
    if form.validate_on_submit():
        flash(f'barcode ok', 'success')
        return redirect(url_for('home'))
    return render_template('barcode.html', title='barcode', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # kanw hash to password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) #vazw ta stoixia thn formas sthn metavliti user
        db.session.add(user)#ta kanw add sthn bash
        db.session.commit()
        flash(f'Account created !Please log in ', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:

            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
   return render_template('account.html', title='Account')
