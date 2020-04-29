column = int(input())
row = int(input())

if column != 8 and column != 1 and row != 8 and row != 1:
    print(8)
elif column in (1, 8) and row in (1, 8):
    print(3)
else:
    print(5)
