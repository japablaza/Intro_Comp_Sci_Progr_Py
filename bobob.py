# palabra = 'asdaslkdjbobjlksjdbobobasdsad'
# inicio = 0
# fin = inicio + 2
# contador = 0

# First try.... did not work
# while True:
#     if palabra[inicio:fin] == 'bob':
#         contador = contador + 1
#         inicio = inicio + 1
#     else:
#         inicio = inicio + 1
# .
# print(contador)
# .

# while True:
#     for i in palabra:
#         if fin - 1 == len(palabra):
#             break
#         if palabra[inicio:fin] == 'bob':
#             count = count + 1
#             inicio = inicio + 1
'''
Problem 2
0.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string
'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print
'''
count = 0
s = 'asdaslkdjbobjlksjdbobobasdsad'
inicio = 0
bob = 0
for inicio in range(len(s)):
    bob = inicio + 3
    print(s[inicio:bob])
    if s[inicio:bob] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))
