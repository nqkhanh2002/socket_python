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




root = Tk()
root.title("Timezone | Connected to " + HOST + ":" + str(SERVER_PORT))
root.geometry("800x200")
image_icon = PhotoImage(file="socket_python\clock.png")
root.iconphoto(False, image_icon)

_timezone = "Asia/Ho_Chi_Minh"
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
btnSelect = Button(root, text = "Select")

def time():
    home = pytz.timezone(_timezone)
    local_time = datetime.now(home)
    string = local_time.strftime('%a %H:%M:%S %p %d-%m-%Y')
    lbl.config(text = string)
    lbl.after(1000, time)
    lbl.pack(anchor = 'center')
    l.pack()
    cmb1.pack()
    btnSelect.pack()
time()

# Styling the label widget so that clock
# will look more attractive

# cmb1.grid(row=0,column=0)
# btnSelect.grid(row=0,column=1)

# time()
root.mainloop()