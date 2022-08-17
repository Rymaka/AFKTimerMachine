import os
import time
from turtle import color
from tkinter import *
from tkinter.scrolledtext import *
import threading
import ctypes


root = Tk()             
root.wm_title("Friendly AFK timer")
# Open window having dimension 600x500 and red colour
root.geometry('300x200')
root.minsize(300,200)
root.maxsize(300,200)
root.configure(bg='black')
#In instant start is needed make it "True"
running = False
#interfaces
wifi_name = 'WLAN'
eth0_name = "Ethernet 0"
eth_name = "Ethernet"
eth1_name = "Ethernet 1"
eth2_name = "Ethernet 2"
eth3_name = "Ethernet 3"
#running state
running = False

#Try to disable_internet_all and lock PC by WIN+L
def disable_internet_all():
    global wifi_name
    global eth0_name 
    global eth_name
    global eth1_name
    global eth2_name
    global eth3_name
    #cmd commands for wifi, eth1-3   
    disable_wifi = 'netsh interface set interface "'+wifi_name+'" disabled'
    disable_eth = 'netsh interface set interface "'+eth_name+'" disabled'
    disable_eth0 = 'netsh interface set interface "'+eth0_name+'" enabled'
    disable_eth1 = 'netsh interface set interface "'+eth1_name+'" disabled'
    disable_eth2 = 'netsh interface set interface "'+eth2_name+'" disabled'
    disable_eth3 = 'netsh interface set interface "'+eth3_name+'" disabled'
    
    #try to disable wi-fi interface
    try:
     os.popen(disable_wifi)    
    except: 
     pass
    #try to disable_eth
    try:
     os.popen(disable_eth)    
    except: 
     pass
    #try to disable_eth0
    try:
     os.popen(disable_eth0)    
    except: 
     pass
    #try to disable_eth1
    try:
     os.popen(disable_eth1)    
    except: 
     pass
    #try to disable_eth2
    try:
     os.popen(disable_eth2)    
    except: 
     pass
    #try to disable_eth3
    try:
     os.popen(disable_eth3)    
    except: 
     pass
    ctypes.windll.user32.LockWorkStation()

         
#Try to enable_internet_all
def enable_internet_all():
    global wifi_name
    global eth0_name 
    global eth_name
    global eth1_name
    global eth2_name
    global eth3_name
   #cmd commands for wifi, eth1-3
    enable_wifi = 'netsh interface set interface "'+wifi_name+'" enabled'
    enable_eth = 'netsh interface set interface "'+eth_name+'" enabled'
    enable_eth0 = 'netsh interface set interface "'+eth0_name+'" enabled'
    enable_eth1 = 'netsh interface set interface "'+eth1_name+'" enabled'
    enable_eth2 = 'netsh interface set interface "'+eth2_name+'" enabled'
    enable_eth3 = 'netsh interface set interface "'+eth3_name+'" enabled'
        #try to enable wi-fi interface
    try:
     os.popen(enable_wifi)    
    except: 
     pass
    #try to enable_eth
    try:
     os.popen(enable_eth)    
    except: 
     pass
    #try to enable_eth0
    try:
     os.popen(enable_eth0)    
    except: 
     pass
    #try to enable_eth1
    try:
     os.popen(enable_eth1)    
    except: 
     pass
    #try to enable_eth2
    try:
     os.popen(enable_eth2)    
    except: 
     pass
    #try to enable_eth3
    try:
     os.popen(enable_eth3)    
    except: 
     pass
    

#The afk script
def afk_timer_script():
    #Turn on internet in case if programm was closed by mistake or smh
    enable_internet_all()
    disable_internet_all()
    print ("internet has been killed")
    threading.Timer(600, enable_internet_all).start()
    print('internet has been invoked')
    
#The main programm



#enable internet before exiting programm
def exit_button():
    global running
    running = False
    enable_internet_all()
    f = open('log.txt', 'a+')
    f.write(time.ctime() + '')
    f.close
    time.sleep(1)
    root.destroy()
 
#main script that activates by button    
def main():
    running = True
    if running:
    #log when you`ve started working
     f = open('log.txt', 'a+')
     f.write(time.ctime() + 'Starting time')
     f.close
     threading.Timer(3600, afk_timer_script).start()
     root.after(4202000, main)
    

#Create a start button and place it
Start_Timer_button = Button(root, text = "Start AFK Timer", height= 4, width = 30, fg='#993af0', bg='#262626', font=('Helvetica',14,'bold'), 
                            command = main)
Start_Timer_button.pack(side = 'top')

#Button that enables internet before exiting
Exit_Timer_button = Button(root, text = "Exit AFK Timer", height= 4,width = 30, fg='#993af0', bg='#262626', font=('Helvetica',14,'bold'), 
                            command = exit_button)
Exit_Timer_button.pack(side = 'bottom')

root.mainloop()

