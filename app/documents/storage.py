import os
import uuid

UPLOAD_FOLDER = "storage/documents"


def save_document(file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    extension = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{extension}"
    path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(path)

    return path
