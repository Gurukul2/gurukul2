from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField, SelectMultipleField, FileField, \
    BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_wtf.file import FileAllowed, FileRequired


# Custom validator to ensure password strength
def password_strength_check(form, field):
    password = field.data
    if len(password) < 6:
        raise ValidationError('Password must be at least 6 characters long.')
    # Add more password strength checks if needed


class RegistrationForm(FlaskForm):
    # Personal Information
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), password_strength_check])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])

    # Profile Details
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], validators=[DataRequired()])
    hobbies = SelectMultipleField('Hobbies',
                                  choices=[('reading', 'Reading'), ('traveling', 'Traveling'), ('gaming', 'Gaming'),
                                           ('cooking', 'Cooking')], validators=[DataRequired()])
    country = SelectField('Country', choices=[
        ('us', 'United States'),
        ('ca', 'Canada'),
        ('uk', 'United Kingdom'),
        ('au', 'Australia'),
        ('in', 'India'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    profile_picture = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])

    # Agreement
    agree = BooleanField('I agree to the Terms and Conditions', validators=[DataRequired()])

    submit = SubmitField('Register')
