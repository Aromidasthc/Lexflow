from app.database import get_connection


def save_case(data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO cases(document_type, name, description)
        VALUES (?, ?, ?)
        """,
        (
            data.get("document_type"),
            data.get("name"),
            data.get("description"),
        ),
    )

    connection.commit()
    connection.close()
