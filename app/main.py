def get_human_age(cat_age: int, dog_age: int) -> list:
    count_human_age_per_cat = 0
    count_human_age_per_dog = 0
    if cat_age >= 15:
        count_human_age_per_cat += 1
        cat_age -= 15
        if cat_age >= 9:
            count_human_age_per_cat += 1
            cat_age -= 9
            if cat_age > 0:
                count_human_age_per_cat += cat_age // 4

    if dog_age >= 15:
        count_human_age_per_dog += 1
        dog_age -= 15
        if dog_age >= 9:
            count_human_age_per_dog += 1
            dog_age -= 9
            if dog_age > 0:
                count_human_age_per_dog += dog_age // 5

    return [int(count_human_age_per_cat), int(count_human_age_per_dog)]
