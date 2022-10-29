from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,ValidationError
from flaskblog.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() # se periptwsh poy yparxei kataxwrish sthn bash me to idio username me ayto poy evale twra o xrhsths sthn bash tote h metavlith user tha parei timh an einai kenh tote paei na pei oti den yparxei to username sthn bash  
        if user:
            raise ValidationError('username already taken1')



    def validate_email(self, email):

        email = User.query.filter_by(email=email.data).first() # se periptwsh poy yparxei kataxwrish sthn bash me to idio email me ayto poy evale twra o xrhsths sthn bash tote h metavlith user tha parei timh an einai kenh tote paei na pei oti den yparxei to email sthn bash

        if email:
            raise ValidationError('email already taken2')        




class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class BarcodeForm(FlaskForm): 
        barcode = StringField(' 16 digits barcode',
                        validators=[DataRequired(), Length(min=15, max=16)])
        submit = SubmitField('submit')
