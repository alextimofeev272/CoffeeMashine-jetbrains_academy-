money = int(input())
number_animal = [
    ('chicken', money // 23),
    ("goat", money // 678),
    ("pig", money // 1296),
    ("cow", money // 3848),
    ("sheep", money // 6769),
]
st = ''
if money < 23:
    print(None)
else:
    for i in reversed(number_animal):
        if i[1] != 0 and i[0] == "sheep" or i[1] == 1:
            print(f"{i[1]} {i[0]}")
            break
        elif i[1] != 0:
            print(f"{i[1]} {i[0]}s")
            break
