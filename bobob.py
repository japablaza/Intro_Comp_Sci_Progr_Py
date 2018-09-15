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
