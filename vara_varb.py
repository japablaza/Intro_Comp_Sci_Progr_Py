varA = 7
varB = 8

# Moving integer to string
if ((type(varA) == str) or (type(varB) == str)):
    print('string involved')
    # if type(varA) != str:
    #     varA = str(varA)
    #     if varA > varB:
    #         print('bigger')
    #     elif varA == varB:
    #         print("equal")
    #     elif varA < varB:
    #         print("smaller2")
    # if type(varB) != str:
    #     varB = str(varB)
    #     if varA > varB:
    #         print("bigger")
    #     elif varA == varB:
    #         print("equal")
    #     elif varA < varB:
    #         print("smaller3")

# Testing if varA and varB are string
# if (isinstance(varA, str) and isinstance(varB, str)):
if (type(varA) == str) and (type(varB) == str):
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")

# Testing if varA and varB are integer
# if (isinstance(varA, int) and isinstance(varB, int)):
if (type(varA) == int) and (type(varB) == int):
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")
