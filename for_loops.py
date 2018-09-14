misuma = 0
print("Suma before FOR loop: " + str(misuma))

for i in range(5, 11, 2):
    print("Suma after FOR loop: " + str(misuma))
    misuma = misuma + i
    print("Suma after ADD 1 inside the loop: " + str(misuma))
    if misuma == 5:
        break

print("Suma after FOR loop is done: " + str(misuma))
