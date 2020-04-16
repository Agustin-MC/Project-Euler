## Problem
#  Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#  1,2,3,5,8,13,21,34,55,89,...
#  By considering the terms in the Fibonacci sequence whose values do not exceen N, find the sum of the even-valued terms.
## Input format
#  First line contains T that denotes the Fibonacci sequence whose values do not exceed N, find the sum of the even valued terms. 
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
#  10
#  44
## Explanation
#  For N = 10, we have {2,8}, sum is 10.
#  For N = 100, we have {2,8,34}, sum is 44
#################################################################################################################

# list of variables
list_of_integers = []
fibonacci_series = [0,1]
sum_of_evens = 0
                
# inputs
number_of_integers = int(input("Enter the number of integers: "))

for i in range(0, number_of_integers):
    list_of_integers.append(int(input("Input Integer {} in list: ".format(i+1))))
    
for i in range(0, number_of_integers):
    N = list_of_integers[i]
    
    while fibonacci_series[-1] <= N:
        if fibonacci_series[-1] % 2 == 0:
            sum_of_evens += fibonacci_series[-1]
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])    
            
    print(sum_of_evens)
# reseting variables     
    sum_of_evens = 0
    fibonacci_series = [0,1]
    
    
