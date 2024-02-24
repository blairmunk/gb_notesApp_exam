from abc import ABC, abstractmethod

class InterfaceNotes(ABC):
    '''
    Интерфейс для работы с заметками. 
    '''

    @abstractmethod
    def load_notes():
        pass

    @abstractmethod
    def save_notes():
        pass

    @abstractmethod
    def add_note():
        pass
    
    @abstractmethod
    def delete_note_by_title():
        pass

    @abstractmethod
    def edit_note():
        pass

    @abstractmethod
    def get_note_by_title():
        pass

    @abstractmethod
    def print_all_notes():
        pass

