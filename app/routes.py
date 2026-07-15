from flask import Blueprint, render_template, request

from app.documents.generator import create_document_draft
from app.services import save_case

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/create", methods=["GET", "POST"])
def create_document():
    if request.method == "POST":
        data = {
            "document_type": request.form.get("document_type"),
            "name": request.form.get("name"),
            "court": request.form.get("court"),
            "case_number": request.form.get("case_number"),
            "description": request.form.get("description"),
            "evidence": request.form.get("evidence"),
        }

        save_case(data)

        draft = create_document_draft(
            data.get("document_type"),
            data,
        )

        return render_template("draft.html", draft=draft)

    return render_template("create.html")
