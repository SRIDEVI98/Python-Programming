count=0
n=int(input("Enter number to print number of digit:"))

while n>0:
    n=n//10
    count=count+1
print(count)
