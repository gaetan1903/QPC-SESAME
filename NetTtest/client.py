from tkinter import *
import socket

host = socket.gethostname()
port = 8000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

class Application(Frame):
    def __init__(self, master=None):
        #Create master frame
        Frame.__init__(self,master)
        self.grid()
        self.master.title("Test 1")
        self.conn=False #State of connection to server


        #Configure main frame
        for r in range (4):
            self.master.rowconfigure(r, weight=1)
        for c in range (2):
            self.master.columnconfigure(c)

        #Create sub frames
        TopFrame=Frame(master, bg="red")
        TopFrame.grid(row=0, column=0, rowspan=3)
        BottomFrame=Frame(master, bg="blue")
        BottomFrame.grid(row=4, column=0)
        SideFrame=Frame(master, bg="green")
        SideFrame.grid(column=1, row=0, rowspan=4)

        #Create Chat log
        self.chatlog=Text(TopFrame)
        self.chatlog.pack(padx=5, pady=5)


    #Create entry field
        self.e1=StringVar()
        self.e1=Entry(BottomFrame)
        self.e1.pack(pady=5, padx=5)

        #Create buttons
        b1=Button(SideFrame, text="Connect", command=self.connect)
        b1.grid(row=0, column=0, padx=5, pady=5)
        b2=Button(SideFrame, text="Disconnect", command=self.disconnect)
        b2.grid(row=1, column=0, padx=5, pady=5)
        b3=Button(SideFrame, text="Send", command=self.sendmessage)
        b3.grid(row=2, column=0, padx=5, pady=5)

    def connect(self): #Connect to server
        self.chatlog['state'] = NORMAL
        self.chatlog.insert(END, ("===ATTEMPTING TO CONNECT TO SERVER\n"))
        self.chatlog['state'] = DISABLED
        self.chatlog.yview(END)
        try:
            s.connect((host,port))
            self.chatlog['state'] = NORMAL
            self.chatlog.insert(END, ("===CONNECTED TO SERVER\n"))

            self.chatlog['state'] = DISABLED
            self.chatlog.yview(END)
            self.conn=True
            print("Connected") #Connection successful

            #Receive messages
            self.receive_msg()

        except ConnectionRefusedError: #Can't find server
            self.chatlog['state'] = NORMAL
            self.chatlog.insert(END, ("===SERVER COULD NOT BE FOUND\n" + "===PLEASE MAKE SURE THE SERVER IS ON, AND YOU'RE CONNECTED TO THE NETWORK\n"))
            self.chatlog['state'] = DISABLED
            self.chatlog.yview(END)
        except: #Other errors
            self.chatlog['state'] = NORMAL
            self.chatlog.insert(END, ("===THERE'S AN ERROR WITH THE PROGRAM\n" + "===PLEASE TURN IT OFF AND ON AGAIN\n"))
            self.chatlog['state'] = DISABLED
            self.chatlog.yview(END)

        # When attempting to connect a second time, produces OS error: an operation was attempted on something that is not a socket

    def disconnect(self):
        if self.conn: #Tests to see if client is connected
            s.close()
            self.chatlog['state'] = NORMAL
            self.chatlog.insert(END, ("===DISCONNECTED FROM SERVER.\n"))
            self.chatlog['state'] = DISABLED
            self.chatlog.yview(END)
            self.conn=False
        else: #Prevents attempting to disconnect when already disconnected
            self.chatlog['state'] = NORMAL
            self.chatlog.insert(END, ("===YOU AREN'T CURRENTLY CONNECTED.\n"))
            self.chatlog['state'] = DISABLED
            self.chatlog.yview(END)


    def sendmessage(self):
        if self.conn: #Prevents sending if not connected
            self.msg=self.e1.get()
            if self.msg == "": #Empty message catcher
                self.chatlog['state'] = NORMAL
                self.chatlog.insert(END, ("===YOU CANNOT SEND AN EMPTY MESSAGE.\n" ))
                self.chatlog['state'] = DISABLED
                self.chatlog.yview(END)
            else:
                self.chatlog['state'] = NORMAL
                self.chatlog.insert(END, ('You: ' + self.msg + '\n'))
                self.chatlog['state'] = DISABLED
                self.chatlog.yview(END)
                self.send_data(self.msg) #Sends message
        else:
                self.chatlog['state'] = NORMAL
                self.chatlog.insert(END, ("===YOU ARE NOT CONNECTED TO A SERVER. YOU CANNOT SEND A MESSAGE.\n" ))
                self.chatlog['state'] = DISABLED
                self.chatlog.yview(END)

    def receive_msg(self):
        #Prepared to receive message
        print("Preparing to receive")
        while 1:
            data=s.recv(1024)
            decoded_data=data.decode('UTF-8')
            print(decoded_data) #Only printing to cmd line for now, to resolve errors
            #self.mainloop() ##Only fix I've found. This loop seems to crash the mainloop used to update GUI

    def send_data(self, message):
        try:
            s.send(message.encode('UTF-8'))
        except:
                self.chatlog['state'] = NORMAL
                self.chatlog.insert(END, ("===THE PREVIOUS MESSAGE DIDN'T SEND. THIS IS POSSIBLY DUE TO A SERVER ERROR.\n"))
                self.chatlog['state'] = DISABLED
                self.chatlog.yview(END)


root = Tk()
app = Application(root)
app.mainloop()