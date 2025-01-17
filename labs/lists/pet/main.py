"""
Lists and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - Pet: https://open.kattis.com/problems/pet 

Algorithm steps:
		1. Create a list to store the total scores of each contestant
		2. Repeat 5 times:
      1. Read the input line
      2. Split the line into a list of numbers
      3. Convert the list of strings into a list of ints
      4. Sum the list of ints
      5. Append the sum to the list of scores
    3. Find the max score in the list of scores
    4. Find the index of the max score in the list of scores
    5. Print the index of the max score + 1 and the max score
"""

import sys
from typing import List

def main():
  """Main function that solves the problem
  """
  # step 1. create a list to store the total scores of each contestant
  scores = []
  # FIXME 1 - repeat step 2-4 5 times
  # FIXME 2 - read the input line as a list of integers using get_data function
  # FIXME 3 - find the sum of scores using list_sum function
  # FIXME 4 - append the sum to the list of scores
  # FIXME 5 - print the final output calling answer function

def get_data():
  """Reads the data from std input and returns it as a list of ints
  Args:
      None
  Returns:
      List[int]: list of ints
  """
  str_nums = input().split() # list of string numbers
  # FIXME 6: convert str_nums int a list of ints and return it
  pass

def list_sum(numbers: List[int]):
  """Finds and returns sum of the numbers in the list
  Args:
      numbers: List[int]: # takes a list of numbers as a parameter

  Returns:
      int: sum of the numbers in the list
  """
  # FIXME 7: find the sum of the numbers in the list and return it
  ans = 0
  return ans

def answer(scores: List[int]):
  """Returns the index of the max score + 1 and the max score as a string

  Args:
      scores (List[int]): List of 5 contestants scores
  """
  max_score = max(scores)
  index = scores.index(max_score)
  # FIXME 8: return the index+1 and the max number in the list as a string
  pass

if __name__ == "__main__":
  main()
