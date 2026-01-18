from view import View
from model import Model

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):
        while True:
            self.view.show_message("\nOptions: [1] Add Person  [2] Show People  [3] Exit")
            choice = self.view.get_input("Choose an option: ")

            if choice == "1":
                name = self.view.get_input("Enter name: ")
                address = self.view.get_input("Enter address: ")
                phone = self.view.get_input("Enter phone number: ")
                self.model.add(name, address, phone)
                self.view.show_message("Person added successfully.")

            elif choice == "2":
                people = self.model.get_all()
                if people:
                    self.view.show_people(people)
                else:
                    self.view.show_message("No people in the list yet.")

            elif choice == "3":
                self.view.show_message("Exiting program.")
                break

            else:
                self.view.show_message("Invalid option. Try again.")
