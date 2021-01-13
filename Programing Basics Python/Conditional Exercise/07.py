top_time = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())


seconds_needed = distance_in_meters * seconds_per_meter
extra_seconds = distance_in_meters // 15
extra_seconds *= 12.5

total_seconds = seconds_needed + extra_seconds

if total_seconds < top_time:
    print(
        f'Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.')
elif total_seconds >= top_time:
    print(
        f'No, he failed! He was {total_seconds - top_time:.2f} seconds slower.')
