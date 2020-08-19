#!/usr/bin/env python
import os
import subprocess
import nmap
import sys
import time

from subprocess import check_call

print("\nWelcome!!")
print("\n")
cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")
cmd = os.system("sleep 3 && clear")


def intro():
    cmd = os.system("clear")
    print("""\033[1;32m
---------------------------------------------------------------------------------------
\033[0m  ██████████╗ ██    ██   ██╗ ██████    ██ ██████╗ ████████╗
\033[0m  ██╔════╝██╔═██╗   ██╔══██╗  ██  ██═══██ █╔════╝    ██╔════╝
\033[0m  ██████████║ ████████║  ██║  ██║  █   ██ ███████    ██║     
\033[0m  ██║     ║   ██║   ██║  ██║  ██    █  ██╔█══╝  ╚════██║     
\033[0m ╚██╔╝        ██    ██╔╝ ██   ██     ████╗███████║   ██      
\033[0m  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝  
                                                        
---------------------------------------------------------------------------------------                                                                     
(1)metasploit      
(2)airmon-ng                        
(3)armitage                           
(4)burpsuite  
(5)nmap                  
(6)maltego
(7)Recon-ng
(8)medusa
(9)wireshark                                     
(10)Faraday IDE
(11)aircrack-ng
(12)wifite
(13)crunch
(14)Install more tools


(0)About usr/share/metasploit-framework/service postgresql start && msfdb init && msfconsole start {} Phinet
(00)Exit
-----------------------------------------------------------------------
""")
    print("\nEnter your choice here : !# ")
    var = int(input(""))
    if var == 1:
        order = "msfconsole start {} "
        geny = os.system(order)
        intro()
    elif var == 2:
        order = "msfconsole start {} "
        geny = os.system(order)
        intro()
    elif var == 3:
        order = "armitage start {} "
        geny = os.system(order)
        intro()
    elif var == 4:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 5:
        print("Installing Requirements...")
        os.system("sudo apt-get install figlet")
        os.system("pkg install figlet")
        # Figlet installed
        os.system("sudo apt-get install nmap")
        os.system("pkg install nmap")
        # Nmap installed

        os.system("clear")
        os.system("figlet -f slant NMAP AUTOMATE")
        print("----------------------------------------------------")
        print("")
        print("[1] Scan A Website ")
        print("[2] Scan a ip Address")
        print("[3] Advanced Options")
        print("[4] About The Tool")
        print("")
        print("[99] Exit")
        print("")
        op = int(input(""))

        def logo():
            os.system("figlet -f slant NMAP AUTOMATE")

        def cls():
            os.system("clear")

        if op == 1:
            cls()
            logo()
            print("")
            website = input("Which Website You want To Scan : ")
            os.system("nmap -v -A %s" % website)

        elif op == 2:
            cls()
            logo()
            print("")
            wep = input("Which Ip Do You Want To Scan :")
            os.system("nmap -v -sn %s" % wep)

        elif op == 3:
            cls()
            logo()
            print("These Are Some Advanced Options From Nmap...")
            time.sleep(1)
            os.system("nmap")
            print("You Can use The By Typing 'Nmap <Option>'")
            time.sleep(2)
            exit()

        elif op == 99:
            cls()
            logo()
            print("Sure! Quiting.... Hope U Liked")
            sys.exit()

        elif op == '4':
            cls()
            os.system("figlet -f slant About")
            print()
            print(
                "This Tools Is Made For The Newbie That Do Not Know How to use Nmap The Hacking Tools Because The Nmap has a Litle Difficul Statements To Exexute Them By This Tools You Do Not Have To Write  Any Statements You Can Exexute Nmap and Scan Websites By Just Writing The Name Of The Website/Ip Advanced Options are also there For Some Experts")
            print("")
            print("Author       -> Sarthak")
            print("Posted on    -> Github")
            print("Authors Age  -> 11 Years")
            print("Intrested in -> Cyber Security,Ethical Hacking,Tech")
            print("")

        else:
            print("\n[!] ERROR : Wrong Input")
            time.sleep(1)
        intro()
    elif var == 6:
        order = "maltego start{} "
        geny = os.system(order)
        intro()
    elif var == 7:
        order = "usr/share/metasploit-framework/msfconsole start {} "
        geny = os.system(order)
        intro()
    elif var == 8:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 9:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 10:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 11:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 12:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 13:
        order = "metasploit start {} "
        geny = os.system(order)
        intro()
    elif var == 14:
        def wire():
            cmd = os.system("clear")
            print("""
1) Aircrack-ng                          17) kalibrate-rtl
2) Asleap                               18) KillerBee
3) Bluelog                              19) Kismet
4) BlueMaho                             20) mdk3
5) Bluepot                              21) mfcuk
6) BlueRanger                           22) mfoc
7) Bluesnarfer                          23) mfterm
8) Bully                                24) Multimon-NG
9) coWPAtty                             25) PixieWPS
10) crackle                             26) Reaver
11) eapmd5pass                          27) redfang
12) Fern Wifi Cracker                   28) RTLSDR Scanner
13) Ghost Phisher                       29) Spooftooph
14) GISKismet                           30) Wifi Honey
15) Wifitap                             31) gr-scan
16) Wifite                              32) Back to main menu
90) airgeddon
91) wifite v2

0)install all wireless tools
""")
            w = int(input("Enter The number of the tool : >>> "))
            if w == 1:
                cmd = os.system("sudo apt-get update && apt-get install aircrack-ng")
            elif w == 90:
                print(
                    "sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
            elif w == 91:
                print("sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.git")
            elif w == 2:
                cmd = os.system("sudo apt-get update && apt-get install asleep")
            elif w == 3:
                cmd = os.system("sudo apt-get update && apt-get install bluelog")
            elif w == 4:
                cmd = os.system("sudo apt-get update && apt-get install bluemaho")
            elif w == 5:
                cmd = os.system("sudo apt-get update && apt-get install bluepot")
            elif w == 6:
                cmd = os.system("sudo apt-get update && apt-get install blueranger")
            elif w == 7:
                cmd = os.system("sudo apt-get update && apt-get install bluesnarfer")
            elif w == 8:
                cmd = os.system("sudo apt-get update && apt-get install bully")
            elif w == 9:
                cmd = os.system("sudo apt-get update && apt-get install cowpatty")
            elif w == 10:
                cmd = os.system("sudo apt-get update && apt-get install crackle")
            elif w == 11:
                cmd = os.system("sudo apt-get update && apt-get install eapmd5pass")
            elif w == 12:
                cmd = os.system("sudo apt-get update && apt-get install fern-wifi-cracker")
            elif w == 13:
                cmd = os.system("sudo apt-get update && apt-get install ghost-phisher")
            elif w == 14:
                cmd = os.system("sudo apt-get update && apt-get install giskismet")
            elif w == 15:
                cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
            elif w == 16:
                cmd = os.system("sudo apt-get update && apt-get install kalibrate-rtl")
            elif w == 17:
                cmd = os.system("sudo apt-get update && apt-get install killerbee-ng")
            elif w == 18:
                cmd = os.system("sudo apt-get update && apt-get install kismet")
            elif w == 19:
                cmd = os.system("sudo apt-get update && apt-get install mdk3")
            elif w == 20:
                cmd = os.system("sudo apt-get update && apt-get install mfcuk")
            elif w == 21:
                cmd = os.system("sudo apt-get update && apt-get install mfoc")
            elif w == 22:
                cmd = os.system("sudo apt-get update && apt-get install mfterm")
            elif w == 23:
                cmd = os.system("sudo apt-get update && apt-get install multimon-ng")
            elif w == 24:
                cmd = os.system("sudo apt-get update && apt-get install pixiewps")
            elif w == 25:
                cmd = os.system("sudo apt-get update && apt-get install reaver")
            elif w == 26:
                cmd = os.system("sudo apt-get update && apt-get install redfang")
            elif w == 27:
                cmd = os.system("sudo apt-get update && apt-get install rtlsdr-scanner")
            elif w == 28:
                cmd = os.system("sudo apt-get update && apt-get install spooftooph")
            elif w == 29:
                cmd = os.system("sudo apt-get update && apt-get install wifi-honey")
            elif w == 30:
                cmd = os.system("sudo apt-get update && apt-get install wifitap")
            elif w == 31:
                cmd = os.system("sudo apt-get update && apt-get install wifite")
            elif w == 32:
                intro()
            elif w == 0:
                cmd = os.system(
                    "apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
            else:
                print("Not Found")
            wire()

        wire()
    elif var == 0:
        cmd = os.system("clear")
        print("""
This code was written in phinet 

""")
        quit()
    elif var == 00:
        exit()


intro()
