#from interfaces.InterfaceNotes import InterfaceNotes
from model.JsonModel import NoteManager
from view.ConsoleView import ConsoleView
from Controller import Controller

def main():
    view = ConsoleView()
    model = NoteManager(view.load_file())
    controller = Controller(view,model)

    controller.run()

if __name__ == '__main__':
    main()
    