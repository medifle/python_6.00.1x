# Lec 3.4, slide 4
# convert decimal float to binary

a = float(raw_input('Enter a decimal number:'))

if a < 0:
    ifNeg = True
    a = -a
else:
    ifNeg = False

p = 1
while (a * (2 ** p)) % 1 != 0:
    p += 1
b = int(a * (2 ** p))

result = ''
if a == 0:
    result = 0.0
else:
    while b > 0:
        result = str(b % 2) + result
        b = b / 2
    result = float(result) / (10 ** p) # precision problem

if ifNeg:
    result = -result

print result