from person import Person

class Model:
    def __init__(self):
        self.people = []

    def add(self, name, address, phone):
        person = Person(name, address, phone)
        self.people.append(person)

    def get_all(self):
        return self.people
