print('Problem 1: Multiples of 3 and 5')

total = 0
for i in range(0,1000):
  if i % 5 == 0 or i % 3 == 0:
    total = total + i
print('Answer: ' + str(total))