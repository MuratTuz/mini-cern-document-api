from flask import Blueprint, jsonify, request
from .database import db
from .models import Document

main = Blueprint("main", __name__)

@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@main.route("/documents", methods=["GET"])
def get_documents():
    documents = Document.query.order_by(Document.id.asc()).all()
    return jsonify([doc.to_dict() for doc in documents])

@main.route("/documents/<int:document_id>", methods=["GET"])
def get_document(document_id):
    document = Document.query.get(document_id)

    if not document:
        return jsonify({"error": "Document not found"}), 404

    return jsonify(document.to_dict())

@main.route("/documents", methods=["POST"])
def create_document():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    author = data.get("author")
    description = data.get("description")

    if not title or not author:
        return jsonify({"error": "title and author are required"}), 400

    document = Document(
        title=title,
        author=author,
        description=description
    )

    db.session.add(document)
    db.session.commit()

    return jsonify(document.to_dict()), 201

@main.route("/documents/<int:document_id>", methods=["PUT"])
def update_document(document_id):
    document = Document.query.get(document_id)

    if not document:
        return jsonify({"error": "Document not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    title = data.get("title")
    author = data.get("author")
    description = data.get("description")

    if title is not None:
        document.title = title

    if author is not None:
        document.author = author

    if description is not None:
        document.description = description

    db.session.commit()

    return jsonify(document.to_dict())

@main.route("/documents/<int:document_id>", methods=["DELETE"])
def delete_document(document_id):
    document = Document.query.get(document_id)

    if not document:
        return jsonify({"error": "Document not found"}), 404

    db.session.delete(document)
    db.session.commit()

    return jsonify({"message": f"Document {document_id} deleted successfully"})