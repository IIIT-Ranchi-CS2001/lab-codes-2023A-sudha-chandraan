# question 1
# Write a program to find the:
# Sum,  
# Difference,   
# Product,  
# Integer quotient,
# Remainder 
# Fractional quotient
# of two numbers. Enter the numbers on run time. Display the input data and results in neat format


def perform_operations(num1, num2):

    sum_result = num1 + num2
    

    difference_result = num1 - num2
    

    product_result = num1 * num2
    

    integer_quotient = num1 // num2
    remainder_result = num1 % num2
    

    fractional_quotient = num1 / num2
    
    return sum_result, difference_result, product_result, integer_quotient, remainder_result, fractional_quotient

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result, difference_result, product_result, integer_quotient, remainder_result, fractional_quotient = perform_operations(num1, num2)


print("\nResults:")
print(f"First Number: {num1}")
print(f"Second Number: {num2}")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Integer Quotient: {integer_quotient}")
print(f"Remainder: {remainder_result}")
print(f"Fractional Quotient: {fractional_quotient:.2f}")



# question2
# Write python program to find
# (a) Area and perimeter of a triangle when all three sides are given. Hint: (Use Heron’s Equation)
# (b) Find all three angles of the triangle given in (a)
# Display the input data and results in proper format.

import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calculate_angles(a, b, c):
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180 - angle_A - angle_B
    return angle_A, angle_B, angle_C

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    
    area = calculate_area(a, b, c)
    
    angle_A, angle_B, angle_C = calculate_angles(a, b, c)

    print("\nTriangle Details:")
    print(f"Sides: a = {a}, b = {b}, c = {c}")
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Angle A: {angle_A:.2f} degrees")
    print(f"Angle B: {angle_B:.2f} degrees")
    print(f"Angle C: {angle_C:.2f} degrees")
else:
    print("The given sides do not form a valid triangle.")

# question3
# Write a program to find:
# The equivalent impedance when two impedances Z1 and Z2 are connected in parallel. 
# Display Z1 and Z2 in complex form. 
# Display the real part and imaginary part of the result in separate lines.


import cmath

def equivalent_impedance_parallel(Z1, Z2):
    Z_equiv = 1 / ((1 / Z1) + (1 / Z2))
    return Z_equiv

Z1_real = float(input("Enter the real part of Z1: "))
Z1_imag = float(input("Enter the imaginary part of Z1: "))
Z2_real = float(input("Enter the real part of Z2: "))
Z2_imag = float(input("Enter the imaginary part of Z2: "))

Z1 = complex(Z1_real, Z1_imag)
Z2 = complex(Z2_real, Z2_imag)

Z_equiv = equivalent_impedance_parallel(Z1, Z2)

Z_equiv_real = Z_equiv.real
Z_equiv_imag = Z_equiv.imag

print("\nImpedances:")
print(f"Z1: {Z1}")
print(f"Z2: {Z2}")
print(f"Equivalent Impedance: {Z_equiv}")

print(f"Real part of Equivalent Impedance: {Z_equiv_real}")
print(f"Imaginary part of Equivalent Impedance: {Z_equiv_imag}")
