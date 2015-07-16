# Lec 3.4, slide 4
# convert decimal float to binary

# Ask to input a decimal float number
a = float(raw_input('Enter a decimal number:'))

if a < 0:
    ifNeg = True
    a = -a
else:
    ifNeg = False

p = 1
# Convert the input float into integer by multiplying 2 iteratively
# As long as the input float remains a fraction, add p by 1
while (a * (2 ** p)) % 1 != 0:
    p += 1
    
b = int(a * (2 ** p))

# The following block converts decimal int into binary counterpart
result = ''
if a == 0:
    result = 0.0
else:
    while b > 0:
        result = str(b % 2) + result
        b = b / 2
        
    # Move dot to proper place
    result = float(result) / (10 ** p)

if ifNeg:
    result = -result

print result
