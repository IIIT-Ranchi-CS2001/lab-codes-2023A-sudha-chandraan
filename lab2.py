# Question1
# If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
# “mAHA bHARAT”
# “Bharat”
# “BharatBharatBharat”
# “Mera Bharat”
# “Mera Bharat Mahan”


S1 = "Maha Bharat"
S1_swapped = S1.swapcase()
S1_bharat = S1.split()[1]
S1_bharat_repeat = S1_bharat * 3
S1_mera_bharat = S1.replace("Maha", "Mera")
S1_mera_bharat_mahan = S1_mera_bharat + " Mahan"

print(f'1. "{S1_swapped}"')
print(f'2. "{S1_bharat}"')
print(f'3. "{S1_bharat_repeat}"')
print(f'4. "{S1_mera_bharat}"')
print(f'5. "{S1_mera_bharat_mahan}"')

# question2>
# For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
# The length of the string S
# The first occurrence of the letter ‘e’
# The total number of occurrences of ‘a’
# Generate “Ta Ta Black Sheep”


S = "Ba Ba Black Sheep"
length_of_S = len(S)
first_occurrence_of_e = S.find('e')
occurrences_of_a = S.count('a')
new_string = S.replace('Ba', 'Ta')
print(f"Length of the string: {length_of_S}")
print(f"First occurrence of 'e': {first_occurrence_of_e}")
print(f"Total occurrences of 'a': {occurrences_of_a}")
print(f"New string: {new_string}")


# question3
# Write a python script to enter any string at run time and check whether it is a palindrome or not.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")


# question3
# Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown:
# Name:
# Roll Number:
# Marks:
# Grade Point:
# Remark:
# The criteria for awarding grade point and remark are as given in the table:

# S. No.
# Range of Marks
# Grade Point
# Remark
# 1
# >= 90
# 10
# OUTSTANDING
# 2
# 90 > Marks >= 80
# 9
# VERY GOOD
# 3
# 80 > Marks >= 70
# 8
# GOOD
# 4
# 70 > Marks >= 60
# 7
# AVERAGE
# 5
# 60 > Marks >= 50
# 6
# PASS
# 6
# Marks < 50
# 0
# FAIL


def calculate_grade_and_remark(marks):
    if marks >= 90:
        return 10, "OUTSTANDING"
    elif marks >= 80:
        return 9, "VERY GOOD"
    elif marks >= 70:
        return 8, "GOOD"
    elif marks >= 60:
        return 7, "AVERAGE"
    elif marks >= 50:
        return 6, "PASS"
    else:
        return 0, "FAIL"


name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")
marks = float(input("Enter marks secured in Mathematics out of 100: "))

grade_point, remark = calculate_grade_and_remark(marks)

print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks}")
print(f"Grade Point: {grade_point}")
print(f"Remark: {remark}")



# question4
# Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)
# Hint: find the discriminant d= b2 − 4ac
# If d = 0, the equation has one real repeated root (both roots are the same: 
# R1= R2 = -b/(2a)

# If d > 0, the equation has two distinct real roots.
# 	R1= (-b + sqrt(d))/2a
# R2= (-b - sqrt(d))/2a
 
# If d < 0, the equation has two complex roots.
# real_part = -b / (2 * a) 
# imaginary_part = math.sqrt(-discriminant) / (2 * a)


import math

def find_roots(a, b, c):

    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        R1 = (-b + math.sqrt(discriminant)) / (2 * a)
        R2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The equation has two distinct real roots: R1 = {R1}, R2 = {R2}")
    elif discriminant == 0:
        R1 = R2 = -b / (2 * a)
        print(f"The equation has one repeated real root: R1 = R2 = {R1}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The equation has two complex roots: R1 = {real_part} + {imaginary_part}i, R2 = {real_part} - {imaginary_part}i")


a = int(input("Enter the coefficient a (a ≠ 0): "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))


if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    find_roots(a, b, c)












