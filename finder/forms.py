from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from finder.models import User


class SignUpForm(FlaskForm):
    """Use this class to create a signup form"""

    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=5, max=12)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=5, max=15)])
    confirm_password = PasswordField('Confirm password', 
                                     validators=[EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validate the uniqueness of the entered username."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken!')

    def validate_email(self, email):
        """Validate the uniqueness of the entered email."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken!')


class LogInForm(FlaskForm):
    """Use this class to create a login form"""

    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=5, max=12)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=5, max=15)])
    submit = SubmitField('Log In')
