from network import send, connect, close;
from datetime import datetime;
import tkinter;

def message_handler(time, player, networkMsg):
    currentDateAndTime = datetime.now().strftime("%H:%M:%S");

top = tkinter.Tk();
top.title("PGamingHDs Chatters");