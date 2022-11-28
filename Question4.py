### 4. Write a Python Program to Check Prime Number?
##### Sol.

#Prime numbers:
#If the natural number is greater than 1 and having no positive divisors other than 1 and the number itself etc.
#For example: 3, 7, 11 etc are prime numbers.

#For checking prime number we use function

def PrimeChecker(num):
    #Checking number is above 1 or not because less than 1 is neither prime nor composite
    if (num > 1) :
        for j in range (2,int(num/2)+1):
            if (num % j)==0:
                print("The number {} is not prime number".format(num))
                break
        else:
            print("The number {} is prime number".format(num))
    else:
        print(num,"is neither prime nor composite")

#Taking input from user
num=int(input("Enter number : "))

#Calling above function of execution
PrimeChecker(num)


#############################################
############ANSWER###################
#        Enter number : 101
#        The number 101 is prime number