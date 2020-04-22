#Password Generator App Version 1.0
#Created by Han
#Finished in 9.4.2020

#import random and string module
import random
import string


#function to check length of password
def check_length():
    global length_of_password
    while length_of_password < 6:
        print("Minimum 6 letters ")
        length_of_password = int(input("How long do you want your password to be?\n>>> "))


#function to check logical addition between letters and numbers
def check_input():
    global length_of_password
    global how_many_letters
    global how_many_numbers_symbols
    while length_of_password >=6 and length_of_password != how_many_numbers_symbols + how_many_letters:
        print('invalid input')
        length_of_password = int(input("How long do you want your password to be?\n>>> "))
        while length_of_password < 6:
            print("Minimum 6 letters ")
            length_of_password = int(input("How long do you want your password to be?\n>>> "))
        how_many_letters = int(input("How many letters do you want to put in your password?\n>>> "))
        how_many_numbers_symbols = int(input("How many numbers and symbols do you want too put in your password?\n>>> "))


#function to generate password
def password_generator():
    global letters
    global mixture1
    global result
    letters = string.ascii_letters
    mixture1 = ""
    result = mixture1.join(random.choice(letters) for i in range(how_many_letters))

    global numbers
    global result2
    numbers = string.digits
    symbols = string.punctuation
    sum = numbers + symbols
    mixture2 = ""
    result2 = mixture2.join(random.choice(sum) for i in range(how_many_numbers_symbols))

    global password
    global result3
    global mixed_password

    password = result + result2
    mixed_password = ''.join(random.sample(password, len(password)))


print("Password Generator\nVersion 1.0\nCreated by Han\n")
length_of_password = int(input("How long do you want your password to be?\n>>> "))
check_length()
how_many_letters = int(input("How many letters do you want to put in your password?\n>>> "))
how_many_numbers_symbols = int(input("How many numbers and symbols do you want too put in your password?\n>>> "))
check_input()
password_generator()
print("")
print("Your generated password is " +mixed_password)
