#11. WAP to check number is even or Odd
num = int(input("Enter the number: "))
print(type(num))
if num % 2 == 0:
    print(f"Number {num} is Even number")
else:
    print(f"Number {num} is ODD number")

#12. WAP to check leap year
year = int(input("Enter the year : "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 !=0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

#13. WAP to check prime number
num = int(input("Enter the number : "))
flag = False
if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
if flag == True:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")

#14. WAP to check prime number in some specific interval
upper = 1
lower = 10
print("The prime numbers in between", upper, "and", lower,"is as follows:")
for num in range(upper,lower+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#15. WAP to find factorial of a number
num = int(input("Enter the number : "))
factorial = 1
if num < 0:
    print("Negative number does not have factorials")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(f"Factorial of {num} is {factorial}")


