income = float(input())
score = float(input())
minimum_income = float(input())

social_scholarship = int(minimum_income * 0.35)
high_score_scholarship = int(score * 25)

if score >= 5.5:

    if income < minimum_income:
        if high_score_scholarship > social_scholarship:
            print(
                f'You get a scholarship for excellent results {high_score_scholarship} BGN')
        else:
            print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        print(
            f'You get a scholarship for excellent results {high_score_scholarship} BGN')

elif score > 4.5:

    if income < minimum_income:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        print('You cannot get a scholarship!')

elif score <= 4.5:
    print('You cannot get a scholarship!')
