#Random Password Generator from @codehub.py

import random

#lower   = "abcdefghijklmnopqrstyvwxyz"
upper   = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
numbers  = "0123456789"
symbols = "*!@#$%&_"

#all = lower + upper + numbers + symbols

lower = input("Digite os caracteres de A - Z: ")
symbols = input("Digite os símbolos desejados no password: ")
length = input("Digite o tamanho do password desejado de 1 - 10: ")

all = lower + symbols


random = "".join(random.sample(all, int(length)))
print("Este é o seu password: %s" %random)

#length   = 16
#password = "".join(random.sample(all,length))
#print(password)



