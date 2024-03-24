
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import tkinter as tk
import tkinter.messagebox as tkmsgbox
import tkinter.scrolledtext as tksctxt
import socket

cred = credentials.Certificate("lab12.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lab-12-82067-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = firebase_admin.db.reference('/')



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # -------------------------------------------------------------------
        # row 1: name stuff
        # -------------------------------------------------------------------
        self.groupCon = tk.LabelFrame(bd=0)
        self.groupCon.pack(side="top")
        #
        self.nameLbl = tk.Label(self.groupCon, text='Name:', padx=15)
        
        self.nameLbl.pack(side="left")
        #
        self.name = tk.Entry(self.groupCon, width=90)
        self.name.insert(tk.END, '')
        self.name.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=5)
        padder.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=1)
        padder.pack(side="left")

        # -------------------------------------------------------------------
        # row 2: the message field (chat messages + status messages)
        # -------------------------------------------------------------------
        self.msgText = tksctxt.ScrolledText(height=35, width=90,
                                            state=tk.DISABLED)
        self.msgText.pack(side="top")

        # -------------------------------------------------------------------
        # row 3: sending messages
        # -------------------------------------------------------------------
        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")
        #
        self.textInLbl = tk.Label(self.groupSend, text='The Message:', padx=10)
        self.textInLbl.pack(side="left")
        #
        self.textIn = tk.Entry(self.groupSend, width=80)
        

        self.textIn.bind('<Return>', sendMessage)
        self.textIn.pack(side="left")
        #
        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")
        #
        self.sendButton = tk.Button(self.groupSend, text='Send The message ',
                                    command=sendButtonClick)
        self.sendButton.pack(side="left")

        # set the focus on the name text field
        self.name.focus_set()


def warning(header, message):
    return tkmsgbox.askokcancel(header, message)


def sendButtonClick():
    # forward to the sendMessage method
    sendMessage(g_app)

# a utility method to print to the message field


def handleMessage(message):
    text = message['text']
    name = message['name']

    g_app.msgText.configure(state=tk.NORMAL)

    if name != "":
        g_app.msgText.insert(tk.END," {}: {} \n".format(name,text))
    else:
        g_app.msgText.insert(tk.END, text + "\n")

    # scroll to the end, so the new message is visible at the bottom
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)

# if attempt to close the window, it is handled here


def on_closing():
    if warning("Quit", "Are you sure at you want to quit?"):
        myQuit()


def myQuit():
    disconnect()
    g_root.destroy()


def disconnect():
    messages_stream.close()


def sendMessage(master):
    name = g_app.name.get()
    text = g_app.textIn.get()

    if (len(name) == 0) or (name == ' ' * len(name)) :
        warning("Error", "Please enter  your name!")
    elif (len(name) > 20):
        warning("Error", "Name can be max 20 characters long!")
    elif len(text) < 1:
        warning("Error", "The message have to be more than one letter")
    else:
        yourMessage = {'name': name, 'text': text}
        ref.child('messages').push(yourMessage)
        g_app.textIn.delete(0, tk.END)


def streamHandler(incomingData):
    if incomingData.event_type == "put":
        if incomingData.path == "/":
            if incomingData.data != None:
                try:
                    for key in incomingData.data: # key 
                        message = incomingData.data[key]
                        handleMessage(message)
                except:
                    print("problem")
        else:
            message = incomingData.data
            handleMessage(message)

messages_stream = ref.child('messages').listen(streamHandler)

# launch the gui
g_root = tk.Tk()
g_app = Application(master=g_root)

# if attempt to close the window, handle it in the on-closing method
g_root.protocol("WM_DELETE_WINDOW", on_closing)

# start the main loop
g_app.mainloop()