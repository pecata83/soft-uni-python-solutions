cells = input().split("#")
amount_of_water = int(input())

total_efford = 0
total_fire = 0

print("Cells:")

for cell_str in cells:
    cell = cell_str.split(" = ")
    cell_type = cell[0]
    cell_value = int(cell[1])
    is_valid = False

    if cell_type == "High" and 81 <= cell_value <= 125:
        is_valid = True
    elif cell_type == "Medium" and 51 <= cell_value <= 80:
        is_valid = True
    elif cell_type == "Low" and 1 <= cell_value <= 50:
        is_valid = True

    if is_valid and amount_of_water - cell_value >= 0:
        print(f" - {cell_value}")
        total_fire += cell_value
        total_efford += cell_value * 0.25
        amount_of_water -= cell_value

print(f"Effort: {total_efford:.2f}")
print(f"Total Fire: {total_fire}")