from network import send, connect, close;
from datetime import datetime;
import tkinter;

def message_handler(time, player, networkMsg):
    currentDateAndTime = datetime.now().strftime("%H:%M:%S");



def send_to_user(): #Sending function to send msg!
    msg = my_msg.get();
    my_msg.set("");

    if msg == "":
        return;

    send(msg);
    if msg == "/quit":
        close();
        top.quit();

def on_closing():
    close();
    top.quit();

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

top.protocol("WM_DELETE_WINDOW", on_closing)
