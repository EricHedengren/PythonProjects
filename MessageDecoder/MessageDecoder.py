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

q = input("What's the code key: ")

newCode = []
for i in range(0, len(q), 5):
    newCode.append(q[i:i+5])

decode = input("Enter the code: ")
decoded = ''

for i in range(0, len(decode), 5):
    decoded += alp[newCode.index(decode[i:i+5])]

print(decoded)