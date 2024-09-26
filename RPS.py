import random
import time as t

b = ['rock', 'paper', 'scissors']
difficulty = ['cakewalk','kid','men','nightmare']
health_player = 100
health_bot = 100
cakewalk_bothealth = 20
kid_bothealth = 50
men_bothealth = 100
nightmare_bothealth = 200
state = ''
poll = ['y','n','yes','no']
t.sleep(1)
print('Made by igen-kolhs')
t.sleep(1)
print('\nWelcome to Simple Rock, Paper, Scissors game.')
t.sleep(1)



def reset_game():
    global health_player, health_bot, state, d, e
    health_player = 100
    health_bot = 0
    state = ''

def bot_choice():
    global comp_choice
    if mode_query == 'cakewalk':
        comp_choice = random.choices(['rock', 'paper', 'scissors'], weights=[0.1, 0.8, 0.1], k=1)[0]
    elif mode_query == 'kid':
        comp_choice = random.choices(['rock', 'paper', 'scissors'], weights=[0.2, 0.6, 0.2], k=1)[0]
    elif mode_query == 'men':
        comp_choice = random.choices(['rock', 'paper', 'scissors'], weights=[0.3, 0.3, 0.4], k=1)[0]
    elif mode_query == 'nightmare':
        comp_choice = random.choice(b)


def checkempty(a, b):
    while a not in b:
        a = input('Please write a valid choice: ')
    return a

def gamemode():
    global mode_query
    mode_query = input('\nChoose the difficulty - [cakewalk, kid, men, nightmare] : ').lower()
    while mode_query not in difficulty:
        mode_query = input('\nPlease choose valid difficulty - [cakewalk, kid, men, nightmare] : ').lower()

gamemode()
    
def health():
    global health_bot
    if mode_query == 'cakewalk':
        health_bot = cakewalk_bothealth
    elif mode_query == 'kid':
        health_bot = kid_bothealth
    elif mode_query == 'men':
        health_bot = men_bothealth
    elif mode_query == 'nightmare':
        health_bot = nightmare_bothealth

health()

def mainfnc():
    global state, health_player, health_bot, d, e
    if a == 'rock':
        if comp_choice == 'rock':
            state = 'tie'
        elif comp_choice == 'paper':
            state = 'lose'
            health_player -= d
        elif comp_choice == 'scissors':
            state = 'win'
            health_bot -= e
    elif a == 'paper':
        if comp_choice == 'rock':
            state = 'win'
            health_bot -= e    
        elif comp_choice == 'paper':
            state = 'tie'
        elif comp_choice == 'scissors':
            state = 'lose'
            health_player -= d
    elif a == 'scissors':
        if comp_choice == 'rock':
            state = 'lose'
            health_player -= d   
        elif comp_choice == 'paper':
            state = 'win'
            health_bot -= e
        elif comp_choice == 'scissors':
            state = 'tie'

def playerhealthcheck():
    global health_player
    if health_player > 0 and health_player <= 40:
        print('Low Player HP, Be careful.')
    elif health_player <= 0:
        print('\nGame Over\n\nYou Lose\n')
        return 'lose'
    

def bothealthcheck():
    global health_bot
    if health_bot > 0 and health_bot <= 40:
        print('Low Bot HP, This is your time to win.')
    elif health_bot <= 0:
        print('\nGame Over\n\nYou Win\n')
        return 'win'

def damagecheck():
    if a != comp_choice:
        if state == 'win':
            print('\nYou gave', e, 'damage to the bot')
        elif state == 'lose':
            print('\nBot gave', d, 'damage to the player')
    else:
        print('\nNothing Happened')

def hitcheck():
    global d, e
    if mode_query == 'cakewalk':
        d = random.randint(10, 15)
        e = random.randint(20, 40)
    elif mode_query == 'kid':
        d = random.randint(10, 20)
        e = random.randint(10, 40)
    elif mode_query == 'men':
        d = random.randint(10, 40)
        e = random.randint(10, 40)
    elif mode_query == 'nightmare':
        d = random.randint(25, 40)
        e = random.randint(10, 20)
    if health_player < d:
        d = health_player
    if health_bot < e:
        e = health_bot

def play():
    global a,health_bot,health_player,mode_query,comp_choice
    while True:
        bot_choice()
        hitcheck()
        t.sleep(1)
        print('\nYour HP:', health_player)
        print('Bot HP:', health_bot)

        if playerhealthcheck() == 'lose' or bothealthcheck() == 'win':
            break
        t.sleep(1)
        a = input("\nWrite your choice: ").lower()
        a = checkempty(a, b)

        t.sleep(1)
        print('\nYou:', a)
        print('Bot:', comp_choice)
    
        mainfnc()
        damagecheck()

while True:

    play()
    t.sleep(2)
    restart_prompt = input('Do you want to play again ? (Y / N) : ').lower()
    while restart_prompt not in poll:
        t.sleep(1)
        restart_prompt = input('\nWrite Y for Yes, and N for No : ').lower()
    if restart_prompt == 'yes' or restart_prompt == 'y':
        reset_game()
        gamemode()
        health()
    elif restart_prompt == 'no' or restart_prompt == 'n':
        print('\nThanks for Playing.\n')
        exit()

