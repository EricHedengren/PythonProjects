import random

h = ".?! abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

alp = []
for i in h:
    alp.append(i)
code = []
for i in range(len(h)):
    code.append(str(random.randrange(10000,99999)))

message = input("Enter the message: ")
newMessage = ''
for i in message:
    newMessage += str(code[alp.index(i)])

p = ''
for i in code:
    p += i
print(newMessage, p)

q = input("What's the code key: ")

newCode = []
for i in range(0, len(q), 5):
    newCode.append(q[i:i+5])

decode = input("Enter the code: ")
decoded = ''

for i in range(0, len(decode), 5):
    decoded += alp[newCode.index(decode[i:i+5])]

print(decoded)