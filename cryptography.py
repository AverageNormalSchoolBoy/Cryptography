"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""


associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if input1 == 'e':
    message = input('Message: ')
    key = input('Key: ')
elif input1 == 'd':
    message = input('Message: ')
    key = input('Key: ')
elif input1 == 'q':
    print('Goodbye! ')
else: 
    print('Did not understand command, try again.')

message = list(message)
message = [associations.find(x) for x in message]
key = list(key)
key = [associations.find(x) for x in key]
key = [int(x) for x in key]
message = [int(x) for x in message]
enc = message
i=0
j=0
while i < len(message):
    enc = message[i] + key[j]
    i+1
    j+1




    

    






