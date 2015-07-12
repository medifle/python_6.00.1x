# Lec 2.6, slide 4

x = int(raw_input('Enter your number:'))
if x % 2 == 0:
    if x % 3 == 0:
        print(str(x) + ' is divisible by 2 and 3')
    else:
        print(str(x) + ' is divisible by 2 and not by 3')
elif x % 3 == 0:
    print(str(x) + ' is divisible by 3 and not by 2')
else:
    print(str(x) + ' is not divisible by 2 or 3')