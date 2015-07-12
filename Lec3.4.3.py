# Lec 3.4, slide 3
# convert decimal to binary

num = int(raw_input('Enter a decimal number:'))
result = '' 
nega = False

if num < 0:
    num = -num
    nega = True
if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num = num / 2

if nega:
    result = '-' + result

print (result)