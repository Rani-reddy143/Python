#checking the given year is leap year or not
year=int(input("enter the year"))
if (year%4==0) and (year%100!=0):
    print("leap year")
else:
    print("It is not a leap year")