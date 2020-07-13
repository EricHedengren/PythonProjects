from random import randint
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*`~-+=';:/?|><"
password = ''

length = randint(10,30)

for i in range(length):
    password += letters[randint(0,len(letters)-1)]

print(password)