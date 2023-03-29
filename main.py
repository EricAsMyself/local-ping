import os
# typo error in import
import subprocess
import speedtest  
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.cleanup()



st = speedtest.Speedtest()

A = 8
B = 6
C = 26
D = 19
E = 13
F = 7
G = 16
H = 20

D1 = 21
D2 = 12
D3 = 5
D4 = 11

for x in [D1,D2,D3,D4]:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x, GPIO.HIGH)

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(H, GPIO.OUT)

GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.HIGH)



def num_and_letter(num, char):
    print('hello')
    

def download_format (num):
    if num < 10000000:
        print(str(round((num/100000),2)) + "Kb/s")
    elif num < 10000000000:
        print(str(round((num/1000000),2)) + "Mb/s")
    elif num < 10000000000000:
        print(str(round((num/1000000000),2)) + "Gb/s")

def display_letter(letter, place):
        print(f"{letter=}, {place=}")
        to_alphabet = {
        " ": [],
        "A": [A,B,F,C,E,G],
        "B": [A,B,C,D,E,F,G],
        "C": [A,D,E,F],
        "D": [A,B,C,D,E,F],
        "E": [A,D,E,F,G],
        "F": [A,B,E,F,G],
        "G": [A,B,C,D,F,G],
        "H": [B,C,E,F,G,H],
        "I": [E,F],
        "J": [B,C,D,E],
        "K": [B,C,E,F,G],
        "L": [D,E,F],
        "M": [A,B,C,E,F],
        "N": [A,B,C,E,F],
        "O": [A,B,C,D,E,F],
        "P": [A,B,E,F,G],
        "Q": [A,B,C,D,E,F,H],
        "R": [A,B,C,E,F,G,H],
        "S": [A,C,D,F,G],
        "T": [E,F,G],
        "U": [B,C,D,E,F],
        "V": [B,C,D,E,F],
        "W": [B,C,D,E,F],
        "X": [B,C,D,E,F],
        "Y": [F,B,G,C],
        "Z": [A,C,D,F,G],
        "1": [E,F],
        "2": [A,B,D,E,G],
        "3": [A,B,C,D,G],
        "4": [B,C,F,G],
        "5": [A,C,D,F,G],
        "6": [A,C,D,E,F,G],
        "7": [A,B,C],
        "8": [A,B,C,D,E,F,G],
        "9": [A,B,C,F,G],
        "0": [A,B,C,D,E,F],
        ".": [H]
        }
        GPIO.output(place, GPIO.LOW)
        for my_char in to_alphabet[letter]:
            print(my_char)
            GPIO.output(my_char, GPIO.HIGH)



def display(str_disp):
    old_disp = str_disp.upper()
    while True:
        # length = 4
        str_disp = old_disp
        for x in range(len(str_disp) + 4):
            new_str = str_disp[:4]
            print(new_str)
            reset()
            start_time = time.time()
            while (time.time() - start_time) < 2:
                display_letter(new_str[0], D4)
                reset()
                display_letter(new_str[1], D3)
                reset()
                display_letter(new_str[2], D2)
                reset()
                display_letter(new_str[3], D1)
                reset()
            # time.sleep(0.2)
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
    
def reset():
    for new_place in [D1,D2,D3,D4]:
        GPIO.output(new_place, GPIO.HIGH)
    for x in [A,B,C,D,E,F,G,H]:
        GPIO.output(x, GPIO.LOW)

if __name__ == "__main__":
    print("starting")
    # setcode()
    # while True:
    #     for x in ["A","B","C","D","8", "1"]:
    #         for place in [D1,D2,D3,D4]:
    #             display_letter(x, place)
    #             time.sleep(1)
    #             for new_place in [D1,D2,D3,D4]:
    #                 GPIO.output(new_place, GPIO.HIGH)
    #         time.sleep(1)
            
    #         for x in [A,B,C,D,E,F,G,H]:
    #             GPIO.output(x, GPIO.LOW)

    #     break
    # GPIO.cleanup()
    display('Here is the new one that I found.')
