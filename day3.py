#There are  lines of numeric input:
#The first line has a double,  (the cost of the meal before tax and tip).
#The second line has an integer,  (the percentage of  being added as tip).
#The third line has an integer,  (the percentage of  being added as tax).

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
	total_cost=round(meal_cost + (meal_cost*(tip_percent/100)) + (meal_cost*(tax_percent/100)))
	print(total_cost)

if __name__ == "__main__":
	meal_cost=float(input())
	tip_percent=int(input())
	tax_percent=int(input())

	solve(meal_cost,tip_percent,tax_percent)
