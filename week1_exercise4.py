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

# Number 5
#
# num5 = 100
# while not False:
#     if num5 < 0:
#         break
# print('num5 is: ' + str(num5))

numero = 2
while numero < 11:
    print(numero)
    numero += 2
print("Goodbye!")

end = 6
while True:
    for i in range(1, end):
        end += i
    break
print(end)

print("This is before the test")
lol = 6
for i in range(1, lol):
    lol += i
    print(lol)
print("This is after the test")
print(lol)

print('"Hello!"')
for i in range(10, 1, -2):
    print(i)

end = 6
for i in range(1, end):
    end += i
print(end)
