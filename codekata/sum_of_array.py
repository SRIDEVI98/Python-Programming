a=[]
n=int(input("Enter size array:"))
k=int(input("Enter the value to add the number in given array:"))
sum=0
for i in range(n):
    a.append(int(input("Enter the number:")))
for i in range(k):
    sum=sum+a[i]
print(sum)
            
