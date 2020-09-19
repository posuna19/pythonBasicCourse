#!/usr/bin/env python3
import sys
import random

print("**** Simulating a program ****")

value = random.randint(1, 3)
print("Returning value: ", value)
print("**** program end ****")
sys.exit(value)

