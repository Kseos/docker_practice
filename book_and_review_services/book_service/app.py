from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
books = []

@app.route('/books', methods=['GET'])
def get_books():
    if not books:
        url = 'https://openlibrary.org/search?subject=Fantasy'
        response = requests.get(url)
        soup = bs(response.content, 'html.parser')

        count = 0
        for item in soup.select('.searchResultItem'):
            if count >= 5:
                break
            title = item.select_one('.booktitle a').get_text(strip=True)
            author = item.select_one('.bookauthor a').get_text(strip=True)
            rating = item.select_one('[itemprop="ratingValue"]').get_text(strip=True)
            
            books.append({'title': title, 'author': author, 'rating': rating})
            count +=1

    return jsonify(books), 200

@app.route('/books/title/<string:title>', methods=['GET'])
def get_book(title):
    book = next((b for b in books if b['title'].lower() == title.lower()), None)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)