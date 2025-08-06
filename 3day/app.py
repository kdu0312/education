from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:090909@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#blueprint 설정
app.config["API_TITLE"] = "Book API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from routes.board import board_blp
api.register_blueprint(board_blp)

from flask import render_template

@app.route('/manage-boards')
def manage_boards():
    return render_template("borads.html")

@app.route("/manage-users")
def manage_users():
    return render_template("users.html")

if __name__ == '__main__': #
    with app.app_context():
        print("complete")
        db.create_all()
    
    app.run(debug=True) #서버를 실행하세요.
