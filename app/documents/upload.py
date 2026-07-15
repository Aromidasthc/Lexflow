ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}


def validate_file(filename):
    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()
    return extension in ALLOWED_EXTENSIONS
