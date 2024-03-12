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
END
