from model.JsonModel import NoteManager
from view.ConsoleView import ConsoleView
from Controller import Controller

def main():
    view = ConsoleView()
    model = NoteManager(view.load_file())
    controller = Controller(view,model)

    while True:

        controller.run()
        
        resume = input("Продолжить работу?\nПродолжить: (д/y), Выход: (н/q) \n")

        if resume.lower() in {"д","y","да","yes"}:
            continue
        else:
            print("Выход...")
            break

if __name__ == '__main__':
    main()
    