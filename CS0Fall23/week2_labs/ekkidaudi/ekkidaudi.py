"""
Math and Variables Lab
By: FIXME
CSCI 110 Lab
Date: FIXME
 
Read and solve: EKKIDAUDI - https://open.kattis.com/problems/ekkidaudi 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two strings named line1_a and line1_b using .split('|') method
  3. Read second line and split into two new varibles, line2_a and line2_b 
  4. Concatenate the strings into a string named answer
  5. Print the answer
"""
 
def main():
  """Main function that solves the problem
  """

  # Input 1st line of data into varible "line"
  line = input()

  # Split the line into two strings named line1_a and line1_b using .split('|') method
  line1_a, line1_b = line.split('|')

  # check to see if the data is split correctly
  print(f'{line1_a=}, {line1_b=}') # FIXME 1: comment/remove this line before submitting to Kattis
  
  # FIXME 2: Read second line into line variable
  
  # FIXME 3: Split into two new varibles, line2_a and line2_b
  
  # check to see if the data is split correctly
  print(f'{line2_a=}, {line2_b=}') # FIXME 4: comment/remove this line before submitting to Kattis
  
  # FIXME 5: Concatenate the strings into a string named answer: 
  # Add the a lines, then a space, then add the b lines
  answer = 
  
  # FIXME 6: print the answer
  

main() # call main function
