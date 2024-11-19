from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

authors = [
    {"id": 1, "name": "Newton"},
    {"id": 2, "name": "Einstein"},
    {"id": 3, "name": "Max Planck"}
]

articles = [
    {"id": 1, "title": "On the Law of the Energy Distribution in the Normal Spectrum", "author_id": 3},
    {"id": 2, "title": "On the Electrodynamics of Moving Bodies", "author_id": 2},
    {"id": 3, "title": "Philosophiae Naturalis Principia Mathematica", "author_id": 1}
]

@app.route('/author', methods=['GET'])
def get_author():
    author_id = request.args.get('authorid', type=int, default=1)
    author = next((a for a in authors if a['id'] == author_id), None)
    if author is None:
        return jsonify({"error": "Author not found"}), 404
    return jsonify(author)

@app.route('/author-article', methods=['GET'])
def get_authors_article():
    author_id = request.args.get('authorid', type=int, default=1)
    author_articles = [a for a in articles if a['author_id'] == author_id]
    if not author_articles:
        return jsonify({"error": "No article found for this author"}), 404
    return jsonify(author_articles[0])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')