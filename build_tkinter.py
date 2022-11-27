from datetime import datetime
import pytz
from tkinter import *
from tkinter.ttk import *
import time
import threading
from tzlocal import get_localzone
# importing strftime function to
# retrieve system's time
from time import strftime

from pytz_deprecation_shim import timezone
# import for socket
import socket
HOST = "127.0.0.1" # Địa chỉ ip trỏ về máy chủ
SERVER_PORT = 65432 # > 50000 , Port 
FORMAT = "utf8"

def sendTimezone():
    _timezone = cmb1.get()
    # client.send(_timezone.encode(FORMAT))
    notSelect['text'] = "Selected Timezone"
    
    
root = Tk()
root.title("Timezone | Connected to " + HOST + ":" + str(SERVER_PORT))
root.geometry("800x550") # Size of the window
image_icon = PhotoImage(file="clock.png") 
root.iconphoto(False, image_icon)

def times():
    home = pytz.timezone(_timezone)
    local_time = datetime.now(home)
    string = local_time.strftime('%a %H:%M:%S %p %d-%m-%Y')
    lbl.config(text = string)
    # lbl.after(200, time)
    lbl.pack(anchor = 'center')
    l.pack()
    cmb1.pack()
    btnSelect.pack()
    
    home = pytz.timezone('Asia/Ho_Chi_Minh')
    local_time = datetime.now(home)
    current_time = local_time.strftime('%H:%M:%S')
    clock1.config(text = current_time)
    name1.config(text = "Ho Chi Minh")
    
    home = pytz.timezone('Asia/Hong_Kong')
    local_time = datetime.now(home)
    current_time = local_time.strftime('%H:%M:%S')
    clock2.config(text = current_time)
    name2.config(text = "Hong Kong")
    
    home = pytz.timezone('America/New_York')
    local_time = datetime.now(home)
    current_time = local_time.strftime('%H:%M:%S')
    clock3.config(text = current_time)
    name3.config(text = "New York")
    
    home = pytz.timezone('Asia/Tokyo')
    local_time = datetime.now(home)
    current_time = local_time.strftime('%H:%M:%S')
    clock4.config(text = current_time)
    name4.config(text = "Tokyo")
    root.after(200, times)
    # clock4.after(200, times)
name1 = Label(root, font = ("times", 20, 'bold'))
name1.place(x = 120, y = 200)
clock1 = Label(root, font = ('times', 25, 'bold'))
clock1.place(x = 130, y = 250)
nota1 = Label(root, text = "Hours Minutes Seconds", font = ("times", 15, 'bold'))
nota1.place(x = 100, y = 300)

name2 = Label(root, text = "jbfien", font = ("times", 20, 'bold'))
name2.place(x = 560, y = 200)
clock2 = Label(root,text='somthing here', font = ('times', 25, 'bold'))
clock2.place(x = 570, y = 250)
nota2 = Label(root, text = "Hours Minutes Seconds", font = ("times", 15, 'bold'))
nota2.place(x = 550, y = 300)

name3 = Label(root, font = ("times", 20, 'bold'))
name3.place(x = 130, y = 400)
clock3 = Label(root, font = ('times', 25, 'bold'))
clock3.place(x = 130, y = 450)
nota3 = Label(root, text = "Hours Minutes Seconds", font = ("times", 15, 'bold'))
nota3.place(x = 100, y = 500)

name4 = Label(root, font = ("times", 20, 'bold'))
name4.place(x = 590, y = 400)
clock4 = Label(root, font = ('times', 25, 'bold'))
clock4.place(x = 570, y = 450)
nota4 = Label(root, text = "Hours Minutes Seconds", font = ("times", 15, 'bold'))
nota4.place(x = 550, y = 500)


_timezone  = "Asia/Bangkok"
name = timezone(_timezone).zone
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
l = Label(root, text = "Current Time: " + name, font = ('calibri', 40, 'bold'))
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
labelcmb1 = Label(root, text = "Select Timezone", font = ('calibri', 20, 'bold'))
labelcmb1.place(x=30, y=125)
cmb1 = Combobox(root, values = pytz.all_timezones,width=50)
cmb1.place(x=200, y=150)
notSelect = Label(root,text="Not Selected", font = ('calibri', 20, 'bold'))
notSelect.place(x=570, y=125)
btnSelect = Button(root, text = "Select", command = sendTimezone)
# def time():
    
times()


root.mainloop()