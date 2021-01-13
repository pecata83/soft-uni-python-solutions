import math
hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60 + minutes + 15

hours = math.floor(time_in_minutes / 60)
minutes = time_in_minutes % 60

if hours == 24:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')

else:
    print(f'{hours}:{minutes}')
