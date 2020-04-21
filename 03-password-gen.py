import random

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
password = ""

usr_inp = int(input("What will be the length? > "))

def create_pass(length):
    print("\nGenerated password:\u001b[32m")
    for i in range(length):
        r = random.randint(1, len(characters) - 1)
        print(password + characters[r], end="")
    print("\n\u001b[37m")

create_pass(usr_inp)