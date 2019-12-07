h = ".?! abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

alp = []
for i in h:
    alp.append(i)

q = input("What's the code key: ")

newCode = []
for i in range(0, len(q), 5):
    newCode.append(q[i:i+5])

decode = input("Enter the code: ")
decoded = ''

for i in range(0, len(decode), 5):
    decoded += alp[newCode.index(decode[i:i+5])]

print(decoded)