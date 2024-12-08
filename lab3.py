#question 1>
# Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop
# Number    	Square
# 1              	1
# 2               	4
# …		…
# n		n


def squares_of_natural_numbers(n):
    print(f"{'Number':<10}{'Square':<10}")  
    print("-" * 20)
    
    i = 1  
    while i <= n:
        print(f"{i:<10}{i**2:<10}") 
        i += 1  


try:
    n = int(input("Enter the value of n (natural number): "))

    if n > 0:
        squares_of_natural_numbers(n)
    else:
        print("Error: Please enter a positive natural number.")
except ValueError:
    print("Error: Please enter a valid number.")
  
  
    
# question 2 
# Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.    
# Function to calculate the sum of digits


def sum_of_digits(number):
    original_number = number  
    digit_sum = 0
    
   
    while number > 0:
        digit_sum += number % 10  
        number //= 10  
    

    print(f"The number: {original_number}")
    print(f"The sum of its digits: {digit_sum}")

try:
    num = int(input("Enter a positive integer: "))
    
    if num >= 0:
        sum_of_digits(num)
    else:
        print("Error: Please enter a positive integer.")
except ValueError:
    print("Error: Please enter a valid number.")


# question 3
# Write a python script to print the first n terms of the Fibonacci series using while loop

def fibonacci_series(n):

    a, b = 0, 1
    count = 0

    print("Fibonacci Series:")
    
    while count < n:
        print(a, end=" ")  

        a, b = b, a + b
        count += 1


try:
    n = int(input("Enter the number of terms to print: "))
    
    if n > 0:
        fibonacci_series(n)
    else:
        print("Error: Please enter a positive integer.")
except ValueError:
    print("Error: Please enter a valid number.")


# question 4
# Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.


def multiplication_table(number, limit):
    print(f"Multiplication Table of {number} up to {limit}:")
    

    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


try:
    num = int(input("Enter the number for the multiplication table: "))
    limit = int(input("Enter the limit for the multiplication table: "))

    if limit > 0:
        multiplication_table(num, limit)
    else:
        print("Error: Please enter a positive limit.")
except ValueError:
    print("Error: Please enter valid numbers.")
    
    
    
# question 5    
# Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.
    

def are_all_characters_alphanumeric(s):
 
    for char in s:
   
        if not char.isalnum():
            return False
    return True


input_string = input("Enter a string to check if all characters are alphanumeric: ")

result = are_all_characters_alphanumeric(input_string)
print(result)



# question6
# Write a python script to find the number of occurrences of a particular character present in the given string using a loop. (Don’t use string methods).

def count_character_occurrences(s, char_to_count):
    count = 0
    

    for char in s:
    
        if char == char_to_count:
            count += 1
    
    return count


input_string = input("Enter a string: ")
char_to_find = input("Enter the character to find: ")


if len(char_to_find) != 1:
    print("Error: Please enter a single character.")
else:

    occurrences = count_character_occurrences(input_string, char_to_find)
    print(f"The character '{char_to_find}' appears {occurrences} times in the string.")
