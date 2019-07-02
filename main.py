from flask import Flask, request, redirect, render_template
import cgi, re



app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return '<h1>Hello, {0} </h1>'.format(username)

# @app.route("/validate-fields")
# def display_form():
#     return render_template('form.html', username='', username_error='', email='', 
#     email_error='', password='', password_error='', password_verify='', password_verify_error='')

def validate_email(email):
    valid = True
    if len(email) <3 or len(email) >20:
        valid = False
    if ' ' in email or '@' not in email or '.' not in email:
        valid = False
    return valid

@app.route("/", methods = ['POST'])
def validate_fields():

    username = request.form['username']
    email =request.form['email']
    password = request.form['password']
    password_verify = request.form['password_verify']

    username_error = ''
    email_error = ''
    password_error= ''
    password_verify_error = ''
       
    if username == '':
        username_error = "This field is required"
        username = ''
    elif " " in username:
        username_error = "This field can NOT contain spaces"
        username = ''
    elif len(username) <3 or len(username) > 20:
        username_error = "This field must be between 3 and 20 characters"
        username = ''
    
    if password == '':
        password_error = "This field is required"
        password = ''
    elif " " in password:
        password_error = "This field can NOT contain spaces"
        password = ''
    elif len(password) <3 or len(password) > 20:
        password_error = "This field must be between 3 and 20 characters"
        password = ''

    if password_verify == '':
        password_verify_error = "This field is required"
        password_verify= ''
    elif password != password_verify:
        password_verify_error = "Passwords do not match. Please re-enter"
        password_verify = ''

    if not validate_email(email):
        email_error = "This is not a valid email address."
        email = ''

    if username_error != '' or password_error != '' or password_verify_error != '' or email_error != '':

        return render_template('form.html', username = username, username_error=username_error, 
        password = password, password_error = password_error, password_verify = password_verify,
        password_verify_error = password_verify_error, email = email, email_error=email_error)

    else:
        username = username
        return redirect('/welcome?username={0}'.format(username))


    





#TO DO: create form that includes username, email, password and password verify
# this is in the form template

#TO DO: create function to determine if username, password or verfify password is empty (email is optional), otherwise return error (error should be next to the field)
# 
# 



#TO DO: create function to determine if username or password is not valid (for example - if tontains a space or consists of less than 3 characters or more than 20 characters), otherwise return error (error should be next to the field)

#TO DO: create a function to determine if password and password verify match, otherwise return error (error should be next to the field)

#TO DO: create a function to determine if it is a valid email. The field CAN be empty but if it is filled is needs to be validated. Criteria is that there is only one @ sign, a single., contains no spaces and is between 3 and 20 characters long.  (error should be next to the field)

#TO DO: preserve the username and email fields, preserve what the user typed so they don't have to re-type it but password fields should clear for security reasons.

#TO DO: If all fields are valid, then redirect to a new welcome pagethat uses the username input to display welcome message of "Welcome, [username]"

#TO DO: use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.





app.run()