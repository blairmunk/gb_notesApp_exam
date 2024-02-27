import json
from datetime import datetime
from .InterfaceNotes import InterfaceNotes
from .Note import Note

class NoteManager(InterfaceNotes):
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                notes = []
                for note_data in data:
                    note = Note(
                        note_data["title"],
                        note_data["content"]
                    )
                    note.id = note_data["id"]
                    note.created_at = datetime.fromisoformat(note_data["created_at"])
                    notes.append(note)
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            data = [note.to_dict() for note in self.notes]
            json.dump(data, file, ensure_ascii=False)

    def check_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return True
        return False

    def title_exist_msg_check(self,title):
        if self.check_note_by_title(title):
            print(f'Заметка с заголовком "{title}" уже существует')
            return True
        else: return False


    def add_note(self, title, content):
        if not self.title_exist_msg_check(title):
            note = Note(title, content)
            self.notes.append(note)
            self.save_notes()
        print()
        print(f'Заметка c заголовком "{title}" создана!')
        print()

    def delete_note_by_title(self, title):
        self.notes = [note for note in self.notes if note.title != title]
        self.save_notes()

    def get_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None
    
    def print_note_by_title(self,title):
        if self.check_note_by_title(title):
            note = self.get_note_by_title(title)
        else: 
            print("Заметка с таким заголовком не найдена!")
            return 
        print(f"Created_at: {note.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"Modified_at: {note.created_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"ID: {note.id}")
        print(f"Title: {note.title}")
        print(f"Content: {note.content}")
        print()
        

    def edit_note_by_title(self, title, new_title, new_content):
        note = self.get_note_by_title(title)
        if not self.title_exist_msg_check(new_title):
            note.title = new_title
            note.modified_at = datetime.now()
            note.content = new_content
        


    def print_all_notes(self):
        for note in self.notes:
            print(f"Created_at: {note.created_at.strftime('%Y-%m-%d %H:%M')}")
            print(f"ID: {note.id}")
            print(f"Title: {note.title}")
            print()

