#!/usr/bin/env python3

import os,sys
import random,string
from hashlib import sha256

KEY_LENGTH_MAX = 32
# key = ''.join([random.choice(string.printable) for _ in range(random.randint(KEY_LENGTH_MAX//2,KEY_LENGTH_MAX))]) 
key = ''.join([random.choice(string.printable) for _ in range(KEY_LENGTH_MAX)])

cards = [
    ('Super Mario Bros.U DELUXE', 6480),
    ('Super Smash Bros - ultimate (special)', 7490), 
    ('Super Smash Bros - ultimate', 6480), 
    ('The Legend of Zelda - breath of the wild', 7460), 
    ('Let\'s go Pokemon Eevee!', 5490), 
    ('Let\'s go Pokemon Pikachu!', 5490), 
    ('Super Mario Party', 4840), 
    ('Kirby Star Allies', 4120), 
    ('Splatoon2', 3430), 
    ('Overcooked!', 980), 
    ('Overcooked!!', 1360), 
    ('Flag', 9999999)
]

money = 20000

def switchBS(bs):
    """
    Switch bytes and string.
    """
    if type(bs) == type(b''):
        return "".join(map(chr, bs))
    return n2s(int(''.join( hex(ord(c))[2:].rjust(2,'0') for c in bs),16))

def n2s(n,byteorder='big'):
    """
    Number to string.
    """
    length = (len(hex(n))-1)//2
    return int(n).to_bytes(length=length,byteorder=byteorder)

def eshop():
    print("\nWelcome to eShop ~ \nHere is the existing product : \n")
    for i,card in enumerate(cards):
        print(f'{i+1}. {card[0]} - {card[1]}')
    print()

def buy():
    num = int(input('card ID: ')) - 1
    
    if num < 0 or num >= len(cards):
        print('Invalid card ID.\n')
        return
    
    order = f'product={cards[num][0]}&price={cards[num][1]}&orderId={random.randint(1<<29,1<<30)}'
    order += f'&sign={sha256((key+order).encode()).hexdigest()}'
    print(f'Here is your order:\n{order}\n')
    
    if input('Pay now? (y to continue) ').lower() == 'y' :
        pay()
    else : 
        print('Well ... \n')

def pay():
    global money
    order = input('Give me your order :\n').strip()

    sign_idx = order.rfind('&sign=')
    if sign_idx == -1:
        print('Invalid Order.\n')
        return

    sign = order[sign_idx+6:]

    try:
        sign = b''.fromhex(sign)
    except TypeError:
        print('Invalid Order.\n')
        return

    order = order[:sign_idx]
    if sha256( switchBS(key+order) ).digest() != sign:
        print('Corrupt Order.\n')
        return

    for seg in order.split('&'):
        k,v = seg.split('=')
        if k == 'product':
            product = v
        elif k == 'price':
            try:
                price = int(v)
            except ValueError:
                print('Invalid Order.\n')
                return

    if money < price:
        print('Go away!!! Poor guys!!')
        return

    money -= price
    print(f'\nThank you for purchasing ~ ')
    print(f'You have bought {product}')
    print(f'Your current money: ${money}\n')
    if product == 'Flag':
        flag = open('flag').read().strip()
        print(f'YOOOOOOO! Here is your flag\n**********************************\n{flag}\n**********************************\n')

def exit():
    pass

def menu():
    print("Welcome to Nintendo eShop\n")
    while True:
        print(f"Current money: ${money}\n1. Take a look\n2. Order\n3. Pay for order\n4. Exit\n")
        try :
            choice = int(input("Command: "))
            if choice == 4 :
                print("See you next time.")
                return 
            {
                1: eshop,
                2: buy,
                3: pay,
                4: exit
            }.get(choice, lambda *args:1)()
        except ValueError:
            print('Invalid Order!\n')
            return

if __name__ == "__main__":
    menu()

