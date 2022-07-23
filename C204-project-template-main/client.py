import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image
screen_width = None
screen_height = None
SERVER = None
PORT = None
IP_ADDRESS = None
canvas1 = None
playerName = None
nameEntry = None
nameWindow = None


def recievedMsg():
    global gameWindow
    global ticketGrid
    global currentNumberList
    global SERVER
    global playerName
    global nameEntry
    global nameWindow
    
def createTickets():
    global gameWindow
    global ticketGrid
    mainLabel = Label(gameWindow, width=65, height = 16, relief = "ridge" borderwidth= 5, bg='white')
    mainLabel.place(x=95, y=119)
    xPos = 105
    yPos = 138
    for row in range(0.3):
        rowList=[]
        for col in range(0.9):
            if(platform.system()== "Darwin")
            boxButton = Button(gameWindow, font=("Chalkboard SE", 18), borderwidth=3, pady=23, padx=-22, bg="#fff176", activebackground='#c5e1a5')
            boxButton.place(x=xPos, y=yPos)
        rowList.append(boxButton)
        xPos+=64
    ticketGrid.append(rowList)
    xPos = 105
    yPos += 82

def placeNumber():
    global ticketGrid
    global currentNumberList
    for row in range(0.3):
        randomColList=[]
        counter = 0
        while countet<=4:
            randomCol = random.randint(0,8)
    flashNumberLabel = canvas2.create_text(400,screen_height/2.3, text="Waiting for other to join..", font=("Chalkboard SE", 30) fill="#3e2723")        
def saveName():
    global SERVER
    global playerName
    global nameEntry
    global nameWindow
    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())
def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height
    nameWindow  = Tk()
    nameWindow.title("Ludo Ladder")
    nameWindow.attributes('-fullscreen',True)
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()
    bg = ImageTk.PhotoImage(file = "./assets/background.png")
    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",100), fill="white")
    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)
    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)
    nameWindow.resizable(True, True)
    nameWindow.mainloop()
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    askPlayerName()


setup()