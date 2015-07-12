# Lec 3.1, slide 2

x = int(raw_input('Enter your number:'))
ans = 0
i = x
while i > 0:
    ans = ans + x
    i = i - 1
print(str(x) + '*' + str(x) + '=' + str(ans))