palabra = 'asdaslkdjbobjlksjdbobobasdsad'

inicio = 0
fin = inicio + 2
contador = 0

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

while True:
    for i in palabra:
        if fin - 1 == len(palabra):
            break
        if palabra[inicio:fin] == 'bob':
            count = count + 1
            inicio = inicio + 1
            
