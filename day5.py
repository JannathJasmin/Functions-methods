# 1.Write a function that computes the volume of a sphere given its radius
def volume_of_sphere(radius):
    return (4/3) * 3.14159 * radius**3
radius = float(input("Enter the radius of the sphere: "))
print("Volume of the sphere with radius", radius, "is:", volume_of_sphere(radius))

# 2.Write a function that checks whether a number is in a given range (inclusive of high and low)
def in_range(number, low, high):
    return low <= number <= high
num = float(input("Enter a number: "))
low_bound = float(input("Enter the lower bound of the range: "))
high_bound = float(input("Enter the upper bound of the range: "))
if in_range(num, low_bound, high_bound):
    print(f"{num} is within the range [{low_bound}, {high_bound}]")
else:
    print(f"{num} is not within the range [{low_bound}, {high_bound}]")

# 3.If you only wanted to return a boolean:
def ran_bool(num, lower, upper):
    return lower <= num <= upper
result = ran_bool(13, 1, 10)
print(result)

# 4.Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
#     Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#     Expected Output : 
#     No. of Upper case characters : 4
#     No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
def up_low(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Upper case characters :", upper_count)
    print("No. of Lower case Characters :", lower_count)
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(s)
up_low(s)
# 5a.Write a Python function that takes a list and returns a new list with unique elements of the first list.**
    # Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    # Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    return list(set(lst))
sample_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7]
unique = unique_list(sample_list)
print("Unique List:", unique)

#5b. unique_list([1,1,1,1,2,2,3,3,3,3,4,5,6,6,6,7,7,7])
def unique_set(lst):
    return set(lst)
unique_list=([1,1,1,1,2,2,3,3,3,3,4,5,6,6,6,7,7,7])
unique_set_result = unique_set(unique_list)
print("Unique Set:", unique_set_result)

#6. Write a Python function to multiply all the numbers in a list.**
    # Sample List : [1, 2, 3, -4]
    # Expected Output : -24
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
sample_list = [1, 2, 3, -4]
print("Sample List:", sample_list)
print("Expected Output:", multiply_list(sample_list))


#6b. multiply([1,2,3,4,74])
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
sample_list = [1, 2, 3, 4, 74]
#print("Sample List:", sample_list)
print("Expected Output:", multiply(sample_list))

# 7.Write a Python function that checks whether a passed in string is palindrome or not.
def is_palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]

string1 = "madam"
string2 = "nurses run"
string3 = "hello"

print(string1, "is a palindrome:", is_palindrome(string1))
print(string2, "is a palindrome:", is_palindrome(string2))
print(string3, "is a palindrome:", is_palindrome(string3))
print(is_palindrome(' '))

#8. Write a Python function to check whether a string is pangram or not.
import string
def is_pangram(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))

# 8.a
import string
print(string.ascii_lowercase)
# print("'" + string.ascii_lowercase + "'")

