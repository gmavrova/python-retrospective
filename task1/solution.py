﻿SIGNS = {1: (20, "Водолей", "Козирог"), 2: (19, "Риби", "Водолей"),
         3: (21, "Овен", "Риби"), 4: (21, "Телец", "Овен"),
         5: (21, "Близнаци", "Телец"), 6: (21, "Рак", "Близнаци"),
         7: (22, "Лъв", "Рак"), 8: (23, "Дева", "Лъв"),
         9: (23, "Везни", "Дева"), 10: (23, "Скорпион", "Везни"),
         11: (22, "Стрелец", "Скорпион"), 12: (22, "Козирог", "Стрелец")}


def what_is_my_sign(day, month):
    if day >= SIGNS[month][0]:
        return SIGNS[month][1]
    else:
        return SIGNS[month][2]
