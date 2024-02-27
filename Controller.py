import datetime
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
                break
            
            elif decision.lower() in {"2", "e"}:
                title = input("Введите заголовок заметки: ")
                if not self.model.check_note_by_title(title):
                    print("Заметка с таким заголовком не найдена!")
                    break
                print("Вот эта заметка:")
                self.model.print_note_by_title(title)

                new_title = input("Введите новый заголовок для заметки: ")
                new_content = input("Введите текст заметки: ")
                self.model.edit_note_by_title(title, new_title, new_content)
                print("Заметка отредактирована!")
                print()
                break
            
            elif decision.lower() in {"3", "d"}:
                title = input("Введите заголовок заметки, которая должна быть удалена: ")
                self.model.delete_note_by_title(title)
                print("Заметка была удалена!")
                print()
                break
            
            elif decision.lower() in {"4", "a"}:
                print("Все ваши заметки выведены ниже:\n")
                self.model.print_all_notes()
                print("---------------------------------")
                break
            
            elif decision.lower() in {"5", "f"}:
                title = input("Введите заголовок заметки: ")
                self.model.print_note_by_title(title)
                break

            elif decision.lower() in {"6", "l"}:
                while True:
                    try:
                        date_str = input("Введите начало диапазона в формате ГГГГ-ММ-ДД: ")
                        start_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Неверный формат даты. Пожалуйста, введите дату в правильном формате.")
                        continue
                while True:
                    try:
                        date_str = input("Введите конец диапазона в формате ГГГГ-ММ-ДД: ")
                        end_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Неверный формат даты. Пожалуйста, введите дату в правильном формате.")
                        continue
                print(f'\nЗаметки с {start_date} по {end_date} :')
                self.model.filter_by_date(start_date, end_date)
                print("---------------------------------------")
                break
            
            else: 
                self.model.save_notes()
                print("Сохранение в файл ...")
                break
    
