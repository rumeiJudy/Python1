'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float(
'''


# Way 1
hrs = input("Hours:")
h = float(hrs)

rate = input("rate:")
r = float(rate)
if h <= 40:
    print(h * r)
else:
    print((40*r)+(h - 40)*1.5*r)

# Way 2
hrs = input("Hours:")
h = float(hrs)

rate = input("rate:")
r = float(rate)

if h <= 40:
    print(h*r)
if h > 40:
    print( 40 * r + (h - 40) * r * 1.5)


# Way 3
hrs = input("Hours:")
h = float(hrs)

rate = input("rate:")
r = float(rate)


if h != 0:
    if h <= 40:
        print(h*r)
    if h > 40:
        print( 40 * r + (h - 40) * r * 1.5)
