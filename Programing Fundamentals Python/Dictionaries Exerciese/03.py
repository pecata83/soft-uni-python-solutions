from collections import defaultdict

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

inventory = defaultdict(int)


def optain_item_by_material(material):
    inventory[material] -= 250

    print(legendary_items[material], "obtained!")

    key_materials = {
        "shards": inventory["shards"],
        "fragments": inventory["fragments"],
        "motes": inventory["motes"]
    }

    del inventory["shards"]
    del inventory["fragments"]
    del inventory["motes"]

    sorted_key_materials = dict(
        sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
    )

    junk_materials = dict(
        sorted(inventory.items(), key=lambda x: (x[0]))
    )

    for k, v in sorted_key_materials.items():
        print(f"{k}: {v}")

    for k, v in junk_materials.items():
        print(f"{k}: {v}")


while True:
    tokens = input().split(" ")
    winning_material = None

    for i in range(1, len(tokens), 2):
        material = tokens[i].lower()
        value = int(tokens[i - 1])
        inventory[material] += value

        winning_material_list = list(
            filter(lambda x: x[1] >= 250 and x[0] in legendary_items, inventory.items()))
        # winning_material = max(inventory)

        if len(winning_material_list) > 0:
            winning_material = winning_material_list[0][0]
            break

    if winning_material:
        optain_item_by_material(winning_material)
        break
