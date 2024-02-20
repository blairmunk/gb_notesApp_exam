
class Note:
    '''Represents a note, with a name.'''
    # A class variable, counting the number of robots
    num_of_notes = 0
    def __init__(self, name):
        '''Initializes the data.'''
        self.note_id = note_id
        self.caption = ''
        self.body = ''
        self.name = name
        self.name = name
        self.name = name
        print(f'(Initializing {self.name})')
        # When this person is created, the robot
        # adds to the population
        num_of_notes += 1
    def delete_note(self):
        print('Заметка удалена')
        num_of_notes -= 1
        if num_of_notes == 0:
            print('Больше заметок нет')
    def say_hi(self):
        '''Greeting by the robot.
        Yeah, they can do that.'''
        print(f'Greetings, my masters call me {self.name}.')
    @classmethod
    def how_many(cls):
        '''Prints the number of notes'''
        print(f'Всего {cls.num_of_notes} заметок.')
droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()
droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()
print('Robots can do some work here.')
print('Robots have finished their work. So lets destroy them.')
droid1.die()
droid2.die()
Robot.how_many()