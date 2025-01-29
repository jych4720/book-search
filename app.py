import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BOOK_API_URL = os.getenv('BOOK_API_URL')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_books():
    genre = request.args.get('genre')
    author = request.args.get('author')

    params = {}
    if genre:
        params['genre'] = genre
    if author:
        params['author'] = author

    try:
        response = requests.get(BOOK_API_URL, params=params)
        response.raise_for_status()
        books = response.json()
        return jsonify(books)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
