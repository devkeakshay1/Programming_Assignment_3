### 2. Write a Python Program to Check if a Number is Odd or Even?
##### Sol.

#Even number is divisioble by 2(even%2==0)
#odd number is not divisible by 2(odd%2!=0)

num=int(input("Enter number : "))
if (num%2==0):
    print("The number {} is EVEN number".format(num))
else:
    print("The number {} is ODD number".format(num))

##########################################################
#############ANSWER##############################
#            Enter number : 1234
#            The number 1234 is EVEN number
#
#            Enter number : 121
#            The number 121 is ODD number