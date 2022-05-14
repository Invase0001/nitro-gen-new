# nitro lol
import os
import time
import numpy
from sty import fg, bg, ef, rs
import requests
import string


def checkCode(code: str) -> bool:
    t = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    r = requests.get(t)
    if r.status_code == 200:
        return True
    else:
        return False

gg = f"""

{fg(26)}         /$$                                      /$$   /$$                        
{fg(62)}        |__/                                     |__/  | $$                        
{fg(98)}         /$$ /$$$$$$$  /$$    /$$       /$$$$$$$  /$$ /$$$$$$    /$$$$$$   /$$$$$$ 
{fg(134)}        | $$| $$__  $$|  $$  /$$/      | $$__  $$| $$|_  $$_/   /$$__  $$ /$$__  $$
{fg(170)}        | $$| $$  \ $$ \  $$/$$/       | $$  \ $$| $$  | $$    | $$  \__/| $$  \ $$
{fg(207)}        | $$| $$  | $$  \  $$$/        | $$  | $$| $$  | $$ /$$| $$      | $$  | $$
{fg(206)}        | $$| $$  | $$   \  $/         | $$  | $$| $$  |  $$$$/| $$      |  $$$$$$/
{fg(201)}        |__/|__/  |__/    \_/          |__/  |__/|__/   \___/  |__/       \______/ 
                                                                                  

"""
print(gg)
time.sleep(3)
os.system('cls')
time.sleep(2)
s = input(f"{fg(200)}How many codes\n")
chars = []
chars[:0] = string.ascii_letters + string.digits

c = numpy.random.choice(chars, size=[int(s), 23])
invalid = 0
success = 0
error = 0
for s in c:  # Loop over the amount of codes to check
    try:
        code = ''.join(x for x in s)
        url = f"https://discord.gift/{code}"  # Generate the url

        if checkCode(url) == True:
            print(f"{fg(206)}> YES | {url}\n")
            success = success + 1
        else:
            print(f"{fg(124)}> NO | {url}\n")
            invalid = invalid + 1



    except KeyboardInterrupt:
        # If the user interrupted the program
        print("\nInterrupted by user")
        break  # Break the loop

    except Exception as e:  # If the request fails
        error = error + 1
time.sleep(2)
print(f"{fg(208)} Ended process! Success: {success} Invalid: {invalid} Error: {error}")
time.sleep(6)
