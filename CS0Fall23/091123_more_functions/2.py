'''
Playing with libraries
'''

import math
import time
import random

num1 = 5.6
num2 = 10
degrees = 30

radians = math.radians(degrees)
sin_ans = math.sin(radians)
answer = "{} degrees = {} radians.\nThe sin({}) = {}".format(degrees, radians, degrees, sin_ans)

print(answer)
# To sleep the program for x seconds, time.sleep(x)
time.sleep(3)
print(time.localtime())
print(answer)

rand_num = random.random()
rand_1_10 = rand_num*10
int_rand_num = int(rand_1_10)
print(int_rand_num)
print(int(random.random()*10))