from flask_wtf import Form
from wtforms import StringField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField

from wtforms import validators,ValidationError

class ContactForm(Form):
    name = StringField('Name of the Student',[validators.DataRequired('Please enter your name')])
    Gender = RadioField('Gender', choices=[( 'M','Male'),('F','Female')])
    Address = TextAreaField("Address")

    email =StringField("Email",[validators.DataRequired("Please enter your email address"),
                                  validators.Email("Please enter valid email address")])
    
    Age = IntegerField("Age")
    Language = SelectField('Language Known', choices=[('CPP', 'C++'), ('py','Python')])
    


    submit = SubmitField("Submit")