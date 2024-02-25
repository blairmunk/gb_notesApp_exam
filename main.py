#from interfaces.InterfaceNotes import InterfaceNotes
from model.JsonModel import NoteManager
from view.ConsoleView import ConsoleView

def main():
    # Пример использования
    note_manager = NoteManager("notes.json")

    # Добавление заметок
    note_manager.add_note("Заголовок заметки 1", "Содержимое заметки 1")
    note_manager.add_note("Заголовок заметки 2", "Содержимое заметки 2")
    note_manager.add_note("Заголовок заметки 3", "Содержимое заметки 3")

    note_manager.edit_note_by_title("Заголовок заметки 2", "Новый заголовок", "Новое содержимое")


    # Удаление заметки по заголовку
    note_manager.delete_note_by_title("Заголовок заметки 2")

    # Сохранение и обновление JSON-файла
    note_manager.save_notes()

    # Вывод всех заметок на консоль
    note_manager.print_all_notes()

if __name__ == '__main__':
    main()
    