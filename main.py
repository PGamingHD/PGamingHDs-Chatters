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

msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set);
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y);
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH);
msg_list.pack();
messages_frame.pack();