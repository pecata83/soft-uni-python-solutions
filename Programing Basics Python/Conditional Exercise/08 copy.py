income = float(input())
score = float(input())
minimum_income = float(input())

social_scholarship = int(minimum_income * 0.35)
high_score_scholarship = 0

if score >= 5.5:
    high_score_scholarship = int(score * 25)


if income > minimum_income and score < 4.5:
    print('You cannot get a scholarship!')

elif income < minimum_income and score >= 5.5:
    if high_score_scholarship > social_scholarship:
        print(
            f'You get a scholarship for excellent results {high_score_scholarship} BGN')
    else:
        print(
            f'You get a Social scholarship {social_scholarship} BGN')

elif income < minimum_income and score < 5.5:
    print(
        f'You get a Social scholarship {social_scholarship} BGN')

elif high_score_scholarship > 0:
    print(
        f'You get a scholarship for excellent results {high_score_scholarship} BGN')

elif income > minimum_income:
    print('You cannot get a scholarship!')
