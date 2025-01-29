from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BOOK_API_URL = "http://book-api.uksouth.azurecontainer.io:5000/api/books"


@app.route('/books', methods=['GET'])
def get_books():
    genre = request.args.get('genre')
    url = 'http://book-api.uksouth.azurecontainer.io:5000/api/books'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        books = response.json()
        
        # If a genre query parameter is provided, filter the books by genre
        if genre:
            filtered_books = [book for book in books if genre.lower() in book['genre'].lower()]
            return jsonify(filtered_books)
        
        # If no genre parameter is provided, return the third book by default
        else:
            return jsonify(books[2])  # Return the third book (index 2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
