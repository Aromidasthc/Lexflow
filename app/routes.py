from flask import Blueprint, render_template, request

from app.documents.generator import create_document_draft

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/create", methods=["GET", "POST"])
def create_document():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "court": request.form.get("court"),
            "case_number": request.form.get("case_number"),
            "description": request.form.get("description"),
            "evidence": request.form.get("evidence"),
        }

        draft = create_document_draft(
            request.form.get("document_type"),
            data,
        )

        return render_template("draft.html", draft=draft)

    return render_template("create.html")
