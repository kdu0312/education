from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

# 사용자 추가, 수정, 삭제 라우트 및 함수 작성...

if __name__ == '__main__':
    app.run(debug=True)
