'''
Corin Chepko
9/13/23
Kattis Problem: "Take Two Stones": https://open.kattis.com/problems/twostones

Algorithm:
1.) Input a number
2.) Check if number is even or odd, if even, Bob wins, odd, Alice wins
3.) Output the name of the winner
'''

number = int(input()) #input the number N, and convert to an integer

if(number%2 == 0): # if N is even, ans=Bob, else ans="Alice"
    ans = "Bob"
else:
    ans = "Alice"

print(ans)
