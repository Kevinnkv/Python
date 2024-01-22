# MIN TRIPLE
# cre: thethanh02 
import heapq
import re
import sys

# Custom input function using sys.stdin.readline
input = sys.stdin.readline

# Number of test cases
t = int(input())

while t > 0:
    t -= 1

    # Read the size of the array
    n = input()
    
    # Read the array and duplicate spaces to ensure proper matching
    arrStr = ' ' + input().replace(' ', '  ') + ' '

    # Initialize an empty list to store matched integers
    arr = []

    # Iterate through possible patterns to find integers
    i = -8
    while i < 9 and len(arr) < 4:
        if i < 0:
            pattern = '-' + '\\d'*abs(i) + ' '
        elif i > 0:
            pattern = ' ' + '\\d'*abs(i) + ' '
        else:
            i += 1
            continue

        # Use regular expression to find integers in the array string
        tmpArr = re.findall(pattern, arrStr)

        # Convert matched strings to integers and add to the list
        arr += [int(x) for x in tmpArr]

        i += 1

    # Calculate the sum of the three smallest integers
    result_sum = sum(heapq.nsmallest(3, arr))

    # Print the result
    print(result_sum)
