from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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


class LoginForm(FlaskForm):
    username = StringField("Enter username", 
    validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Enter Email",
    validators=[DataRequired(), Email()])

    password = PasswordField("Password",
    validators=[DataRequired(), Length(min=5, max=20)])

    remember = BooleanField("Remember me")

    submit = SubmitField("Submit")

