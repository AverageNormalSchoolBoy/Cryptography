"""
cryptography.py
Author: Brendan
Credit: Dennison

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

z=0
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
while z !=1:
    input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if input1 == 'e':
        message = input('Message: ')
        key = input('Key: ')
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
            enc[i] = message[i] + key[j]
            i=i+1
            if j < len(key)-1:
                j=j+1
            else:
                j=0
        enc = [associations[x] for x in enc]
        print("".join(enc))
    elif input1 == 'd':
        message = input('Message: ')
        key = input('Key: ')
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
            enc[i] = message[i] - key[j]
            i=i+1
            if j < len(key)-1:
                j=j+1
            else:
                j=0
        enc = [associations[x] for x in enc]
        print("".join(enc))
    elif input1 == 'q':
        print('Goodbye! ')
        z=1
    else: 
        print('Did not understand command, try again.')





    

    






