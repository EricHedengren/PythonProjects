import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*`~-+=';:/?|><"
password = ''

for i in range(25):
    password += letters[random.randint(0,len(letters)-1)]

print(password)