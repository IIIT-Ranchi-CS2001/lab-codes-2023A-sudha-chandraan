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
