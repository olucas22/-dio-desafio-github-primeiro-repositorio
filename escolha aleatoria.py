from random import choice
from time import sleep
a = str(input('Primeiro time: '))
b = str(input('Segundo time: '))
c = str(input('Terceiro time: '))
print('Será sorteado o time que irá pra repescagem.')
print('-=-'*30)
print('Carregando...')
sleep(5)
lista = [a, b, c]
escolhido = choice(lista)
print('O time que irá jogar a repescagem é o {}{}{}.'.format('\033[1;36;40m', escolhido, '\033[m'))