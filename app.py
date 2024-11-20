from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

authors = [
    {"id": 1, "name": "Isaac Newton"},
    {"id": 2, "name": "Albert Einstein"},
    {"id": 3, "name": "Max Planck"},
    {"id": 4, "name": "Marie Curie"},
    {"id": 5, "name": "Niels Bohr"},
    {"id": 6, "name": "Werner Heisenberg"},
    {"id": 7, "name": "Erwin Schrödinger"},
    {"id": 8, "name": "Richard Feynman"},
    {"id": 9, "name": "Paul Dirac"},
    {"id": 10, "name": "Enrico Fermi"},
    {"id": 11, "name": "Louis de Broglie"},
    {"id": 12, "name": "James Clerk Maxwell"},
    {"id": 13, "name": "Wolfgang Pauli"},
    {"id": 14, "name": "Ernest Rutherford"},
    {"id": 15, "name": "Galileo Galilei"},
    {"id": 16, "name": "Johannes Kepler"},
    {"id": 17, "name": "Michael Faraday"},
    {"id": 18, "name": "Louis Pasteur"},
    {"id": 19, "name": "Charles Darwin"},
    {"id": 20, "name": "Nikola Tesla"}
]

articles = [
    {
        "id": 1, 
        "title": "Philosophiae Naturalis Principia Mathematica", 
        "author_id": 1,
        "related_articles": [
            {"id": 2, "relationshipType": "contains"},
            {"id": 3, "relationshipType": "is_contained_by"},
            {"id": 16, "relationshipType": "contains"}
        ]
    },
    {
        "id": 2,
        "title": "On the Electrodynamics of Moving Bodies",
        "author_id": 2,
        "related_articles": [
            {"id": 3, "relationshipType": "contains"},
            {"id": 4, "relationshipType": "contains"},
            {"id": 9, "relationshipType": "is_contained_by"}
        ]
    },
    {
        "id": 3,
        "title": "On the Law of the Energy Distribution in the Normal Spectrum",
        "author_id": 3,
        "related_articles": [
            {"id": 2, "relationshipType": "is_contained_by"},
            {"id": 4, "relationshipType": "contains"},
            {"id": 5, "relationshipType": "contains"}
        ]
    },
    {
        "id": 4,
        "title": "Research on Radioactive Substances",
        "author_id": 5,
        "related_articles": [
            {"id": 5, "relationshipType": "contains"},
            {"id": 6, "relationshipType": "contains"},
            {"id": 14, "relationshipType": "is_contained_by"}
        ]
    },
    {
        "id": 5,
        "title": "On the Constitution of Atoms and Molecules",
        "author_id": 6,
        "related_articles": [
            {"id": 6, "relationshipType": "contains"},
            {"id": 7, "relationshipType": "contains"},
            {"id": 13, "relationshipType": "is_contained_by"}
        ]
    },
    {
        "id": 6,
        "title": "The Physical Principles of the Quantum Theory",
        "author_id": 7,
        "related_articles": [
            {"id": 5, "relationshipType": "is_contained_by"},
            {"id": 7, "relationshipType": "contains"},
            {"id": 8, "relationshipType": "contains"}
        ]
    },
    {
        "id": 7,
        "title": "An Undulatory Theory of the Mechanics of Atoms and Molecules",
        "author_id": 8,
        "related_articles": [
            {"id": 6, "relationshipType": "is_contained_by"},
            {"id": 8, "relationshipType": "contains"},
            {"id": 11, "relationshipType": "contains"}
        ]
    },
    {
        "id": 8,
        "title": "Space-Time Approach to Quantum Electrodynamics",
        "author_id": 9,
        "related_articles": [
            {"id": 9, "relationshipType": "contains"},
            {"id": 10, "relationshipType": "contains"}
        ]
    },
    {
        "id": 9,
        "title": "The Principles of Quantum Mechanics",
        "author_id": 10,
        "related_articles": [
            {"id": 8, "relationshipType": "is_contained_by"},
            {"id": 10, "relationshipType": "contains"},
            {"id": 13, "relationshipType": "contains"}
        ]
    },
    {
        "id": 10,
        "title": "On the Production of Nuclear Reactions by Fast Charged Particles",
        "author_id": 1,
        "related_articles": [
            {"id": 4, "relationshipType": "contains"},
            {"id": 14, "relationshipType": "contains"}
        ]
    },
    {
        "id": 11,
        "title": "The Wave Nature of the Electron",
        "author_id": 11,
        "related_articles": [
            {"id": 7, "relationshipType": "is_contained_by"},
            {"id": 9, "relationshipType": "contains"}
        ]
    },
    {
        "id": 12,
        "title": "A Dynamical Theory of the Electromagnetic Field",
        "author_id": 12,
        "related_articles": [
            {"id": 17, "relationshipType": "contains"},
            {"id": 2, "relationshipType": "contains"}
        ]
    },
    {
        "id": 13,
        "title": "The Connection Between Spin and Statistics",
        "author_id": 13,
        "related_articles": [
            {"id": 9, "relationshipType": "is_contained_by"},
            {"id": 8, "relationshipType": "contains"}
        ]
    },
    {
        "id": 14,
        "title": "The Scattering of Alpha and Beta Particles by Matter",
        "author_id": 14,
        "related_articles": [
            {"id": 4, "relationshipType": "contains"},
            {"id": 10, "relationshipType": "is_contained_by"}
        ]
    },
    {
        "id": 15,
        "title": "Dialogue Concerning the Two Chief World Systems",
        "author_id": 15,
        "related_articles": [
            {"id": 1, "relationshipType": "contains"},
            {"id": 16, "relationshipType": "contains"}
        ]
    },
    {
        "id": 16,
        "title": "Astronomia nova",
        "author_id": 16,
        "related_articles": [
            {"id": 1, "relationshipType": "is_contained_by"},
            {"id": 15, "relationshipType": "is_contained_by"}
        ]
    },
    {
        "id": 17,
        "title": "Experimental Researches in Electricity",
        "author_id": 17,
        "related_articles": [
            {"id": 12, "relationshipType": "is_contained_by"},
            {"id": 20, "relationshipType": "contains"}
        ]
    },
    {
        "id": 18,
        "title": "Studies on Fermentation",
        "author_id": 18,
        "related_articles": []
    },
    {
        "id": 19,
        "title": "On the Origin of Species",
        "author_id": 19,
        "related_articles": []
    },
    {
        "id": 20,
        "title": "System of Polyphase Alternating Current",
        "author_id": 20,
        "related_articles": [
            {"id": 17, "relationshipType": "is_contained_by"}
        ]
    }
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

@app.route('/articles', methods=['GET'])
def get_all_articles():
    return jsonify(articles)

@app.route('/article', methods=['GET'])
def get_article():
    article_id = request.args.get('articleid', type=int, default=1)
    article = next((a for a in articles if a['id'] == article_id), None)
    if article is None:
        return jsonify({"error": "Article not found"}), 404
    return jsonify(article)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')