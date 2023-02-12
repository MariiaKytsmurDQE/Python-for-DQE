import random  # importing random module


#  Getting 100 numbers from 0 to 1000
hundred_random_numbers = []  # Create a list
for _ in range(100):  # Define count of numbers in the list
    hundred_random_numbers.append(random.randint(0, 1000))  # Create the list of numbers from 0 to 1000
# Sort list from min to max
sorted_numbers = []  # Create a new list for further sorted numbers from min to max
while hundred_random_numbers:
    minimum = hundred_random_numbers[0]  # Put min value on the beginning of the list
    for number in hundred_random_numbers:
        if number < minimum:
            minimum = number
    sorted_numbers.append(minimum)
    hundred_random_numbers.remove(minimum)
# Calculate AVG for evens and odds number from the list
even_numbers = []  # Create an empty list for further count of even numbers
odd_numbers = []  # Create an empty list for further count of odd numbers
for i in sorted_numbers:
    if i % 2 == 0:  # Check whether the element of list is even number
        even_numbers.append(i)  # Append every even number to list 'even'
        even_average = round(sum(even_numbers) / len(even_numbers))
    elif i % 2 == 1:  # Check whether the element of list is odd number
        odd_numbers.append(i)  # Append every even number to list 'odd'
        odd_average = round(sum(odd_numbers) / len(odd_numbers))

print('Sorted numbers for min to max: ', sorted_numbers)
print('Average of even numbers: ', even_average)
print('Average of odd numbers: ', odd_average)
