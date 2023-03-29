import os
# typo error in import
import subprocess
import speedtest  
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)


st = speedtest.Speedtest()

A = 8
B = 12
C = 26
D = 19
E = 13
F = 7
G = 6
H = 5

# * D4
# * D3 - GPIO 05
# * D2 -GPIO 06
# * DP - GPIO 20
# * D1 - GPIO 21


def num_and_letter(num, char):
    print('hello')
    

def download_format (num):
    if num < 10000000:
        print(str(round((num/100000),2)) + "Kb/s")
    elif num < 10000000000:
        print(str(round((num/1000000),2)) + "Mb/s")
    elif num < 10000000000000:
        print(str(round((num/1000000000),2)) + "Gb/s")

def display_letter(letter):
        to_alphabet = {
        " ": "",
        "A": "ABFCEG",
        "B": "ABCDEFG",
        "C": "ADEF",
        "D": "ABCDEF",
        "E": "ADEFG",
        "F": "ABEFG",
        "G": "ABCDFG",
        "H": "BCEFGH",
        "I": "EF",
        "J": "BCDE",
        "K": "BCEFG",
        "L": "DEF",
        "M": "ABCEF",
        "N": "ABCEF",
        "O": "ABCDEF",
        "P": "ABEFG",
        "Q": "ABCDEFH",
        "R": "ABCEFGH",
        "S": "ACDFG",
        "T": "EFG",
        "U": "BCDEF",
        "V": "BCDEF",
        "W": "BCDEF",
        "X": "BCDEF",
        "Y": "FBGC",
        "Z": "ACDFG",
        "1": "EF",
        "2": "ABDEG",
        "3": "ABCDG",
        "4": "BCFG",
        "5": "ACDFG",
        "6": "ACDEFG",
        "7": "ABC",
        "8": "ABCDEFG",
        "9": "ABCFG",
        "0": "ABCDEF",
        ".": "H"
        }



def display(str_disp):
    old_disp = str_disp
    while True:
        # length = 4
        str_disp = old_disp
        for x in range(len(str_disp) + 4):
            print(str_disp[:4])
            time.sleep(0.2)
            str_disp =  str_disp[1:]
            str_disp += " "
        



def setcode():

    
    ip_addresses = {
        "192.168.1.10": "TRUENAS",
        "192.168.1.11": "UNIFI",
        "192.168.1.23": "HOMEBRIDGE"
    }

    connect = {}
    disconnected = {}
    
    # for ping in range(1,10):
    for address in ip_addresses:
        res = subprocess.call(['ping', '-c', '3', address])
        if res == 0:
            connect[address] = ip_addresses[address]
        elif res == 2:
            disconnected[address] = ip_addresses[address]
        else:
            print("ping to", address, "failed!")
    for x in connect:
        print('connected '  + connect[x])
    for x in disconnected:
        print('connected ' + connect[x])
    down = st.download()
    download_format(down)
    


if __name__ == "__main__":
    print("starting")
    # setcode()
    display('Here is the new one that I found.')
