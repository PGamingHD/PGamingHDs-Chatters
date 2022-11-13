from network import send, connect, close;
from datetime import datetime;
import tkinter;

def message_handler(time, player, networkMsg):
    currentDateAndTime = datetime.now().strftime("%H:%M:%S");

top = tkinter.Tk();
top.title("PGamingHDs Chatters");

messages_frame = tkinter.Frame(top);
my_msg = tkinter.StringVar();
my_msg.set("Enter Message");
scrollbar = tkinter.Scrollbar(messages_frame);