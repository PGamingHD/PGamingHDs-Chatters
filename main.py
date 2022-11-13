#PGamingHDs EPIC CHATTER APP!
from network import send, connect, close;
from datetime import datetime;
import tkinter;

def message_handler(time, player, networkMsg):
    currentDateAndTime = datetime.now().strftime("%H:%M:%S");
    if 'system' in player:
        msg_list.insert(tkinter.END, "[" + currentDateAndTime + "] [" + player.upper() + "]: " + networkMsg);
        return;
    msg_list.insert(tkinter.END, "[" + currentDateAndTime + "] (" + player + "): " + networkMsg);



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

entry_field = tkinter.Entry(top, textvariable=my_msg);
entry_field.bind("<Return>", send_to_user);
entry_field.pack();
send_button = tkinter.Button(top, text="Send", command=send_to_user);
send_button.pack();

top.protocol("WM_DELETE_WINDOW", on_closing);

CHANNEL = input('Enter Channel: ');
USERNAME = input('Enter Username: ');

connect(CHANNEL, USERNAME, message_handler);

tkinter.mainloop();