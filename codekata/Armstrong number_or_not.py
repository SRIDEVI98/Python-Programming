num=int(input("Enter the value to check armstrong or not:"))
sum=0
temp=num
while num>0:
    r=num%10
    sum=sum+(r**3)
    num=num/10
if temp==sum:
    print("Yes")
else:
    print("No")
