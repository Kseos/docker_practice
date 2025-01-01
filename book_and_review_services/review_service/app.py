from flask import Flask, jsonify, request

app = Flask(__name__)

reviews = []

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews), 200

@app.route('/reviews/add', methods=['POST'])
def add_review():
    new_review = request.json
    
    if not new_review or 'book_title' not in new_review or 'reviewer' not in new_review or 'comment' not in new_review:
        return jsonify({'error': 'Book title, reviewer, and comment are required'}), 400

    reviews.append({
        'book_title': new_review['book_title'],
        'reviewer': new_review['reviewer'],
        'comment': new_review['comment']
    })
    
    return jsonify({'message': 'Review added successfully'}), 201

@app.route('/reviews/<string:book_title>', methods=['GET'])
def get_reviews_by_book(book_title):
    filtered_reviews = [review for review in reviews if review['book_title'] == book_title]
    return jsonify(filtered_reviews), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)