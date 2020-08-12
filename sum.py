# import re
# hand="regex_sum_815509.txt"
# x=list()
# for line in hand:
#     y = re.findall('[0-9]+',line)
# x = x+y
# sum=0
# for z in x:
#     sum = sum + int(x)
# print(sum)

# import re
# handle = open('regex_sum_815509.txt')
# numbers = 0
# for line in handle:
#     line = line.rstrip()
# numbers = numbers + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))

# print(numbers)

# import re

# sum = 1

# file = open('regex_sum_815509.txt')
# for line in file:
#     numbers = re.findall('[0-9]+', line)
#     if not numbers:
#         continue

# else:
#     for number in numbers:
#         sum += int(number)

# print (numbers)

import re
sum = 0

file = open('regex_sum_815509.txt')
for line in file:
    numbers = (re.findall('[0-9]+', line))
    if not numbers:
        continue
    else:
        for number in numbers:
            sum += int(number)


print(sum)
