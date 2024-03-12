AREA OF CIRCLE
"""
r = float(input(""))
pi = 3.142
area = pi * r**2
print("The area of the circle with radius",r,"is:",area)
"""
AREA OF RECTANGLE
"""
import math
s1=float(input())
s2=float(input())
s3=float(input())
s=(s1+s2+s3)/2
area =math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print('The area of triangle is {}'.format(area))
"""
FIRSTNAME AND LASTNAME
"""
fname = input()
lname = input()
print("Hello "+ lname + " "+ fname)
"""
HRA
"""
bpa = float(input(''))
hra = bpa*0.8
da = bpa*0.4
total = hra+da+bpa
print('{:.02f}'.format(total))
"""
SUM OF DIGITS
"""
def calculate(n, power):
    return sum([int(i) for i in str(pow(n, power))])
n = 2
power = int(input(''))
print (calculate(n, power))
"""
SURFACE AREA
"""
l = int(input(''))
w = int(input(''))
h = int(input(''))
sa = (2*((w*l)+(l*h)+(h*w)))
print(sa)
"""
TIME IN SECONDS
"""
days = int(input()) * 3600 * 24
hours = int(input()) * 3600
minutes = int(input()) * 60
seconds = int(input())

time = days + hours + minutes + seconds

print(time)
"""
VOLUME OF SPHERE
"""
r = float(input(''))
pi = 3.14
volume = (4.0/3.0)*pi*r**3
print(volume)
"""
VOLUME OF SPHERE(for given Radius)
"""
pi = 3.142
r = int(input(''))
vol = (4/3)*pi*r*r*r
print(str(vol))
"""
PENTAGONAL NUMBERS
"""
n = int(input())
# Generate the first n pentagonal numbers
for i in range(1, n):
    # Calculate the i-th pentagonal number using the formula Pn=n(3n−1)/2
    Pn = int( (i * (3 * i - 1)) / 2)
    # Print the i-th pentagonal number
    print(Pn)
"""
SMALLEST NUMBER
"""
def smallest_multiple(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    result = 1
    for prime in primes:
        power = 1
        while prime**power <= n:
            power += 1
        result *= prime**(power-1)
    return result

n = int(input())
print(smallest_multiple(n))
"""
PRINTING EVEN AND ODD SEPARATELY
"""
n = int(input())
even = []
odd = []
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(*even, end=' ')
print()
print(*odd, end=' ')
print()
"""
FACTORIAL
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))
"""
ASCENDING ORDER
"""
arr = list(map(int, input().split()))

# Sort the array in ascending order using a for loop
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

# Print the sorted array
print(*arr)
"""
ISBN 
"""
def validate_isbn(isbn):
    if len(isbn) != 10: # ISBN should be a 10 digit number
        return "Invalid"
    else:
        total = 0
        for j in range(10):
            if isbn[j] == 'X': # handle the case where last digit is 'X'
                total += 10 * (10-j)
            else:
                total += int(isbn[j]) * (10-j)
        if total % 11 == 0:
            return "Valid"
        else:
            return "Invalid"

t = int(input()) # number of books
for i in range(t):
    isbn = input()
    print(validate_isbn(isbn))
"""
ODD OR EVEN
"""
def check_even(n):
    if n %2 == 0:
        return "Even"
    else:
        return "ODD"
n = int(input())
print(check_even(n))
"""
PERFECT NUMBER OR NOT
"""
def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
num = int(input())
if is_perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
"""
REPLACE NUMBER
"""
def replace_digits(num_str):
    return num_str.replace('0', 'x').replace('7', '0').replace('x', '7')

input_str = str(input().strip())
print(replace_digits(input_str))
"""
SORTED TABLE
"""
n, m = map(int, input().strip().split(' '))

# read the data into a list of tuples
data = []
for i in range(n):
    row = tuple(map(int, input().strip().split(' ')))
    data.append(row)

# sort the data based on the k-th attribute
k = int(input().strip())
data = sorted(data, key=lambda x: x[k])

# print the sorted data
for row in data:
    print(" ".join(map(str, row)))
"""

END
