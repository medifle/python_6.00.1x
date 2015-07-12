# counting bobs

# s = 'azcbobobobbobegghakl'
i = s.find('bob')
l = len(s) - i - 1
total = 0
for a in range(i, len(s) - 1):
    if s[a:a+3] == 'bob':
        total += 1
print ('Number of times bob occurs is: ' + str(total))