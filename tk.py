from tkinter import*
#install_startup.sh
#sudo bash
#/home/pi/di_update/Raspbian_For_Robots/upd_script/wifi/cinch_setup.sh
#sudo python3 flask_server.py
#pip install numpy
#pip install opencv-python
# camera is there but commented out
#Main for GUI
#
rob = Tk()                            #Make window
rob.wm_title('Robot Radar on Kitt')   #name
rob.config(background="#E3D7BD")      #background

#Definitions of Functions-----------------------------------------------------------------------------------------------
#Servo methods


def servol():
    outputLog.insert(0.0, "Servo turns left\n")


def servos():
    outputLog.insert(0.0, "Servo turns straight\n")


def servor():
    outputLog.insert(0.0, "Servo turns right\n")

#Speed methods


def speed1():
    outputLog.insert(0.0, "Speed set to 1\n")


def speed2():
    outputLog.insert(0.0, "Speed set to 2\n")


def speed3():
    outputLog.insert(0.0, "Speed set to 3\n")

#Shape Constructor


def redCircle():
    circleCanvas.create_oval(30, 30, 80, 80, width=0, fill='red')
    outputLog.insert(0.0, "Too close\n")


def yelCircle():
    circleCanvas.create_oval(30, 30, 80, 80, width=0, fill='yellow')
    outputLog.insert(0.0, "In proximity of Object\n")


def grnCircle():
    circleCanvas.create_oval(30, 30, 80, 80, width=0, fill='green')
    outputLog.insert(0.0, "Safe\n")

#Tope Left Frame-----------------------------------------------------------------------


tleftFrame = Frame(rob, width=200, height=300)
tleftFrame.grid(row=0, column=0, padx=20, pady=4)

Label(tleftFrame, text="Servo Angle").grid(row=0, column=0, padx=10, pady=2)

btnFrame1 = Frame(tleftFrame, width=300, height=600)
btnFrame1.grid(row=1, column=0, padx=10, pady=2)

se1Btn = Button(btnFrame1, text="Left", command=servol)
se1Btn.grid(row=1, column=0, padx=10, pady=2)

se2Btn = Button(btnFrame1, text="Straight", command=servos)
se2Btn.grid(row=1, column=1, padx=10, pady=2)

se3Btn = Button(btnFrame1, text="Right", command=servor)
se3Btn.grid(row=1, column=2, padx=10, pady=2)

#Middle Left Frame(Speed)-----------------------------------------------------------------------------------------------
#mleftFrame = Frame(rob, width=300, height = 300)
#mleftFrame.grid(row=1, column=0, padx=100, pady=20)

Label(tleftFrame, text="Speed").grid(row=2, column=0, padx=10, pady=2)

#btnFrame2 = Frame(mleftFrame, width=200, height = 200)
#btnFrame2.grid(row=2, column=0, padx=10, pady=2)

s1Btn = Button(btnFrame1, text="Speed 1", command=speed1)
s1Btn.grid(row=5, column=0, padx=10, pady=2)

s2Btn = Button(btnFrame1, text="Speed 2", command=speed2)
s2Btn.grid(row=5, column=1, padx=10, pady=2)
#Instruct.grid(row=0, column=0, padx=10, pady=2)

s3Btn = Button(btnFrame1, text="Speed 3", command=speed3)
s3Btn.grid(row=5, column=2, padx=10, pady=2)
#try:
#imageEx = PhotoImage(file = 'image.gif')
#Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
#except:
#print("Image not found")

#Top Middle(Obstruct Constructor/Mapping)-------------------------------------------------------------------------------
midFrame = Frame(rob, width=300, height=600)
midFrame.grid(row=0, column=1, padx=10, pady=2)

Label(midFrame, text="Map").grid(row=0, column=1, padx=10, pady=2)

circleCanvas = Canvas(midFrame, width=400, height=400, bg='black')
circleCanvas.grid(row=1, column=1, padx=10, pady=20)

