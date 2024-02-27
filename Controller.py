from view.ConsoleView import ConsoleView
from model.JsonModel import NoteManager

class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def run(self):

        while True:
            decision = self.view.command_input()
            
            if decision.lower() in {"1", "n"}:
                title = input("Введите заголовок заметки: ")
                content = input("Введите текст заметки: ")
                self.model.add_note(title, content)
                continue
            elif decision.lower() in {"2", "e"}:
                title = input("Введите заголовок заметки: ")
                new_title = input("Введите новый заголовок для заметки: ")
                new_content = input("Введите текст заметки: ")
                self.model.edit_note(title, new_title, new_content)
                continue
            elif decision.lower() in {"3", "d"}:
                title = input("Введите заголовок заметки, которая должна быть удалена: ")
                self.model.delete_note(title)
                continue
            elif decision.lower() in {"4", "a"}:
                self.model.print_all_notes()
                continue
            else: 
                print("Выход. Пока!")
                break
    
