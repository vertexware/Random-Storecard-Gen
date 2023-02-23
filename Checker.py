import random
import string
import os

#Clear The Amount Of Cards You Have
os.system('cls')
print("How Much Storecards Does The Client Expect You To Have?")
amount = input()

# clear
os.system('cls')


# title screen <3
print(r"""
 _____                                      
  /  _  \   _____ _____  ____________   ____  
 /  /_\  \ /     \\__  \ \___   /  _ \ /    \ 
/    |    \  Y Y  \/ __ \_/    (  <_> )   |  \
\____|__  /__|_|  (____  /_____ \____/|___|  /
        \/      \/     \/      \/          \/ 
  _________ __                                               .___
 /   _____//  |_  ___________   ____   ____ _____ _______  __| _/
 \_____  \\   __\/  _ \_  __ \_/ __ \_/ ___\\__  \\_  __ \/ __ | 
 /        \|  | (  <_> )  | \/\  ___/\  \___ / __ \|  | \/ /_/ | 
/_______  /|__|  \____/|__|    \___  >\___  >____  /__|  \____ | 
        \/                         \/     \/     \/           \/ 
_________ .__                   __                 
\_   ___ \|  |__   ____   ____ |  | __ ___________ 
/    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
\     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
 \______  /___|  /\___  >\___  >__|_ \\___  >__|   
        \/     \/     \/     \/     \/    \/     
                """)

# rng setup
S = 3
ran = ''.join(random.choices(string.digits, k=S))

#Gets Card Number
print("Input Storecard Number: ")
numer = input()

#Balance Viewer
print('Storecards Value ' + numer + ' is ' + amount + str(ran) + '$')
input("Press Enter To Exit")
