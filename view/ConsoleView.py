from abc import ABC, abstractmethod

class ConsoleView():

    def is_json_check(self, filename):
        if filename.lower().endswith(".json"):
            return True
        else: return False

    def load_file(self):
        while True:
            filename = input("Введите имя файла в формате .json (с расширением)\n или оставьте пустым (по умолчанию: notes.json): ")
            if filename:
                if len(filename) > 5 and self.is_json_check(filename):
                    return filename
                else:
                    print("Ошибка формата файла. Введите имя файла с расширением .json")
            else: return "notes.json"

    def command_input(self):
        print("Что Вы хотите сделать:")
        print("1. Создать заметку (N)")
        print("2. Редактировать заметку (E)")
        print("3. Удалить заметку (D)")
        print("4. Показать все заметки (A)")
        print("5. Выйти (Q)", end='\n\n')

        decision = input("Ваш выбор: ")

        return desicion