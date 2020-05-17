from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignUpForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=5, max=12)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=5, max=15)])
    confirm_password = PasswordField('Confirm password', 
                                     validators=[EqualTo('password')])
    submit = SubmitField('Sign Up')


class LogInForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=5, max=12)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=5, max=15)])
    submit = SubmitField('Log In')
        
