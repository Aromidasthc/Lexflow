from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DocumentFile:
    case_id: int
    original_name: str
    stored_name: str
    file_type: str
    file_path: str
    created_at: datetime = field(default_factory=datetime.now)
