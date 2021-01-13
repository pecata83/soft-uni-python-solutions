people_in_jury = int(input())
presentation_name = input()
total_presentations = 0
total_scores = 0

while presentation_name != "Finish":
    scores = 0
    for n in range(1, people_in_jury + 1):
        scores += float(input())

    final_score = scores / people_in_jury

    print(f"{presentation_name} - {final_score:.2f}.")
    total_presentations += 1
    total_scores += final_score
    presentation_name = input()
else:
    print(
        f"Student's final assessment is {total_scores / total_presentations:.2f}.")
