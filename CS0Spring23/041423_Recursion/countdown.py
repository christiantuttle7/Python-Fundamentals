# Recursively print countdown from 10-1 and blast off!
# Run it as a script
import time
import sys

def countDown(n):
    if n == 0:
        print('Blast Off!')
        time.sleep(1)
    else:
        print(n)
        time.sleep(1)
        countDown(n-1) # tail recursion
        #print(n)

print(sys.getrecursionlimit())
countDown(10)