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
                if not self.model.check_note_by_title(title):
                    print("Заметка с таким заголовком не найдена!")
                    continue
                print("Вот эта заметка:")
                self.model.print_note_by_title(title)
                print()

                new_title = input("Введите новый заголовок для заметки: ")
                new_content = input("Введите текст заметки: ")
                self.model.edit_note_by_title(title, new_title, new_content)
                print("Заметка отредактирована!")
                print()
                continue
            
            elif decision.lower() in {"3", "d"}:
                title = input("Введите заголовок заметки, которая должна быть удалена: ")
                self.model.delete_note_by_title(title)
                continue
            
            elif decision.lower() in {"4", "a"}:
                print("Все ваши заметки выведены ниже")
                self.model.print_all_notes()
                continue
            
            elif decision.lower() in {"5", "f"}:
                title = input("Введите заголовок заметки: ")
                self.model.print_note_by_title(title)
                continue
            
            else: 
                print("Выход. Пока!")
                break
    
