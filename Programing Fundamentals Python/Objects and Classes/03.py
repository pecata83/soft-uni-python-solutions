class Email:
    def __init__(self, sender, receiver, content, is_send=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


class Emails:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        return [e.get_info() for e in self.emails]

    def send_emails(self, indexes):
        for i in indexes:
            self.emails[i].send()


emails = Emails()

while True:
    command = input()

    if command == "Stop":
        break

    tokens = command.split()
    email = Email(tokens[0], tokens[1], tokens[2])
    emails.add_email(email)

emails_to_send = [int(i) for i in input().split(", ")]

emails.send_emails(emails_to_send)

print("\n".join(emails.list_emails()))
