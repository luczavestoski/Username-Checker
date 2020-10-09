# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                     Version 2, December 2004 

#  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

#  Everyone is permitted to copy and distribute verbatim or modified 
#  copies of this license document, and changing it is allowed as long 
#  as the name is changed. 

#             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

#   0. You just DO WHAT THE FUCK YOU WANT TO.

# Developed by github.com/luczavestoski | knas#2222
# Most code from github.com/4-W/ByteChecker

import requests
import datetime
url = "https://r6.apitab.com/namecheck/"
available = "available.txt"
users = "usernames.txt"
now = datetime.datetime.now()

def count():
    namecount = 0
    with open(users) as f:
            for namecount, l in enumerate(f):
                pass
            namecount = namecount + 1


    return namecount

def check():
    with open(users, "r+") as fp:
        line = fp.readline()
        checked = 0
        f= open(available,"a+")
        f.write("\n----> Checking started! <---- \n")
        while line:
            name = line.strip()
            r = requests.get(url + name)
            status = r.json()
            if status["available"] == False:
                print(f"{name} [TAKEN]")
            if status["available"] == True:
                print(f"{name} is available!")
                f.write(f"{name}\n")

            line = fp.readline()
            if not line.strip():
                print("")
                print("Finished checking... Availalbe usernames in available.txt")
                f.write(f"----> Checking finished -")
                f.write(now.strftime('%l:%M:%S%p %A %b-%d-%Y'))
                f.write("<----\n")
                f.close()
                quit()


def initialize():
    print("Ubisoft Username Checker by github.com/luczavestoski")
    print("")
    print(f"{count()} usernames detected")
    print("Press ENTER to begin checking")
    input("")
    check()




 

if __name__ == "__main__":
    initialize()
