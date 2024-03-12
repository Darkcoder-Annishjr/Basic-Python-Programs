LENGTH OF THE STRING (without using len())
"""
a = input("Enter a String: ")
count = 0
for i in a:
    count += 1
    
print(count)
"""
LENGTH OF THE STRING
"""
L.find()"""
class length:
    def __init__(self, string):
        self.string = string
        
    def find(self):
        count = 0
        for char in self.string:
            count += 1
        print("Length of the string is:")
        print(count)

string = input()
L = length(string)
L.find()
"""
TOTAL NUMBER OF CHAR IN THE STRING
"""
a = input("Enter a String: ")
count = 0
for i in a:
    count += 1
    
print(count)
"""
SPLIT THE STRING
"""
a = input("Enter a String: ")
char = a.split()
print(char)
"""
REVERSING A STRING
"""
a = input("Enter a String: ")
char = a.split()
rev_words = ' '.join(reversed(char))
print(rev_words)
"""
TITLE FOR STRING
"""
a = input("Enter a String: ")
titl =  a.title()
print(titl)
"""
CAPITALIZE FOR STRING
"""
a = input("Enter a String: ")
cap = a.capitalize()
print(cap)
"""
FINDING SUBSTRING IN STRING
"""
my_str = input("Enter a String: ")
sub_str = input("Enter a Sub_String: ")
index = -1
while (index := my_str.find(sub_str, index +1)) != -1: 
print(index)
"""
REPLACING A STRING
"""
my_str = input("Enter a String: ")
sub_str = input("Enter a Substring: ")
new_str = input("Enter the new String: ")
my_str1 = my_str.replace(sub_str,new_str)
print(my_str1)
"""
REPLACING A STRING (using while loop)
"""
my_str = input("Enter a String: ")
substr = input("Enter a Substring: ")
new_str = input("Enter a New String: ")
index = -1
while True:
    index = my_str.find(substr, index + 1)
    if index == -1:
        break  # Exit the loop if no more occurrences are found
    # Replace the substring with the new string
    my_str = my_str[:index] + new_str + my_str[index + len(substr):]
print("Modified String:", my_str)
"""
PALINDROME
"""
class string:
    def __init__(self, s):
        self.s = s
    
    def reversecheck(self):
        # Reversing the string using slicing
        rev = self.s[::-1]
        
        # Checking if the reversed string is equal to the original string
        if self.s == rev:
            print("It is palindrome")
        else:
            print("It is not palindrome")
            
# Reading the input string from the user
s = input()
# Creating an object of the string class
str_obj = string(s)
# Calling the reversecheck method to check if the string is palindrome
str_obj.reversecheck()
"""

