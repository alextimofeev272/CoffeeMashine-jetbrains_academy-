summa = 0
summa_sq = 0
while True:
    a = int(input())
    summa_sq += a**2
    summa += a
    if summa == 0:
        print(summa_sq)
        break
