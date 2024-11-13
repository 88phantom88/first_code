print("hello world!")
import random

simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenght = int(input("введите длинну пароля"))

password = ""

for i in range(lenght):
    password += random.choice(simvols)

print(password)
