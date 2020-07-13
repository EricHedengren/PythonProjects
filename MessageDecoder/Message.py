import random

h = ".?! abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

alp = []
for l in h:
    alp.append(l)

code = []
for i in range(len(h)):
    code.append(str(random.randint(10000,99999)))

message = input("Enter the message: ")
newMessage = ''
for i in message:
    newMessage += str(code[alp.index(i)])

p = ''
for i in code:
    p += i
print(p, newMessage)