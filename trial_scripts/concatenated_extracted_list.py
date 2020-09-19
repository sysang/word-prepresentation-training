a1 = [1, 2, 3, 4, 5, 6]
s = ''
for i in a1:
    s += '>|<' + str(i)

s = s[3:]
print(s)

for i in s.split('>|<'):
    print(i)