btnFrame2 = Frame(midFrame, width=100, height=100)
btnFrame2.grid(row=2, column=1, padx=10, pady=2)

redBtn = Button(btnFrame2, text="Red", command=redCircle)
redBtn.grid(row=2, column=0, padx=10, pady=2)

yelBtn = Button(btnFrame2, text="Yellow", command=yelCircle)
yelBtn.grid(row=2, column=1, padx=10, pady=2)

grnBtn = Button(btnFrame2, text="Green", command=grnCircle)
grnBtn.grid(row=2, column=2, padx=10, pady=2)

#Top Right Frame (Camera)-----------------------------------------------------------------------------------------------
trFrame = Frame(rob, width=300, height=600)
trFrame.grid(row=0, column=2, padx=10, pady=2)

Instruct = Label(trFrame, text="Camera")
#Instruct.grid(row=0, column=0, padx=10, pady=2)
#inputLog = Text(trFrame, width=30, height=10, takefocus=0)
#inputLog.grid(row=1, column=0, padx=10, pady=2)


#Label(trFrame, text="Camera:").grid(row=0, column=1, padx=10, pady=2)

#Middle Right Frame (Compass)-------------------------------------------------------------------------------------------
#mrFrame = Frame(rob, width=100, height = 200)
#mrFrame.grid(row=1, column=2, padx=10, pady=2)

Instruct = Label(trFrame, text='Compass: ')
Instruct.grid(row=2, column=0, padx=10, pady=2)
inputLog = Text(trFrame, width=30, height=10, takefocus=0)
inputLog.grid(row=3, column=0, padx=10, pady=2)

#Bottom Left Frame (User Input)-----------------------------------------------------------------------------------------
blFrame = Frame(rob, width=300, height=600)
blFrame.grid(row=1, column=0, padx=10, pady=2)
#value = input("Type a command...")
#userinp=simpledialog.askstring('Input', prompt='Type a command: ')
Instruct = Label(blFrame, text="Input")
Instruct.grid(row=0, column=0, padx=10, pady=2)
Label(blFrame, text="Type a command...").grid(row=1, column=0, padx=10, pady=2)

inputLog = Text(blFrame, width=30, height=10, takefocus=0)
inputLog.grid(row=2, column=0, padx=10, pady=2)
#a = input()

#Bottom Middle Frame (OUTPUT)-------------------------------------------------------------------------------------------
bmFrame = Frame(rob, width=300, height=300)
bmFrame.grid(row=1, column=1, padx=10, pady=2)

Instruct = Label(bmFrame, text="Output")
Instruct.grid(row=0, column=0, padx=10, pady=2)
Label(bmFrame, text="Output and System Messages").grid(row=1, column=0, padx=10, pady=2)
outputLog = Text(bmFrame, width=30, height=10, takefocus=0)
outputLog.grid(row=2, column=0, padx=10, pady=2)
#print(a)
#Bottom right Frame(Returned Values)------------------------------------------------------------------------------------

brFrame = Frame(rob, width=300, height=600)
brFrame.grid(row=1, column=2, padx=10, pady=2)
#value = input("Type a command...")
Label(brFrame, text="Returned Values: ").grid(row=0, column=1, padx=10, pady=2)

intA = 1
intB = 2
intC = 3
ints = intA, intB, intC

Instruct = Label(brFrame, text="Speed: ")
Instruct.grid(row=1, column=0, padx=10, pady=2)
Instruct = Label(brFrame, text="Servo Angle: ")
Instruct.grid(row=2, column=0, padx=10, pady=2)
Instruct = Label(brFrame, text="Distance: ")
Instruct.grid(row=1, column=2, padx=10, pady=2)
Instruct = Label(brFrame, text="Battery: ")
Instruct.grid(row=2, column=2, padx=10, pady=2)

#update GUI
rob.mainloop()
