class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        filtered = list(filter(lambda x: x[0] == letter, self.products))
        # print("\n".join(filtered))
        return filtered

    def __repr__(self):
        _products = "\n".join(sorted(self.products))
        return f'Items in the {len(self.products)} catalogue:\n{_products}'


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
