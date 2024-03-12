ALPHABET OR NOT
"""
ch = input()

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("ALPHABET")
else:
    print("NOT AN ALPHABET")
"""
APPLE BUDGET
"""
apple1 = int(input())
apple2 = int(input())
apple3 = int(input())
if apple2 > apple1 and apple3 > apple2:
    print("Fit into Budget")
else:
    print("Doesn't fit into Budget")
"""
CATEGORY OF TRIANGLE
"""
side1 = int(input())
side2 = int(input())
side3 = int(input())
if side1 == side2:
    if side2 == side3:
        print("Equilateral triangle")
    else:
        print("Isoceles triangle")
elif side1 == side3:
    print("Isoceles triangle")
elif side2 == side3:
    print("Isoceles triangle")
else:
    print("Scalene triangle")
"""
CLASS GRADE
"""
s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
total=s1+s2+s3+s4+s5
avg=total/5
print("{:.2f}".format(avg),"Percent")
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
elif avg>=40:
    print("Grade E")
else:
    print("Grade F")
"""
INVALID WITHDRAWAL REQUEST
"""
requested_amount = int(input())
initial_balance = float(input())
bank_charges = 0.5
if requested_amount % 5 != 0 or requested_amount > initial_balance - bank_charges:
    print("Invalid Withdrawal Request")
    print("Initial Balance : {:.2f}".format(initial_balance))
else:
    current_balance = initial_balance - requested_amount - bank_charges
    print("Current Balance : {:.2f}".format(current_balance))
    print("Initial Balance : {:.2f}".format(initial_balance))
"""
LEAP OR NOT
"""
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
"""
PROFIT OR LOSS
"""
cp = int(input())
sp = int(input())

if cp > sp:
    print("Mislay")
elif cp < sp:
    print("Profit")
else:
    print("No Profit No Mislay")
"""
ROOM RENT
"""
month = int(input())
room_rent = float(input())
num_of_days = int(input())

if month == 4 or month == 5:
    total_rent = room_rent * num_of_days * 1.2
else:
    total_rent = room_rent * num_of_days

print("Rs.{:.2f}".format(total_rent))
"""
SPEED DIFFERENCE
"""
arav_speed = int(input())
aaron_speed = int(input())
if arav_speed > aaron_speed:
    speed_diff = arav_speed - aaron_speed
    print(speed_diff)
elif aaron_speed > arav_speed:
    speed_diff = aaron_speed - arav_speed
    print(speed_diff)
else:
    print(0)
"""
VOTE ELIGIBILITY
"""
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
"""
END
