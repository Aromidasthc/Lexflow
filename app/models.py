from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Case:
    title: str
    document_type: str
    created_at: datetime = field(default_factory=datetime.now)
    answers: dict = field(default_factory=dict)


@dataclass
class Document:
    document_type: str
    content: str
    created_at: datetime = field(default_factory=datetime.now)
