date = {1: 20, 2: 19, 3: 21, 4: 21, 5: 21, 6: 21,
        7: 21, 8: 23, 9: 23, 10: 23, 11: 22, 12: 22}
sign = {1: "Водолей", 2: "Риби", 3: "Овен",
        4: "Телец", 5: "Близнаци", 6: "Рак",
        7: "Лъв", 8: "Дева", 9: "Везни",
        10: "Скорпион", 11: "Стрелец", 12: "Козирог"}


def what_is_my_sign(day, month):
    if day >= date[month]:
        return sign[month]
    else:
        index = month - 1
        if index == 0:
            index = 12
        return sign[index]
