numbers = [int(x) for x in input().split()]
sum = 0
for i in numbers:
    sum += i
print(sum / len(numbers))
