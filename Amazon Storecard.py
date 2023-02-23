import random
import string
import os


#This Command Is Used To Clear Cards That Are Being Generated
#Import Random Is Used To Generate Cards Until It Gets A Valid Card Number

os.system('cls')
print(r"""
   _____                                      
  /  _  \   _____ _____  ____________   ____  
 /  /_\  \ /     \\__  \ \___   /  _ \ /    \ 
/    |    \  Y Y  \/ __ \_/    (  <_> )   |  \
\____|__  /__|_|  (____  /	/|___|  /
        \/      \/     \/      \/          \/ 
  _________ __                                               .___
 /   _____//  |_  ___________   ____   ____ _____ _______  __| _/
 \_____  \\   __\/  _ \_  __ \_/ __ \_/ ___\\__  \\_  __ \/ __ | 
 /        \|  | (  <_> )  | \/\  ___/\  \___ / __ \|  | \/ /_/ | 
/_______  /|__|  \____/|__|    \___  >\___  >____  /__|  \____ | 
        \/                         \/     \/     \/           \/ 
  ________                                   __                
 /  _____/  ____   ____   ________________ _/  |_  ___________ 
/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
\    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
 \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/     \/     \/     \/           \/                   """)
print("How Many Store Cards Would You Like To Generate?")
amount = int(input())


# erase
erase = open("output.txt", "w")
erase.write("")



#open and write to a file
file = open("output.txt", "a")


for i in range(amount):
 #rng setup
 S = 8
 ran = ''.join(random.choices(string.digits, k=S))
 file.write('60457811' + str(ran) +'\n')
