#Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.
#Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.

def prod(lst):
    multiply=1
    for i in lst:
        multiply*=i
    return multiply
lst=[1,2,3]
print(prod(lst))