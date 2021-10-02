import sys
from colorama import Fore
from Module import Help
from Module import instagram
from Module import instafollower
from Module import steam
from Module import google
from Module import wordpress

while True:
    try:
        Help.Banner()
        Help.list1()
        num = input("╰> ")
    except:
        print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
        sys.exit()
    if num == "04":
        print(f"\n {Fore.LIGHTMAGENTA_EX}Good Luck :)")
        sys.exit()
    elif num == "4":
        print(f"\n {Fore.LIGHTMAGENTA_EX}Good Luck :)")
        sys.exit()    
    elif num == "03":
       Help.list4()
    elif num == "3":
       Help.list4()       
    elif num == "":
        print(f"{Fore.WHITE}Please Enter Number:")
        input("Press Enter... ")
    elif num == "02":
        Help.list5()
    elif num == "2":
        Help.list5()
    elif num == "01":
        try:
            Help.list2()
            fake = input("╰> ")
        except:
            print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
            sys.exit()
        if fake == "01":# instagram
            try:
                Help.Banner()
                Help.list3()
                ins = input("╰> ")
            except:
                print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
                sys.exit()
            if ins == "01": #orginal
                instagram.main()
            elif ins == "1":
                instagram.main()
            elif ins == "02":#follower
                instafollower.main()
            elif ins == "2":
                instafollower.main()
            else:
                print()
        elif fake == "1":
            try:
                Help.Banner()
                Help.list3()
                ins = input("╰> ")
            except:
                print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
                sys.exit()
            if ins == "01": #orginal
                instagram.main()
            elif ins == "1":
                instagram.main()
            elif ins == "02":#follower
                instafollower.main()
            elif ins == "2":
                instafollower.main()
            else:
                print()
        elif fake == "02":
            google.main()
        elif fake == "2":
            google.main()
        elif fake == "03":
            steam.main()
        elif fake == "3":
            steam.main()
        elif fake == "04":
            wordpress.main()
        elif fake == "4":
            wordpress.main()
        else:
            print()
    elif num == "1":
        try:
            Help.list2()
            fake = input("╰> ")
        except:
            print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
            sys.exit()
        if fake == "01":# instagram
            try:
                Help.Banner()
                Help.list3()
                ins = input("╰> ")
            except:
                print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
                sys.exit()
            if ins == "01": #orginal
                instagram.main()
            elif ins == "1":
                instagram.main()
            elif ins == "02":#follower
                instafollower.main()
            elif ins == "2":
                instafollower.main()
            else:
                print()
        elif fake == "1":
            try:
                Help.Banner()
                Help.list3()
                ins = input("╰> ")
            except:
                print(f"\n{Fore.LIGHTYELLOW_EX}You are kick From App")
                sys.exit()
            if ins == "01": #orginal
                instagram.main()
            elif ins == "1":
                instagram.main()
            elif ins == "02":#follower
                instafollower.main()
            elif ins == "2":
                instafollower.main()
            else:
                print()
        elif fake == "02":
            google.main()
        elif fake == "2":
            google.main()
        elif fake == "03":
            steam.main()
        elif fake == "3":
            steam.main()
        elif fake == "04":
            wordpress.main()
        elif fake == "4":
            wordpress.main()
        else:
            print()
    
    
            