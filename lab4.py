# Find the number of palindrome words in the given sentence without defining any new function 
# (feel free to use python’s in-built functions).

sentence = input("enter the sentence : ")
words = sentence.lower().split()
palindromes = [word for word in words if word == word[::-1]]
count = len(palindromes)
print(f"Number of palindrome words: {count}")


# question 2>
# Create a list of int using list comprehension [multiple input from keyboard].  Find the mean, median, and mode of the given list 
# (usage of specific modules such as statistics is strictly prohibited. Lab problems are for you to build-up logic and strengthen your understanding of
# the topic & its concepts).


numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
mean = sum(numbers) / len(numbers)
sorted_numbers = sorted(numbers)
n = len(numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
mode = max(frequency, key=frequency.get)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

# question 3>
# Generate 2 lists (course code and course name). create a new list with both course code and name like
# ["CS1001:Python",...]


course_codes = ["CS1001", "CS1002", "CS1003"]
course_names = ["Python", "Data Structures", "Algorithms"]

courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print(courses)


# question4>
# Generate two sets – first for all singers and second for all dancers of the class using set comprehension. Perform set operations to generate the following sets 
# of   all artists of the class
#     allrounders of the class
#     dancers but not singers
#     singers but not dancers
#     dancers but not singers cum singers but not dancers

singers = {"Alice", "Bob", "Charlie", "David"}
dancers = {"Charlie", "David", "Eve", "Fay"}
all_artists = singers | dancers  
allrounders = singers & dancers  
dancers_not_singers = dancers - singers 
singers_not_dancers = singers - dancers 
exclusive_artists = dancers ^ singers 
print(f"All artists: {all_artists}")
print(f"Allrounders: {allrounders}")
print(f"Dancers but not singers: {dancers_not_singers}")
print(f"Singers but not dancers: {singers_not_dancers}")
print(f"Exclusive artists (either dancers or singers but not both): {exclusive_artists}")



