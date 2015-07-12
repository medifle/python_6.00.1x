# Lec 3.3, slide 3
# a cleaned up cube root finder

c = int(raw_input('Enter an integer:'))
for r in range(0, abs(c) + 1):
    if r ** 3 >= abs(c):
        break
if r ** 3 == abs(c):
    if c < 0:
        r = -r
    print('Cube root of ' + str(c) + ' is ' + str(r))
else:
    print(str(c) + ' is not a perfect cube.')