from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/", methods=['POST'])
def validation():

    username_input = request.form['username']
    password_input = request.form['password']
    verify_input = request.form['verify']
    email_input = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username_input == "" or " " in username_input:
        username_error= "Username Field must have characters" 
        username_input = ""
    elif len(username_input) < 3 or len(username_input) > 20:
        username_error= "Username Field must be between 3 and 20 characters" 
        username_input = ""

    if password_input == "" or " " in password_input:
        password_error = "Password Field must have characters"
        password_input = ""
    elif len(password_input) < 3 or len(password_input) > 20:
        password_error = "Password Field must be between 3 and 20 characters"
        password_input = ""

    else:
        if password_input != verify_input:
            verify_error = "The Passwords do not match"

    if email_input == "":
        email_input = email_input

    elif '@' not in email_input or '.' not in email_input or " " in email_input or len(email_input) < 3 or len(email_input) > 20:
        email_error = "Email is Invalid"
        email_input = ""

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username_input)

    else:
        return render_template('form.html', username=username_input, email=email_input, username_error=username_error, 
            password_error=password_error, verify_error=verify_error, email_error=email_error)
 

@app.route("/")
def index():
    return render_template('form.html')


app.run()