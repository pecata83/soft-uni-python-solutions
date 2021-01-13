class Person:

    def __init__(self, name):
        self.name = name


class Party:

    def __init__(self):
        self.people = []

    def invite(self, name):
        person = Person(name)
        self.people.append(person)

    def list_attendees(self):
        print(f"Going: {', '.join([p.name for p in self.people])}")

    def total_attendees(self):
        print(f"Total: {len(self.people)}")


party = Party()

while True:
    comand = input()

    if comand == "End":
        break

    name = comand
    party.invite(name)

party.list_attendees()
party.total_attendees()
