import math
print('Problem 3: Largest prime factor')

fibTotal = 1
ansTotal = 0
prev = 0

def IsPrime(x:int):
  factor = 0
  result = True

  if x > 1:
    for i in range(1,x+1):
      
      if x % i == 0:
        factor = factor + 1
        
      if factor > 2:
        result = False
        break
  else:
    result = False
  
  return result

num = 600851475143 
largestPrime = 0
j = 0

for i in range(1, int(math.sqrt(num))+1):
  if num % i == 0:

    j = int(num/i)

    if (IsPrime(j) and largestPrime < j):
      largestPrime = j

    if IsPrime(i) and largestPrime < i:
      largestPrime = i

print('Answer: ' + str(largestPrime))
print('Done')