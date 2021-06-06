import tkinter as tk
from tkinter import*
from tkinter import filedialog as fd
from main import *

#This is GUI based to download Youtube Videos.
    

def down():
    downlink = urlentry.get()
    qualiti = qualentry.get()
    filename = fd.askdirectory(initialdir='/',title="Save")
    url = downlink
    path = filename+"/"

    try:
        link = pytube.YouTube(url)
        print("Connection Success")
    except:
        print("Connection Error")

    dvid = link.streams.get_by_resolution(qualiti)
    dvid.download(path)
    print("Complete Download")

def downloadsong():
    downlink = urlentry.get()
    filename = fd.askdirectory(initialdir='/',title="Save To")
    path = filename+"/"
    url = downlink

    try:
        link = pytube.YouTube(url)
        print("connection To Youtube success")
    except:
        print("Connection Error")

    sdown = link.streams.get_audio_only()
    sdown.download(path)
    print("Song Downloaded")

    

root = tk.Tk()
root.title("YOUTUBE VIDEO DOWNLOADER | DEVELOPED BY SURAJKR2456")
root.minsize(500,500)

label = Label(root, text = "YOUTUBE VIDEO DOWNLOADER", font = ("Arial", 30),fg='blue')

urlgui = Label(root,text = "Url of YT Video :",fg='red')
urlentry = Entry(root,bd=2,width=80,)


quality = Label(root,text = "Enter Quality (360p/480p/720p/1080p) :",fg='red')
qualentry = Entry(root,bd=2,width=20,)

downbtn = Button(root,text="Download Video",width=60,bg='red',command=down,fg='white')

songdownbtn = Button(root,text="Download Audio Only(Song)",width=60,bg='cyan',fg='red',command=downloadsong)


label.pack()

urlgui.pack()
urlentry.pack()


quality.pack()
qualentry.pack()

downbtn.pack()
songdownbtn.pack()

root.mainloop()
