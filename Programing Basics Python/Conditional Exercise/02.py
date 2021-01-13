number = int(input())
points = 0

if number <= 100:
    points += 5

elif number > 100 and number <= 1000:
    points = number * 0.2

elif number > 1000:
    points = number * 0.1

if number % 2 == 0:
    points += 1

# Judge system tests bug
# elif number % 5 == 0:
#     points += 2
elif number % 10 == 5:
    points += 2

print(points)
print(number + points)
