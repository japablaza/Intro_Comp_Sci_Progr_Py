s = 'azcbobobegghakl'
bob = 'bob'
count = 0
start = 0
end = 2

while True:
    if bob == s[start:end]:
        count = count + 1
        start = start + 1
        end = end + 1
    break
print(count)
