class Stack:
    def __init__(self, items):
        self.items = items

    def append(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


text = list(input())
my_stack = Stack(text)
reversed_text = ""

while my_stack.size() > 0:
    reversed_text += my_stack.pop()

print(reversed_text)
