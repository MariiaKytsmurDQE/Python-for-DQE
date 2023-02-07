
import random # importing random module
# getting 100 numbers from 0 to 1000
list = [] # create a list
for i in range(100):  # define count of numbers in the list
    list.append(random.randint(0, 1001))  # create the list of numbers from 0 to 1000
# sort list from min to max
new_list = [] # create a new list for further sorted numbers from min to max
while list:
    minimum = list[0]  # define min value in the list
    for a in list:
        if a < minimum:
            minimum = a
    new_list.append(minimum)
    list.remove(minimum)
# calculate AVG for evens and odds number from the list
numbers = new_list
even = []  # Create an empty list for further count of even numbers
odd = []   # Create an empty list for further count of odd numbers
evenSums = 0  # declare and initialised variable evenSums to sum of even numbers
oddSums = 0  # declare and initialised variable oddSums to sum of odd numbers
evenCount = 0  # declare and initialised variable evenCount to count of even numbers
oddCount = 0  # declare and initialised variable oddCount to count of odd numbers
for i in numbers:
        if (i % 2) == 0:  # Check whether the element of list is even number
            evenSums += i  # Sum of even numbers
            even.append(i)  # Append every even number to list 'even'
        if (i % 2) == 1:  # Check whether the element of list is odd number
            oddSums += i  # Sum of odd numbers
            odd.append(i)  # Append every even number to list 'odd'
for x in numbers:  # to find count of odd and even numbers in the list
    if not x % 2:  # Check whether the element is not odd number
        evenCount += 1  # Count of even numbers
    else:
        oddCount += 1  # Count of odd numbers
print("Even Average: " + str  (evenSums / evenCount))
print("Odd Average: " + str  (oddSums / oddCount))

