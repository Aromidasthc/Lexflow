from datetime import datetime


def create_document_draft(document_type, data):
    """Create a structured document draft.

    Initial version uses templates. AI integration will be added as a separate layer.
    """

    return {
        "type": document_type,
        "created": datetime.now().isoformat(),
        "content": data,
    }
