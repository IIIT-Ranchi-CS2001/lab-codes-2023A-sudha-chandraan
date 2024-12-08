# question1>
# Generate two tuples to represent two distinct points in space. (Three dimensional geometry). Determine the Euclidian distance between the two.

import math
point1 = (1, 2, 3)
point2 = (4, 5, 6)
distance = math.sqrt((point2[0] - point1[0])**2 + 
                     (point2[1] - point1[1])**2 + 
                     (point2[2] - point1[2])**2)
print(f"Euclidean distance between {point1} and {point2} is: {distance}")


# qusetion2>
# Generate three lists using list comprehension. List of names, list of Roll nos and list
# of marks for Physics exam for all students of the class. Create a list of tuples using the zip function where each tuple carries individual 
# student details. Sort the list of tuples using a sorted function by keeping Marks as the key for sorting.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
roll_nos = [101, 102, 103, 104, 105]
marks = [85, 92, 78, 88, 95]
student_details = list(zip(names, roll_nos, marks))
sorted_students = sorted(student_details, key=lambda x: x[2])
print("Sorted student details by marks:")
for student in sorted_students:
    print(student)


# qusetion3>
# Redo question 3 without using zip and sorted functions.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
roll_nos = [101, 102, 103, 104, 105]
marks = [85, 92, 78, 88, 95]

student_details = []
for i in range(len(names)):
    student_details.append((names[i], roll_nos[i], marks[i]))
n = len(student_details)
for i in range(n):
    for j in range(0, n-i-1):
        if student_details[j][2] > student_details[j+1][2]:
            student_details[j], student_details[j+1] = student_details[j+1], student_details[j]

print("Sorted student details by marks:")
for student in student_details:
    print(student)

# qusetion4>
# Enter a string. Determine the count of each letter present in the 
# string using the concept of dictionary

input_string = input("Enter a string: ")
letter_count = {}
for char in input_string:
    if char.isalpha(): 
        char = char.lower()  
        if char in letter_count:
            letter_count[char] += 1 
        else:
            letter_count[char] = 1   

print("Count of each letter in the string:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")



# qusetion 6>WAP to count the number of each character present in a string using the concept of a dictionary.

string = input("Enter a string: ")
char_count = {}

for char in string:
    if char != ' ': 
        char_count[char] = char_count.get(char, 0) + 1

print("Character frequencies (excluding spaces):")
for char, count in char_count.items():
    print(f"'{char}': {count}")


# question 7>Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. 
# Construct a list of tuples with and without using built-in function zip().

names = [input("Enter customer name: ") for _ in range(3)]
customer_ids = [int(input("Enter customer ID: ")) for _ in range(3)]
points = [int(input("Enter shopping points: ")) for _ in range(3)]

customers_without_zip = [(names[i], customer_ids[i], points[i]) for i in range(3)]
print("List of tuples (without zip):", customers_without_zip)


# question 8> Sort the list of tuples constructed above with and without sorted function. 

names = [input("Enter customer name: ") for _ in range(3)]
customer_ids = [int(input("Enter customer ID: ")) for _ in range(3)]
points = [int(input("Enter shopping points: ")) for _ in range(3)]

customers_with_zip = list(zip(names, customer_ids, points))
print("List of tuples (with zip):", customers_with_zip)


customers_without_zip = [(names[i], customer_ids[i], points[i]) for i in range(3)]
print("List of tuples (without zip):", customers_without_zip)

sorted_customers_with_zip = sorted(customers_with_zip, key=lambda x: x[1])
print("Sorted customers (with zip, using sorted()):", sorted_customers_with_zip)

sorted_customers_without_zip = sorted(customers_without_zip, key=lambda x: x[1])
print("Sorted customers (without zip, using sorted()):", sorted_customers_without_zip)

def bubble_sort(customers):
    n = len(customers)
    for i in range(n):
        for j in range(0, n-i-1):
            if customers[j][1] > customers[j+1][1]:  
                customers[j], customers[j+1] = customers[j+1], customers[j]
    return customers

sorted_customers_with_zip_manual = bubble_sort(customers_with_zip.copy())
sorted_customers_without_zip_manual = bubble_sort(customers_without_zip.copy())

print("Sorted customers (with zip, manual sort):", sorted_customers_with_zip_manual)
print("Sorted customers (without zip, manual sort):", sorted_customers_without_zip_manual)
