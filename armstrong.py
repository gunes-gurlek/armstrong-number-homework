# Check Armstrong Numbers Between Two Integers

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    temp = num
    sum = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if num == sum:
        print(num)