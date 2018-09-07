# Number 1
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)

# Number 3
num1 = 10
while num1 > 3:
    num1 -= 1
    print(num1)

# Number 4
num4 = 10
while True:
    if num4 < 7:
        print('Breaking out of loop')
        break
    print(num4)
    num4 -= 1
print('Outside of loop')
