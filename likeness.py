import pandas as pd 
import matplotlib.pyplot as plt

# Calculates the percent difference between two values
def calcPercentDiff(n1, n2):
    if n1 <= 0 or n2 <= 0:
        raise ValueError("The value n1 or n2 cannot be 0 or negative")
    return abs(n1 - n2) / ((n1 + n2) / 2) * 100

# Calculates the percent difference between two lists
def calcPercentDiffList(l1, l2):
    if len(l1) != len(l2):
        raise ValueError("The length of the lists must be the same")
    return [calcPercentDiff(l1[i], l2[i]) for i in range(len(l1))] # list comprehension

# Calculates the average of a list
def calcAverage(l):
    return sum(l) / len(l)
    
def main():
    l1 = [1,2,3,4,5,6,7,8,9,10]
    l2 = [5,3,12,7,9,3,1,3,4,1]
    avg = calcAverage(calcPercentDiffList(l1, l2))
    print("These two lists are: {}%".format(round(100 - round(avg, 2), 2)))

main()