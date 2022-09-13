from flask import Blueprint, render_template, request

# Create Blueprint
auth = Blueprint('auth', __name__)

#route
@auth.route('/logout')
def logout():
    return render_template('logout.html')

# login
@auth.route('/sign-in', methods=['GET','POST'])
def sign_in():
    return render_template('sign_in.html')

# sign-up
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        # Split Data
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 유효성 검사
        if len(email) < 5 :
            pass
        elif len(nickname) < 2 :
            pass
        elif password1 == password2 :
            pass
        elif len(password1) < 7 :
            pass
        else:
            # Create User -> DB
            pass

    return render_template('sign_up.html')