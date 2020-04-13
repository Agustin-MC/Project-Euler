## Problem
#  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
#  The sum of these multiples is 23.
#  Find the sum of all the multiples of 3 or 5 below N.
## Constrains
#  1 <= T <= 10^5
#  1 <= N <= 10^9
## Output Format
#  For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.
################################################################################################################
## Sample Input
#  2
#  10
#  100
## Sample Output
#  23
#  2318
## Explanation
#  For N = 10, if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
#  The sum of these multiples is 23.
# Similarly for N = 100, we get 2318
#################################################################################################################



# list of variables
list_of_integers = []
sum_of_3ths = 0
sum_of_5ths = 0
sum_of_15ths = 0


# inputs
number_of_integers = int(input("Enter the number of integers: "))

for i in range(0, number_of_integers):
    list_of_integers.append(int(input("Input Integer {} in list: ".format(i+1))))

for i in range(0, number_of_integers):
    N = list_of_integers[i] - 1
    for i in range(0, N//3):
        sum_of_3ths += 3*(i+1)
    for i in range(0, N//5):
        sum_of_5ths += 5*(i+1)
    for i in range(0, N//15):
        sum_of_15ths += 15*(i+1)
    sum_of_3ths_and_5ths_minus_multiples= sum_of_3ths + sum_of_5ths - sum_of_15ths
    print(sum_of_3ths_and_5ths_minus_multiples)
    
    #reseting points for next itterations
    sum_of_3ths = 0
    sum_of_5ths = 0
    sum_of_15ths = 0
    

