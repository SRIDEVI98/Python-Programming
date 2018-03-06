n=int(input("Enter the number to check palindrome or not:"))
rev=0
num=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n/10
if num==rev:
    print"Yes"
else:
    print"No"
