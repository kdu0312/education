#API CRUD 작업해야함
from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")

    @posts_blp.route("/", methods=["GET", "POST"])
    def posts():
        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == "GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            posts = cursor.fetchall()

            post_list = []
            for post in posts:
                post_list.append({
                    "id": post[0],
                    "title": post[1],
                    "content": post[2]
                })

            cursor.close()
            return jsonify(post_list)

        # 게시글 생성
        if request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message="Title or Content cannot be empty")

            sql = 'INSERT INTO posts(title, content) VALUES(%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()
            cursor.close()

            return jsonify({
                'msg': 'Successfully created post data',
                'title': title,
                'content': content
            }), 201

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == 'GET':
            sql = f"SELECT * FROM posts WHERE id = {id}"
            cursor.execute(sql)
            post = cursor.fetchone()

            if not post:
                abort(404, message="Not found post")

            
            return jsonify({
                "id": post[0],
                "title": post[1],
                "content": post[2]
            })

        # 게시글 수정
        elif request.method == 'PUT':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message="Title or Content cannot be empty")

            if not post:
                abort(400, "not found")

            sql = f"UPDATE posts SET title = %s, content = %s WHERE id = %s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()
            cursor.close()

            return jsonify({
                "msg": "Post updated successfully",
                "id": id,
                "title": title,
                "content": content
            })

        # 게시글 삭제
        elif request.method == 'DELETE':
            if not post:
                abort(400, "not found")
            sql = f"DELETE FROM posts WHERE id = {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()

            return jsonify({
                "msg": "Post deleted successfully",
                "id": id
            })

    return posts_blp