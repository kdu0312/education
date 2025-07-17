from flask import Flask, render_template
from jwt_utils import configure_jwt  # JWT 설정 함수를 임포트합니다.
from routes.user import user_bp

app = Flask(__name__)
configure_jwt(app)  # JWT 관련 추가 설정을 적용합니다.

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)