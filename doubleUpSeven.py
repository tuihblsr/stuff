# unfinished
import random
import os
from colorama import Back

p_ammo = 0
p_poison = 0

ai_ammo = 0
ai_poison = 0

choice = ''
done = False
whoose_turn = 0 # 0 = player        1 = ai
moves = ['reload gun', 'reload poison', 'shoot', 'poison', 'defend', 'gas mask']
p_move = ''
ai_move = ''
ai_moved = ''

while not done:
    if whoose_turn == 0:
        choice = input('').lower().strip()
        if choice == 'reload gun':
            p_ammo += 1
            print('Player reloaded')
            print('Ammo: ', p_ammo)
            whoose_turn += 1
        elif choice == 'reload poison':
            p_poison += 1
            print('Poison: ', p_poison)
            whoose_turn += 1
        elif choice == 'shoot':
            if p_ammo > 0:
                p_move = 'shot'
                p_ammo -= 1
                print('You shot at the ai')
                whoose_turn += 1
            else:
                print("You spent 6 hours trying to shoot your gun and then realized you didn't reload it")
                whoose_turn += 1
        elif choice == 'poison':
            if p_poison > 0:
                p_move = 'poisoned'
                p_poison -= 1
                print('You poisoned the ais food')
                whoose_turn += 1
            else:
                print("Pretty sure you can't poison someone with air but ok ")
                whoose_turn += 1
        elif choice == 'defend':
            p_move = 'block'
            print('You used iron defense!!!!!!!! +1000000 defense')
            whoose_turn += 1
        elif choice == 'gas mask':
            p_move = 'mask'
            print("You put on a gas mask")
            whoose_turn += 1

        if whoose_turn == 1:
            ai_move = random.choice(moves)
            if ai_move == 'reload gun':
                ai_ammo += 1
                print('Ai reloaded their gun')
                whoose_turn -= 1
            elif ai_move == 'reload poison':
                ai_poison += 1
                print('Ai reloaded their poison')
                whoose_turn -= 1
            elif ai_move == 'shoot':
                if ai_ammo > 0:
                    ai_moved = 'shot'
                    ai_ammo -= 1
                    print('Ai shot at you')
                    whoose_turn -= 1
                else:
                    print('')
                    whoose_turn -= 1
            elif ai_move == 'poison':
                if ai_poison > 0:
                    ai_moved = 'poison'
                    ai_poison -= 1
                    print('Ai poisoned ur food')
                    whoose_turn -= 1
                else:
                    print('')
                    whoose_turn -= 1
            elif ai_move == 'defend':
                ai_moved = 'block'
                print('Ai used iron defense!!!!!!!! +1000000 defense')
                whoose_turn -= 1
            elif ai_move == 'gas mask':
                ai_moved = 'mask'
                print("Ai put on a gas mask")
                whoose_turn -= 1

        if p_move == 'shot' and ai_moved != 'defend':
            print('YOU WON')
            done = True
        elif p_move == 'poison' and ai_moved != 'gas mask':
            print('YOU WON')
            done = True
        elif ai_moved == 'shot' and p_move != 'defend':
            print('YOU LOST')
            done = True
        elif ai_moved
