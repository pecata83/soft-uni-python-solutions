nylon_needed = int(input())
paint_needed = int(input())
white_spirit_needed = int(input())
work_hours_needed = int(input())

nylon_price = (nylon_needed + 2) * 1.5
paint_price = (paint_needed * 1.1) * 14.5
white_spirit_price = white_spirit_needed * 5

materials_price = nylon_price + paint_price + white_spirit_price + 0.4

work_force_price = work_hours_needed * (materials_price * 0.3)

print(f"Total expenses: {materials_price + work_force_price:.2f} lv.")
