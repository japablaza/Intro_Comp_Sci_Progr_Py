varA = 12
varB = 'B'
varC = type('text')

if (type(varA) == varC or (type(varB) == varC)):
    print('string involved')

# if (type(varA) or type(varB)) == isinstance('text'):
#     print('string involved')

if varA > len(varB):
    print('bigger')

# if (varA == varB):
#     print('equal')

if varA < len(varB):
    print('smaller')
