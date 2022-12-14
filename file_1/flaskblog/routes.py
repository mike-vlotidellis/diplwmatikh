from flask import  render_template, url_for, flash, redirect ,request ,jsonify
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm , BarcodeForm
from flaskblog.models import User , Product , Warehouse , SearchInfo
from flask_login import login_user, current_user, logout_user, login_required
import json



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/barcode", methods=['GET', 'POST'])
def barcode():
    form = BarcodeForm()
    if form.validate_on_submit():
       # search = SearchInfo(barcode=form.barcode.data)
       # db.session.add(search)
       # db.session.commit()
        #searched = SearchInfo.query.first()
        searched_barcode = Product.query.filter_by(barcode=form.barcode.data).all()
        if searched_barcode == []:
            flash('no items ', 'danger')
            return redirect(url_for('barcode'))
        return redirect(url_for('search_results'))

    return render_template('barcode.html', title='barcode', form=form)

@app.route("/search_results", methods=['GET', 'POST'])
def search_results():
   # searched_barcode = Product.query.filter_by(barcode=form.barcode.data).all()
    
    return render_template('search_results.html',title='Search Results')    

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



@app.route('/upload')
def upload_file1():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      with open(f.filename) as g:
            data = json.load(g)
            for item in data['items']:
                item_for_load=Product (barcode=item['barcode'] ,name =item['name'],kind=item['kind'],quantity=item['quantity'],warehouse_id=item['warehouse_id']) 
                db.session.add(item_for_load)
                db.session.commit()
      return 'file uploaded successfully'

@app.route('/search', methods = ['GET', 'POST'])
def serch():
    if request.method == "POST":
        search = request.form.get("todo")
        searched_barcode = Product.query.filter_by(barcode=search).first()
        if searched_barcode : print(searched_barcode.name)
        return jsonify ({'name':searched_barcode.name, 'kind':searched_barcode.kind})
            
    return render_template('search.html') 

#@app.route("/test")
# def test():

#     print ("hello word")
#     with open('states.json') as f:
#         data = json.load(f)

#         for state in data['states']: 
#             print (state['name'])
                
#     return 'file uploaded successfully'





    #with open('states.json') as f:
   #        data = json.load(f)
    #        fruits = ["apple", "banana", "cherry"]
    #        for x in fruits:
    #            print(x)
    #        for state in data['states']:
    #            print(state['name'])
    #            return 'file uploaded successfully'
