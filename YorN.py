from colorama import *
from art import *
from bs4 import BeautifulSoup
import requests, os, json, time, datetime
from requests.api import request
os.system('cls')

good = "["+Fore.GREEN+"GOOD"+Fore.RESET+"] "
medium = "["+Fore.YELLOW+"MEDIUM"+Fore.RESET+"] "
bad = "["+Fore.RED+"BAD"+Fore.RESET+"] "

good_list = {
    "200",
    "204"
}
bad_liste = {
    "401",
    "403",
    "404",
    "500",
    "503",
    "504"
}
medium_list = {
    "301",def 
    "302"
}

def menu():
    tprint("YorN", "\n")
    try: # LIEN
        url_1 = input("First link /"+Fore.RED+"> "+Fore.RESET)
        url_2 = input("Second link /"+Fore.RED+"> "+Fore.RESET)
        url_3 = input("Third link /"+Fore.RED+"> "+Fore.RESET)


         # PREMIERE REQUETE POUR LE PREMIER LIEN
        r = requests.get(url_1)

        if r.status_code == "204" or "200":
            time.sleep(1)
            print("\n")
            print(good, url_1)
            
        elif r.status_code == "301" or "302":
            print(medium, url_1)

        elif r.status_code == bad_liste:
            print(bad, url_1)
            
        else:
            pass

        # DEUXIEME REQUETE POUR LE 2 EME LIEN
        b = requests.get(url_2)

        if b.status_code == "200" or "204":
            time.sleep(1)
            print(good, url_2)

        elif b.status_code == "301" or "302":
            print(medium, url_2)

        elif b.status_code == bad_liste:
            print(bad, url_2)

        else:
            pass

        c = requests.get(url_3) # TROISIEME REQUETS POUR LE TROISIEME LIEN

        if c.status_code == "200" or "204":
            time.sleep(1)
            print(good, url_3)
            

        elif c.status_code == "301" or "302":
            print(medium, url_3)

        elif c.status_code == bad_liste:
            print(bad, url_3)
            time.sleep(300)

        else:
            pass
 
    except:
        pass

menu()
time.sleep(300)
