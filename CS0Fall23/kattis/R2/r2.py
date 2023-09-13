'''
Corin Chepko
9/13/23
Kattis Problem: "Take Two Stones": https://open.kattis.com/problems/r2

Algorithm:
1.) Input a line
2.) Split the line into numbers R1 and S
3.) Calculate R2 = 2S - R1
4.) Output R2
'''

#line = input()
#R1, S = line.split()
R1,S = input().split()

R2 = 2*int(S) - int(R1)

print(R2)