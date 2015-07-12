# alphabetical substrings

s = 'azcbobobegghakl'
sub = s[0]
longest = ''
for i in s[1:]:
    if i >= sub[-1]:
        sub = sub + i
        if len(sub) > len(longest):
            longest = sub
    else:
        sub = i
print('Longest substring in alphabetical order is: ' + longest)