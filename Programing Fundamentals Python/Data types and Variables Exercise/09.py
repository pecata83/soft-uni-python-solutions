total_snow_balls = int(input())

hightest_snowball_coefficient = 0

snowball_snow_highest = 0
snowball_time_highest = 0
snowball_quality_highest = 0

for snowball in range(total_snow_balls):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_coefficient = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_coefficient > hightest_snowball_coefficient:
        hightest_snowball_coefficient = snowball_coefficient
        snowball_snow_highest = snowball_snow
        snowball_time_highest = snowball_time
        snowball_quality_highest = snowball_quality


print(
    f"{snowball_snow_highest} : {snowball_time_highest} = {int(hightest_snowball_coefficient)} ({snowball_quality_highest})"
)
