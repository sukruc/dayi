import random
import os


data = open("dayi.txt", encoding='utf16').readlines()

data = [line for line in data if line.strip()]

soz = random.choice(data)

print(soz)

# yortumcu