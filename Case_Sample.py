# Case Sample
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

print('='*23)

# Test 1
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break  # I added this break


print('='*23)

# Test 3
count = 0
phrase = 'hello, world'
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))

print('='*23)

# test 4
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))

print('='*23)

# test 5
count = 0
for iteration in range(5):
    count += 12
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
