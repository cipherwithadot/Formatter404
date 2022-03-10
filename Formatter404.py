import threading
import random
import json
import time
from termcolor import colored

TokensFull=open('Input.txt','r').read().splitlines()
count=0
for TokenFull in TokensFull:
	count+=1
print("""


\033[1;36;40m███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░████████╗░░██╗██╗░█████╗░░░██╗██╗
██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗╚══██╔══╝░██╔╝██║██╔══██╗░██╔╝██║
█████╗░░██║░░██║██████╔╝██╔████╔██║███████║░░░██║░░░██╔╝░██║██║░░██║██╔╝░██║
██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║░░░██║░░░███████║██║░░██║███████║
██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║░░░██║░░░╚════██║╚█████╔╝╚════██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░░░╚═╝░╚════╝░░░░░░╚═╝
\033[1;31;40mMade By Social404 | Cracked by Traumatism | Published By Critical\033[0;37;40m
""")
print(f"""

\033[1;33;40m{count} Tokens Loaded From Input.txt :O

""")

Answer = input("Would You Like To Format The Tokens From Email:Pass:Token Format To Token Format? | Y/N \n --> ")

def formatter(TokenFull):
	len(TokenFull.split(':')) == 4
	splitted = TokenFull.split(':')
	email = f"{splitted[0]}"
	password = f"{splitted[1]}"
	token = f"{splitted[2]}"
	with open("Output.txt", "a") as f:
		f.write(f"{token}\n")
		f.close()


if Answer == "Y" or Answer == "y":
	for TokenFull in TokensFull:threading.Thread(target=formatter,args=(TokenFull,)).start()
else:
	print("For Requests Of Other Options / Tools Contact Us On Tokens404.com but i like to ignore you :)  -Social404")

input(f"\033[1;32;40m{count} Tokens Formatted | For Requests Of Other Options / Tools Contact Us On Tokens404.com but i like to ignore you :)  -Social404 | Your Tokens Are In The Output.txt File")
