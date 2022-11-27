### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
##### Sol.

#here we use nested if_elif_else condition :-

num=int(input("Enter number : "))

#checking number usding if_elif_else condition
if (num > 0):
    print("The number {} is positive".format(num))

elif (num < 0):
    print("The number {} is negative".format(num))

else :
    print("The number {} is zero".format(num))
###############################################
##############ANSWER##########################
#    Enter number : 10
#    The number 10 is positive
#
#    Enter number : 0
#    The number 0 is zero
#
#    Enter number : -5
#    The number -5 is negative