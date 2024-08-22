#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random as random


# In[8]:


cards_number = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
card_type = ['spades', 'hearts', 'clubs', 'diamonds']

full_deck = []
k=1
for j in card_type:
    for i in cards_number:
        full_deck.append([k,j,i])
        k += 1
        
full_deck_copy = full_deck.copy()


# In[9]:


number_of_players = 2
     
for i in range(number_of_players):
    # Create individual list variables
    exec(f"Player{i+1} = []")
    print(f"Player created : {i+1}")


# In[10]:


cards_assigned = []

for i in range(0,len(full_deck_copy)):
    if i % 2 == 0:
        Player1.append(full_deck_copy[random.randint(0,len(full_deck_copy)-1)])
        full_deck_copy.remove(Player1[-1])
    if i % 2 == 1:
        Player2.append(full_deck_copy[random.randint(0,len(full_deck_copy)-1)])
        full_deck_copy.remove(Player2[-1])


# In[13]:


print(Player1)
print(Player2)


# In[ ]:


## finding index number of a card in the full deck
def find_list_number(target,check):
    for i, lst in enumerate(check):
        if lst[0] == target:
            return i
        
# Player1[find_list_number(a1,Player1)] 
# full_deck[find_list_number(a1,full_deck)]
# find_list_number(20)


# In[ ]:


def turn1(a1,a2,a3,a4):
    a1 = int(input("choose card number A1:  "))
    a2 = int(input("choose card number A2--type 0 if throwing single card only:  "))
    a3 = int(input("choose card number A3--type 0 if throwing single card only:  "))
    a4 = int(input("choose card number A4--type 0 if throwing single card only:  "))
        
    print(f"PLayer1 threw {full_deck[find_list_number(a1,full_deck)]}")
    Player1.remove(Player1[find_list_number(a1,Player1)])
    
    if a2 > 0:
        print(f"PLayer1 threw {full_deck[find_list_number(a2,full_deck)]}")
        Player1.remove(Player1[find_list_number(a2,Player1)])
    if a3 > 0:
        print(f"PLayer1 threw {full_deck[find_list_number(a3,full_deck)]}")
        Player1.remove(Player1[find_list_number(a3,Player1)])
    if a4 > 0:
        print(f"PLayer1 threw {full_deck[find_list_number(a4,full_deck)]}")
        Player1.remove(Player1[find_list_number(a4,Player1)])
    if a2 or a3 or a4 == 0:
        pass
    else:
        pass
        
    
    
def turn2(b1,b2,b3,b4):
    b1 = int(input("choose card number B1:  "))
    b2 = int(input("choose card number B2--type 0 if throwing single card only:  "))
    b3 = int(input("choose card number B3--type 0 if throwing single card only:  "))
    b4 = int(input("choose card number B4--type 0 if throwing single card only:  "))
        
    print(f"PLayer2 threw {full_deck[find_list_number(b1,full_deck)]}")
    Player2.remove(Player2[find_list_number(b1,Player2)])
    
    if b2 > 0:
        print(f"PLayer2 threw {full_deck[find_list_number(b2,full_deck)]}")
        Player2.remove(Player2[find_list_number(b2,Player2)])
        
    if b3 > 0:
        print(f"PLayer2 threw {full_deck[find_list_number(b3,full_deck)]}")
        Player2.remove(Player2[find_list_number(b3,Player2)])
        
    if b4 > 0:
        print(f"PLayer2 threw {full_deck[find_list_number(b4,full_deck)]}")
        Player2.remove(Player2[find_list_number(b4,Player2)])
    if b2 or b3 or b4 == 0:
        pass
    
    else:
        pass


# In[ ]:


turn_number_limit = 100


# In[ ]:


for turn in range(0,turn_number_limit):
    if len(Player1) == len(Player2):
        print("PLayer1 turn")
        for card in Player1:
            print(card)
        turn1(a1,a2,a3,a4)
        print(f"cards with Player1 = {len(Player1)}")
        print("---------------------------------------------------------------------------------------------------")
        
    if len(Player1)==0 or len(Player2)==0:
        print("game ends")
        break
        
    if len(Player1) < len(Player2):
        print("PLayer2 turn")
        for card in Player2:
            print(card)
        turn2(b1,b2,b3,b4)
        print(f"cards with Player2 = {len(Player2)}")
        print("---------------------------------------------------------------------------------------------------")
        
    if len(Player1)==0 or len(Player2)==0:
        print("game ends")
        break
        
    else:
        pass


# In[22]:


## game conditions check

def who_starts(Player1, Player2): ## who will start the game, the one with clubs of 3
    starter = ""
    for j in range(0,13):
        if Player1[j][2]==3:
            for k in range(0,4):
                if Player1[j][1]=='clubs':
                    print("Player1 will start")
                    starter = 'Player2'
                    break
        if Player2[j][2]==3:
            for k in range(0,4):
                if Player2[j][1]=='clubs':
                    print("Player2 will start")
                    starter = 'Player2'
                    break
    return starter
    
def fresh_start(): ## for starting a fresh new turn after all players have passed
    print("")

def player_is_playing(): ## if player does not give pass
    print("")
    
def player_giving_pass(): ## for a player to give a pass
    print("")
    
def running_sequence(): ## check for the running sequence
    print("sequence") 
    
def sequence_break_check(): ## check if player is going above sequence
    print("")
    
def lower_card_check(): ## see if player doesn't throw a lower card than the current running highest card
    print("")
    
def game_ends(): ## game ends if a player has zero cards remaining
    print("")


# In[ ]:


game_ends = False


# In[ ]:


#### game loop

while game_ends not equal to True:
    if len(Player1)+len(Player2) == 52:
        who_starts(Player1,Player2)
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




