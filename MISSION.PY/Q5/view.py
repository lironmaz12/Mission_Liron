class View:
    def get_input(self, prompt):
        return input(prompt)

    def show_message(self, message):
        print(message)

    def show_people(self, people):
        print("\n--- People List ---")
        for person in people:
            print(f"Name: {person.name}, Address: {person.address}, Phone: {person.phone}")
        print("------------------")
