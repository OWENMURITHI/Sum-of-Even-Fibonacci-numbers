

firstNum, lastNum = 1, 2
n = 0
sum = 2  # Initialize sum to 2 since 2 is already evem
maxRange = input("Enter the final number")
max = int(maxRange)

while n < max:
    n = firstNum + lastNum
    firstNum = lastNum
    lastNum = n

    if n % 2 == 0:
        sum = sum + n

print(sum)
