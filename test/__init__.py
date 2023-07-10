from flask import Flask

#Flask는 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식해서
#Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return f'Hello, {__name__}'

    #라우팅 주소를 만들 때 '/경로명'까지만
    #그 다음에 만들어질 하위 경로도 '/경로명'
    @app.route('/chaeyoung')
    def hello_cy():
        return f'Hello, Chae-Young'
    return app