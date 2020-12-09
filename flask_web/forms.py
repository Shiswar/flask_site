from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_web.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField("Enter username", 
    validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Enter Email",
    validators=[DataRequired(), Email()])

    password = PasswordField("Password",
    validators=[DataRequired(), Length(min=5, max=20)])

    confirm_password = PasswordField("Confirm Password",
    validators=[DataRequired(), Length(min=5, max=20), EqualTo("password")])

    submit = SubmitField("Submit")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken, please try another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered, log in to your account or user a different email')

class LoginForm(FlaskForm):
    username = StringField("Enter username", 
    validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Enter Email",
    validators=[DataRequired(), Email()])

    password = PasswordField("Password",
    validators=[DataRequired(), Length(min=5, max=20)])

    remember = BooleanField("Remember me")

    submit = SubmitField("Submit")

class UpdateAccountForm(FlaskForm):
    username = StringField("Update username", 
    validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Update Email",
    validators=[DataRequired(), Email()])

    picture = FileField('Update Profile picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField("Submit")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken, please try another one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already registered, log in to your account or user a different email')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')