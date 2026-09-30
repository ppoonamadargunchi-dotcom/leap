# 1. Take the year as an integer input from the user
year = int(input("Enter a year: "))

# 2. Check the leap year conditions
# A year is a leap year if it is divisible by 400, 
# OR divisible by 4 but NOT divisible by 100.
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
