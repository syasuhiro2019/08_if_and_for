numbers = [34, 432, 1, 99]

total = 0
total = total + numbers[0]
total = total + numbers[1]
total = total + numbers[2]
total = total + numbers[3]

print(total)

total = 0

for number in numbers:
    total = total + number

total = 0

print(total)

for number in numbers:
    total += number

print(total)
