import uuid
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.id = str(uuid.uuid4())
        self._title = title
        self._content = content
        self._created_at = datetime.now()
        self._modified_at = datetime.now()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, value):
        self._created_at = value
    
    @property
    def modified_at(self):
        return self._modified_at

    @modified_at.setter
    def modified_at(self, value):
        self._modified_at = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }