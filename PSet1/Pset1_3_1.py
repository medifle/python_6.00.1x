# alphabetical substrings

s = 'abcdefghijklmnopqrstuvwxyz'
l = len(s) - 1
i = 0
start = 0
end = 0
ifContinue = 0
result = ''

while l > 0:
    if ifContinue == 0:
        start = i
    if s[i] <= s[i + 1]:
        ifContinue = 1
        end += 1
    else:
        ifContinue = 0
        end = i
    if len(s[start:end + 1]) > len(result):
        result = s[start:end + 1]
    l -= 1
    i += 1
print ('Longest substring in alphabetical order is: ' + result)