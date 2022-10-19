from flask import Blueprint, render_template, request
    
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("signin.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return '<h1 class="auth" >Sign Up Page</h1>'

@auth.route('/logout')
def logout():
    return '<h1 class="auth" >Logout Page</h1>'