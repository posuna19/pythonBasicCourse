"""
Imagine one of your colleagues has written a Python script that's failing to run correctly. They're asking for your
help to debug it. In this lab, you'll look into why the script is crashing and apply the problem-solving steps
that we've already learned to get information, find the root cause, and remediate the problem.
"""

import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  print("hello " + name + ", your random number is " + str(number))

greeting()