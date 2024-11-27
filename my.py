
import random
def password_generate(lenght):
    simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    
    password = ""
    
    for i in range(lenght):
        password += random.choice(simvols)
    
    return password
