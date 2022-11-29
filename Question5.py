### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
##### Sol.

#Prime numbers:
#If the natural number is greater than 1 and having no positive divisors other than 1 and the number itself etc.
#For example: 3, 7, 11 etc are prime numbers.

#Taking input from user
lower=1;
upper=100001;
print("All Prime Numbers in an Interval of 1-10000")
for num in range(lower,upper+1):
    #For checking prime number we use function
    def PrimeChecker(num):
        #Checking number is above 1 or not because less than 1 is neither prime nor composite
        if num>1:
            for j in range(2,num):
                if (num%j)==0:
                    break
            else:
                print(num, end = ' ')
    #Calling above function of execution
    PrimeChecker(num)
    

##########################################################
######################ANSWER##############################
#    All Prime Numbers in an Interval of 1-10000:
#        2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 
#        59 61 67 71 73 79 83 89 97 101 103 107 109 
#        113 127 .............. 99833 99839 99859 
#        99871 99877 99881 99901 99907 99923 99929 
#        99961 99971 99989 99991


                


