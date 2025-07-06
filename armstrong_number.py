num=int(input("enter the number "))
sum=0
temp=num
while temp>0:
    rem=temp%10
    sum+=rem**3
    temp//=10
if num==sum:
    print("The number is armstrong number")
else:
    print("It is not a armstrong number")