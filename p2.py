print('Problem 2: Even Fibonacci numbers')

fibTotal = 1
ansTotal = 0
prev = 0

while(fibTotal < 4000000):
  tempTotal = prev + fibTotal
  prev = fibTotal
  fibTotal = tempTotal

  if(fibTotal % 2 == 0):
    ansTotal = ansTotal + fibTotal

print('Answer: ' + str(ansTotal))