def life_in_weeks(age):
    age_until_90 = 90 - age
    weeks_left = age_until_90 * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(29)