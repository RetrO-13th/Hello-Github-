# Mohamad Sadra Gholami ---------- Answer Q3
# Tarbiat 111
# please read comments

import math # using math module for square of numbers -- fast result

numList = [] # list of result for print

def primesFinder(x): # prime numbers finder func
    global numList 

    while x % 2 == 0: # for numbers "have number 2" in it
        numList.append(2)
        x = x / 2
    

    for i in range(3, int(math.sqrt(x)) + 1, 2): # for numbers up to "number 3"
        while x % i == 0:
            numList.append(i)
            x = x / i

    if x > 2: # for numbers under "number 2" -- like: num 1
        numList.append(int(x))

inp = int(input()) # this input gets "an int number" -- for example: 12

primesFinder(inp) 

finalList = set() # set of prime numbers
for p in numList: 
    pri = numList.count(p) # primes counter
    finalList.add('{}**{}'.format(p, pri)) # add prime numbers with output format

formatList = list(finalList) 
for u in finalList:  # sum all the prime together and final output -- for example: 2**2 + 3**1
    print(u, end=' ')
    if u != formatList[(len(finalList) - 1)]:
        print('+', end=' ')

# Thanks -- sorry about my English :) 