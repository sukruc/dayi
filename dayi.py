import random
import os


data = open("dayi.txt", encoding='utf-16').readlines()

data = [line for line in data if line.strip()]

soz = random.choice(data)

print(soz)

#
#