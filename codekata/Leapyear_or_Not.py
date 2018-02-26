n=int(input("Enter the year to check leap year or not:"))
if n % 4 == 0 and n % 100!= 0 or n % 400 == 0:
     print("Yes.")
else:
     print("No.")
