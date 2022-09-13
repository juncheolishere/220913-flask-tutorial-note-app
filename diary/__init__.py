from flask import Flask


#Create App
def create_app():
    app = Flask(__name__)
    # 앱에 사용될 시크릿 키 정의.
    # 자동적으로 세팅이 된다. 로그인, 보안과 관련된 기능을 플라스크에서 행사할때
    # 기준 값을 기준으로 행사되는데 그 기준되는 값을 설정하는 것이다.
    # 어떠한 문자열이어도 상관없다. like boss.
    app.config['SECRET_KEY'] = 'jc_secret_key'

    # Import Blueprint
    from .views import views
    from .auth import auth

    # Apply Blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app