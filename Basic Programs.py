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
