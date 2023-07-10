from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# db에 대한 실제 내용이 작성되어 있습니다
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM과 관련된 코드를 작성해 줍니다
    db.init_app(app)
    migrate.init_app(app, db)
    
    # main_views 내부에 있는 bp를 통한 라우팅 함수들을 등록
    from views import main_views
    app.register_blueprint(main_views.bp)

    return app

