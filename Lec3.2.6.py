# Lec 3.2, slide 6
# Find the cube root of a perfect cube

c = int(raw_input('Enter an integer:'))
r = 0
while r ** 3 < abs(c):
    r += 1
if (r ** 3) != abs(c):
    print(str(c) + ' is not a perfect cube')
elif c < 0:
    r = -r
    print('Cube root of ' + str(c) + ' is ' + str(r))