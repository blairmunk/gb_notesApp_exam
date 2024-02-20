
class Note:
    '''Represents a note, with a name.'''
    # A class variable, counting the number of robots
    note_id = 0
    num_of_notes = 0
    def __init__(self, caption):
        '''Initializes the data.'''
        self.note_id = Note.note_id
        self.caption = caption
        self.body = ''
        print(f'(Создана заметка {self.caption})')
        # When this person is created, the robot
        # adds to the population
        Note.num_of_notes += 1
        Note.note_id += 1

    def get_id(self):
        return self.note_id

    def get_caption(self):
        return self.caption

    def get_body(self):
        return self.body

    def set_caption(self, caption):
        self.caption = caption

    def set_body(self, body):
        self.body = body

    def delete_note(self):
        print('Заметка удалена')
        num_of_notes -= 1
        if num_of_notes == 0:
            print('Больше заметок нет')

    @classmethod
    def how_many(cls):
        '''Prints the number of notes'''
        print(f'Всего {cls.num_of_notes} заметок.')

note1 = Note('Жопу с мылом')
note1 = Note('Жопу с мыл')
Note.how_many()
print(note1.get_id())
print(note1.get_id())