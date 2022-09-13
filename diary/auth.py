from flask import Blueprint, render_template, request, flash

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
            flash('이메일은 5자 이상입니다.', category='error')
        elif len(nickname) < 2 :
            flash('닉네임은 2자 이상입니다..', category='error')
        elif password1 != password2 :
            flash('비밀번호가 서로 다릅니다.', category='error')
        elif len(password1) < 7 :
            flash('비밀번호가 너무 짧습니다.', category='error')
        else:
            # Create User -> DB
            flash('회원가입', category='success')

    return render_template('sign_up.html')