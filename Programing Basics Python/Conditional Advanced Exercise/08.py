exam_hour = int(input())
exam_minutes = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
arriving_time_in_minutes = hour_of_arriving * 60 + minutes_of_arriving

time_difference_in_minutes = exam_time_in_minutes - arriving_time_in_minutes

student_timing = ""

if time_difference_in_minutes < 0:
    student_timing = "Late"

elif 0 <= time_difference_in_minutes <= 30:
    student_timing = "On time"

elif time_difference_in_minutes > 30:
    student_timing = "Early"


def convert_minutes_to_hours(minutes):
    _minutes = abs(minutes)
    if _minutes < 60:
        return _minutes

    elif _minutes >= 60:
        _hours = _minutes // 60
        _minutes = _minutes % 60
        if _minutes < 10:
            _minutes = '{:02}'.format(_minutes)
        return f"{_hours}:{_minutes}"


print(student_timing)

if time_difference_in_minutes > 0:
    if time_difference_in_minutes < 60:
        print(
            f"{convert_minutes_to_hours(time_difference_in_minutes)} minutes before the start")
    elif time_difference_in_minutes >= 60:
        print(
            f"{convert_minutes_to_hours(time_difference_in_minutes)} hours before the start")

elif time_difference_in_minutes < 0:
    if time_difference_in_minutes > -60:
        print(
            f"{convert_minutes_to_hours(time_difference_in_minutes)} minutes after the start")
    elif time_difference_in_minutes <= -60:
        print(
            f"{convert_minutes_to_hours(time_difference_in_minutes)} hours after the start")
