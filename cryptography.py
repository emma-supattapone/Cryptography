"""
cryptography.py
Author: Emma Supattapone
Credit: Abby Feyrer

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
#associations.find()

x = 1
while x == 1: 
    hamilton = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if hamilton == "e":
        mesg = input("Message: ")
        ky = input("Key: ")
        print("encrypt")
    elif hamilton == "d":
        mesgg = input("Message: ")
        kyy = input("Key: ")
        print("decrypt")
    elif hamilton == "q":
        print("Goodbye!")
        x = 2
    else:
        print("Did not understand command, try again.")
