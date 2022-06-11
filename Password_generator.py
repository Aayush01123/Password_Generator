#Python Program To Create A Random Password Generator

#import the necessary modules!
import random
import string
import sys


print("Would You like to to create strong password")
a=input("Enter yes/no : ")

if a == "yes" or a == "Yes":
    print("You enter",a)

else:
    print("You enter ",a)
    sys.exit()

print("Welcome to our Random Password Generator")
def main():
    #input the length of the password
    length = int(input("Enter the length of password you want: "))

    #define data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbols = string.punctuation

    #combine the data
    combine = lower + upper + digit + symbols

    #use random
    x = random.sample(combine, length)

    #Create the password
    password = "".join(x)

    #print the password
    print("Your Password is : ", password)
    main()

main()
