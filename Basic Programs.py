SUM OF MULTIPLES
"""
def sum_of_multiples(N):
    total = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
N = int(input()) # get input from user
print(sum_of_multiples(N)) # calculate and print the sum of multiples
"""
FORMATTING - 1
"""
num_rows = int(input())

for i in range(num_rows):
    num_seats = num_rows - i
    row_layout = [num_seats] * num_seats
    print(*row_layout, end=" ")
    print()
"""
FORMATTING - 2
"""
n = int(input()) # get input from user

# iterate over each row in reverse order
for i in range(n, 0, -1):
    # print the appropriate number of stars for this row
    for j in range(i):
        print("*", end="")
    print() # move to the next line


n = int(input()) # get input from user

# iterate over each row
for i in range(n):
    # print the appropriate number of stars for this row
    for j in range(i+1):
        print("* ", end="")
    print() # move to the next line
"""
DISPLAY NAMES IN ALPHABETIC ORDER
"""
# Read the number of names
n = int(input())

# Read the character names
names = []
for i in range(n):
    names.append(input())

# Sort the names in alphabetical order
names.sort()

# Display the sorted names
for name in names:
    print(name)
"""
SWAPCASES
"""
def swap_case(s):
    """
    This function takes a string as input and swaps the case of all characters in the string.
    """
    swapped_str = ""
    for char in s:
        if char.isupper():
            swapped_str += char.lower()
        elif char.islower():
            swapped_str += char.upper()
        else:
            swapped_str += char
    return swapped_str

# Taking user input
s = input()

# Calling the swap_case function with user input
print(swap_case(s))
"""
PANAGRAM
"""
def is_pangram():
    # Read input sentence
    sentence = input("Enter a sentence: ").lower()

    # Initialize a list to keep track of used alphabets
    used = [False] * 26

    # Loop through each character in the sentence
    for char in sentence:
        # Check if character is an alphabet
        if char.isalpha():
            # Get the index of the alphabet (a=0, b=1, ...)
            index = ord(char) - ord('a')
            # Mark the alphabet as used
            used[index] = True

    # Check if all alphabets are used
    if all(used):
        return "pangram"
    else:
        return "not a pangram"
"""
COMPARISON BTW TWO NUMBERS (Using Ternary Opertor)
"""
num1 = int(input("Enter number num1: "))
num2 = int(input("Enter number num2: "))

'num1 is greater than num2' if num1 > num2 else 'num1 is not greater than num2'
'num1 is smaller than num2' if num1 < num2 else 'num1 is not smaller than num2'
'num1 is equal to num2' if num1 == num2 else 'num1 is not equal to num2'
"""
COMPARISON BTW THREE NUMBERS (Using Ternary Operator)
"""
num1 = int(input("Enter number num1: "))
num2 = int(input("Enter number num2: "))
num3 = int(input("Enter number num3: "))

'num1 is greater than num2 and num3' if num3 < num1 > num2 else 'num1 is not greater than num2 snd num3'
'num2 is greater than num1 and num3' if num1 < num2 > num3 else 'num2 is not greater than num1 and num3'
'num3 is greater than num1 and num2' if num1 < num3 > num2 else 'num3 is not greater than num1 and num2'
"""




