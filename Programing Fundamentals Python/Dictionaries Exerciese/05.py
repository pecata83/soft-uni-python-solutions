class User:

    def __init__(self, name, license_plate):
        self.name = name
        self.license_plate = license_plate


class Parking:

    def __init__(self, name):
        self.name = name
        self.parking = {}

    def register(self, user):
        if user.name not in self.parking:
            self.parking[user.name] = user
            print(f"{user.name} registered {user.license_plate} successfully")
        else:
            existing_user = self.parking[user.name]
            print(
                f"ERROR: already registered with plate number {existing_user.license_plate}")

    def unregister(self, name):
        if name in self.parking.keys():
            del self.parking[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

    def list_registered(self):
        for k, v in self.parking.items():
            print(f"{v.name} => {v.license_plate}")


soft_uni_parking = Parking("soft_uni_parking")

number = int(input())

for _ in range(number):
    tokens = input().split()
    command = tokens[0]
    name = tokens[1]

    if command == "register":
        license_plate = tokens[2]

        user = User(name, license_plate)
        soft_uni_parking.register(user)
    elif command == "unregister":
        soft_uni_parking.unregister(name)


soft_uni_parking.list_registered()
