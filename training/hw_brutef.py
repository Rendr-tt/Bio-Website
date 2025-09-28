import string
import random
import time

letters = string.ascii_letters + "!@#$%^&*()_+-=[]{}|;:,.<>/?`~" + " "

result = ""

target = "Hello world!"

for letter in target:
    while True:
        I = random.choice(letters)
        print(result + I)
        if (I == letter):
            result += I
            break
        time.sleep(0.00001)
        