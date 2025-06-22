# db연결
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["bookstore"]  # ← 이 줄이 빠졌을 가능성 높음

# 데이터 삽입
def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"}
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()

if __name__ == "__main__":
    insert_data()


# 문제 1 특정 장르의 책찾기
def find_books_by_genre(db, genre):
    books_collection = db.books
    query = {"genre": genre}
    projection = {"_id": 0, "title": 1, "author": 1}

    books = books_collection.find(query, projection)
    for book in books:
        print(book)

find_books_by_genre(db, "fantasy")

# 문제 2 감독별 평균 영화평점 계산
def calculate_average_ratings(db):
    movies_collection = db.movies
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}}
    ]

    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

calculate_average_ratings(db)

# 문제 3 특정 사용자의 최근 행동 조회
def find_recent_actions_by_user(db, user_id, limit=5):
    user_actions_collection = db.user_actions
    query = {"user_id": user_id}
    sort_criteria = [("timestamp", -1)]

    actions = user_actions_collection.find(query).sort(sort_criteria).limit(limit)
    for action in actions:
        print(action)

find_recent_actions_by_user(db, 1)

# 문제 4 출판 연도별 책의 수 계산
def count_books_by_year(db):
    books_collection = db.books
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]

    results = books_collection.aggregate(pipeline)
    for result in results:
        print(result)


count_books_by_year(db)

# 문제 5 특정 사용자의 행동 요형 업데이트

from datetime import datetime

def update_user_actions_before_date(db, user_id, date, old_action, new_action):
    user_actions_collection = db.user_actions
    query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}
    update = {"$set": {"action": new_action}}

    result = user_actions_collection.update_many(query, update)
    print(f"Updated {result.modified_count} documents.")


update_user_actions_before_date(db, 1, datetime(2023, 4, 10), "view", "seen")