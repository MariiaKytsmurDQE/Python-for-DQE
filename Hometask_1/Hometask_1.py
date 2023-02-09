import random  # importing random module
#  getting 100 numbers from 0 to 1000
hundred_random_numbers = []  # create a list
for _ in range(100):  # define count of numbers in the list
    hundred_random_numbers.append(random.randint(0, 1000))  # create the list of numbers from 0 to 1000
# sort list from min to max
sorted_numbers = []  # create a new list for further sorted numbers from min to max
while hundred_random_numbers:
    minimum = hundred_random_numbers[0]  # put min value on the beginning of the list
    for a in hundred_random_numbers:
        if a < minimum:
            minimum = a
    sorted_numbers.append(minimum)
    hundred_random_numbers.remove(minimum)
# calculate AVG for evens and odds number from the list
even_numbers = []  # Create an empty list for further count of even numbers
odd_numbers = []  # Create an empty list for further count of odd numbers
even_sums = 0  # declare and initialised variable evenSums to sum of even numbers
odd_sums = 0  # declare and initialised variable oddSums to sum of odd numbers
even_count = 0  # declare and initialised variable evenCount to count of even numbers
odd_count = 0  # declare and initialised variable oddCount to count of odd numbers
for i in sorted_numbers:
    if i % 2 == 0:  # Check whether the element of list is even number
        even_count += 1  # Count of even numbers
        even_numbers.append(i)
        even_sums += i  # Sum of even numbers
        even_numbers.append(i)  # Append every even number to list 'even'
    elif i % 2 == 1:  # Check whether the element of list is odd number
        odd_count += 1  # Count of odd numbers
        odd_numbers.append(i)
        odd_sums += i  # Sum of odd numbers
        odd_numbers.append(i)  # Append every even number to list 'odd'
        even_average = round((even_sums / even_count))
        odd_average = round((odd_sums / odd_count))
print(sorted_numbers)
print(even_average)
print(odd_average)
