from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'saiteja'

class ContactForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    contact = ContactForm()
    names = []  # Store the names in a list

    if contact.validate_on_submit():
        name = contact.name.data
        names.append(name)  # Add the name to the list
        contact.name.data = ''  # Clear the form field for the next entry

    return render_template('index.html', contact=contact, names=names)

if __name__ == '__main__':
    app.run(debug=True)
