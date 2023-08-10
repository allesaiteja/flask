from flask import Flask, render_template,request,flash
from form  import ContactForm


app=Flask(__name__)
app.config['SECRETE_KEY'] = 'saiteja'


@app.route('/')
def home():
    return "Welcome to WTForms Tutorialf"

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method=='POST':
        if form.validate() == False:
            flash("All Fields are required")
            return render_template('contact.html',form=form)
        else:
            return 'Form Posted Succesfully'
        
        if __name__=='__main__':
            app.run(debug=True)
