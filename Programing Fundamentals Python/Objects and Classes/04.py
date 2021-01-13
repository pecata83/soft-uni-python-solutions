class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1

        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        capitalized_name = ""
        animals_names = ""

        if species == "mammal":
            capitalized_name = "Mammals"
            animals_names = ", ".join(self.mammals)
        elif species == "fish":
            capitalized_name = "Fishes"
            animals_names = ", ".join(self.fishes)
        elif species == "bird":
            capitalized_name = "Birds"
            animals_names = ", ".join(self.birds)

        print(f"{capitalized_name} in {self.name}: {animals_names}")
        print(f"Total animals: {self.__animals}")


zoo = Zoo(input())
number = int(input())

for n in range(number):
    specie, animal = input().split()
    zoo.add_animal(specie, animal)


zoo.get_info(input())
