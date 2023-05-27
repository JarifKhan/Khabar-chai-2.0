import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#from app.py
from PyQt5.QtGui import QFont
from datetime import datetime
import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton


widgets = {
    "logo": [],
    "button": [],
    "time": [],
    "label": [],
    "rb1":[],
    "rb2":[],
    "rb3":[],
    "rb4":[],
    "breakfast":[],
    "ms":[],
    "lunch":[],
    "as":[],
    "dinner":[],
    "time1": [],
    "time2": [],
    "time3": [],
    "time4": [],
    "time5": [],

}


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("khabar chai")
#window.setFixedWidth(1000)
#window.setFixedHeight(1000)
window.move(550, 200) #window's position on the screen
window.setStyleSheet("background: #161219;") #Window Background Color

#initialliza grid layout
grid = QGridLayout()

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def start_game():
    '''display frame 2'''
    clear_widgets()
    frame1()

def start_game1():
    '''display frame 3'''
    clear_widgets()
    frame2()

#time shower
#def breakfastTime():
btime = "07:30:00"
btime = btime.split(":")
bh = int(btime[0])
bm = int(btime[1])
bs = int(btime[2])
breakfast_Time=[bh,bm,bs]
breakfast_end_Time=[8,30,60]

lunch_Time=[2,00,00]
lunch_end_Time=[3,30,00]

esnakes_Time=[15,30,00]
esnakes_end_Time=[16,30,00]

dinner_Time = [20,30,00]
dinner_end_Time = [21,30,00]

m_snacks_Time=[10,20,60]
m_snacks_end_Time=[10,59,00]


    

#logo
def mainf():
    image = QPixmap("khabar_chai_logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 0px;")

    widgets["logo"].append(logo)
    #button widget
    button = QPushButton("Still Hungry")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        
            "*{border: 4px solid '#BC006C';"+
            "border-radius: 45px;"+
            "font-size: 35px;"+
            "color: 'white';"+
            "padding: 25px ;"+
            "margin: 100px 200px;}"+
            "*:hover{background: '#BC006C';}"
        
        
    )
    #button callback
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-1], 3, 0)

    name = "Breakfast"
    #time section
    breakfast_lable = QLabel(name)
    breakfast_lable.setAlignment(QtCore.Qt.AlignCenter)
    breakfast_lable.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 25px;"+
        "color: 'white';"+
        "margin-top: 75px;"
    )

    
    

    
    
    widgets["label"].append(breakfast_lable)
    grid.addWidget(widgets["label"][-1],1,0)

        



    


#main frame function
def breakfastTime():
    lst= breakfast_Time
    lst2= breakfast_end_Time
    now = datetime.now()
    displayTxt=now.strftime('%H:%M:%S')
    #breakfast time set
    start = '7:30:00'
    end='8:30:00'
    current=displayTxt
    FMT = '%H:%M:%S'

    hour=int(displayTxt[:2])
    minute=int(displayTxt[3:5])
    second=int(displayTxt[6:])

    #finish condition
    if (hour==lst2[0] and minute>lst2[0]) or (hour>lst2[0]):
        b_lbl.setText('Ended!')
    #time left condition
    elif hour>lst[0] or (hour==lst[0] and minute>=lst[1]):
        txt = str(datetime.strptime(end, FMT) - datetime.strptime(current, FMT))
        b_lbl.setText(f'Meal ends in:\n{txt}')
    #counting time condition
    else:
        txt = str(datetime.strptime(start, FMT) - datetime.strptime(current, FMT))
        b_lbl.setText(txt)





#hiding method



b_timer = QTimer()
b_timer.timeout.connect(breakfastTime) 
b_timer.start(1000)

b_lbl = QLabel()

b_lbl.setAlignment(QtCore.Qt.AlignCenter)
b_lbl.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "margin-right: 15px;"
)
widgets["time"].append(b_lbl) 
grid.addWidget(widgets["time"][-1],2,0)


#------------------ breakfast ---------------------
def breakfastTime1():
    lst= breakfast_Time
    lst2= breakfast_end_Time
    now = datetime.now()
    displayTxt=now.strftime('%H:%M:%S')
    #breakfast time set
    start = '7:30:00'
    end='8:30:00'
    current=displayTxt
    FMT = '%H:%M:%S'

    hour=int(displayTxt[:2])
    minute=int(displayTxt[3:5])
    second=int(displayTxt[6:])

    #finish condition
    if (hour==lst2[0] and minute>lst2[0]) or (hour>lst2[0]):
        b1_lbl.setText('Ended!')
    #time left condition
    elif hour>lst[0] or (hour==lst[0] and minute>=lst[1]):
        txt = str(datetime.strptime(end, FMT) - datetime.strptime(current, FMT))
        b1_lbl.setText(f'Meal ends in:\n{txt}')
    #counting time condition
    else:
        txt = str(datetime.strptime(start, FMT) - datetime.strptime(current, FMT))
        b1_lbl.setText(txt)


b1_timer = QTimer()
b1_timer.timeout.connect(breakfastTime1) 
b1_timer.start(1000)

b1_lbl = QLabel()

b1_lbl.setAlignment(QtCore.Qt.AlignCenter)
b1_lbl.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "margin-right: 15px;"
)

#------------------ breakfast ---------------------

#------------------ msnacks ---------------------

def msnacks():
    lst= m_snacks_Time
    lst2= m_snacks_end_Time
    now = datetime.now()
    displayTxt=now.strftime('%H:%M:%S')
    #lunch time set
    start = '10:20:00'
    end='11:00:00'
    current=displayTxt
    FMT = '%H:%M:%S'

    hour=int(displayTxt[:2])
    minute=int(displayTxt[3:5])
    second=int(displayTxt[6:])

    #finish condition
    if (hour==lst2[0] and minute>lst2[0]) or (hour>lst2[0]):
        ms_lbl.setText('Ended!')
    #time left condition
    elif hour>lst[0] or (hour==lst[0] and minute>=lst[1]):
        txt = str(datetime.strptime(end, FMT) - datetime.strptime(current, FMT))
        ms_lbl.setText(f'Meal ends in:\n{txt}')
    #counting time condition
    else:
        txt = str(datetime.strptime(start, FMT) - datetime.strptime(current, FMT))
        ms_lbl.setText(txt)


ms_timer = QTimer()
ms_timer.timeout.connect(msnacks) 
ms_timer.start(1000)

ms_lbl = QLabel()

ms_lbl.setAlignment(QtCore.Qt.AlignCenter)
ms_lbl.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "margin-right: 15px;"
)

#------------------ msnacks ---------------------

#------------------ lunch ---------------------

def Lunch():
    lst= lunch_Time
    lst2= lunch_end_Time
    now = datetime.now()
    displayTxt=now.strftime('%H:%M:%S')
    #lunch time set
    start = '12:00:00'
    end='14:30:00'
    current=displayTxt
    FMT = '%H:%M:%S'

    hour=int(displayTxt[:2])
    minute=int(displayTxt[3:5])
    second=int(displayTxt[6:])

    #finish condition
    if (hour==lst2[0] and minute>lst2[0]) or (hour>lst2[0]):
        l_lbl.setText('Ended!')
    #time left condition
    elif hour>lst[0] or (hour==lst[0] and minute>=lst[1]):
        txt = str(datetime.strptime(end, FMT) - datetime.strptime(current, FMT))
        l_lbl.setText(f'Meal ends in:\n{txt}')
    #counting time condition
    else:
        txt = str(datetime.strptime(start, FMT) - datetime.strptime(current, FMT))
        l_lbl.setText(txt)


l_timer = QTimer()
l_timer.timeout.connect(Lunch) 
l_timer.start(1000)

l_lbl = QLabel()

l_lbl.setAlignment(QtCore.Qt.AlignCenter)
l_lbl.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "margin-right: 15px;"
)

#------------------ lunch ---------------------

#------------------ evening snacks ---------------------

def esnakes():
    lst= esnakes_Time
    lst2= esnakes_Time
    now = datetime.now()
    displayTxt=now.strftime('%H:%M:%S')
    #lunch time set
    start = '15:30:00'
    end='16:30:00'
    current=displayTxt
    FMT = '%H:%M:%S'

    hour=int(displayTxt[:2])
    minute=int(displayTxt[3:5])
    second=int(displayTxt[6:])

    #finish condition
    if (hour==lst2[0] and minute>lst2[0]) or (hour>lst2[0]):
        es_lbl.setText('Ended!')
    #time left condition
    elif hour>lst[0] or (hour==lst[0] and minute>=lst[1]):
        txt = str(datetime.strptime(end, FMT) - datetime.strptime(current, FMT))
        es_lbl.setText(f'Meal ends in:\n{txt}')
    #counting time condition
    else:
        txt = str(datetime.strptime(start, FMT) - datetime.strptime(current, FMT))
        es_lbl.setText(txt)


es_timer = QTimer()
es_timer.timeout.connect(esnakes) 
es_timer.start(1000)

es_lbl = QLabel()

es_lbl.setAlignment(QtCore.Qt.AlignCenter)
es_lbl.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "margin-right: 15px;"
)

#------------------ evening snacks ---------------------

#------------------ dinner ---------------------

def dinner():
    lst= dinner_Time
    lst2= dinner_end_Time
    now = datetime.now()
    displayTxt=now.strftime('%H:%M:%S')
    #lunch time set
    start = '20:30:00'
    end='21:30:00'
    current=displayTxt
    FMT = '%H:%M:%S'

    hour=int(displayTxt[:2])
    minute=int(displayTxt[3:5])
    second=int(displayTxt[6:])

    #finish condition
    if (hour==lst2[0] and minute>lst2[0]) or (hour>lst2[0]):
        d_lbl.setText('Ended!')
    #time left condition
    elif hour>lst[0] or (hour==lst[0] and minute>=lst[1]):
        txt = str(datetime.strptime(end, FMT) - datetime.strptime(current, FMT))
        d_lbl.setText(f'Meal ends in:\n{txt}')
    #counting time condition
    else:
        txt = str(datetime.strptime(start, FMT) - datetime.strptime(current, FMT))
        d_lbl.setText(txt)


d_timer = QTimer()
d_timer.timeout.connect(dinner) 
d_timer.start(1000)

d_lbl = QLabel()

d_lbl.setAlignment(QtCore.Qt.AlignCenter)
d_lbl.setStyleSheet(
    "font-family: Shanti;"+
    "font-size: 25px;"+
    "color: 'white';"+
    "margin-right: 15px;"
)

#------------------ dinner ---------------------

def btnstate(b):
        if b.text() == "Green":
            if b.isChecked() == True:
                window.setStyleSheet("background-color: green;")
				
        if b.text() == "Red":
            if b.isChecked() == True:
                window.setStyleSheet("background-color: red;")
        if b.text() == "Grey":
            if b.isChecked() == True:
                window.setStyleSheet("background-color: grey;")
        if b.text() == "reset":
            if b.isChecked() == True:
                window.setStyleSheet("background-color: #161219;")

#frame 1

ftemp = 3
def frame1():

    #------------------ breakfast ---------------------
    breakfast1_lable = QLabel("Breakfast: ")
    breakfast1_lable.setAlignment(QtCore.Qt.AlignCenter)
    breakfast1_lable.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 25px;"+
        "color: 'white';"+
        "margin-top: 20px;"
    )
    
    widgets["breakfast"].append(breakfast1_lable)
    grid.addWidget(widgets["breakfast"][-1],0,ftemp)

    widgets["time1"].append(b1_lbl) 
    grid.addWidget(widgets["time1"][-1],1,ftemp)
    #------------------ breakfast ---------------------

    #------------------ msnakes ---------------------
    msnakes_lable = QLabel("Morning snacks: ")
    msnakes_lable.setAlignment(QtCore.Qt.AlignCenter)
    msnakes_lable.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 25px;"+
        "color: 'white';"+
        "margin-top: 20px;"
    )

    widgets["ms"].append(msnakes_lable)
    grid.addWidget(widgets["ms"][-1],2,ftemp)

    widgets["time2"].append(ms_lbl) 
    grid.addWidget(widgets["time2"][-1],3,ftemp)
    #------------------ msnakes ---------------------

    #------------------ lunch ---------------------
    lunch_lable = QLabel("Lunch: ")
    lunch_lable.setAlignment(QtCore.Qt.AlignCenter)
    lunch_lable.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 25px;"+
        "color: 'white';"+
        "margin-top: 20px;"
    )

    widgets["lunch"].append(lunch_lable)
    grid.addWidget(widgets["lunch"][-1],4,ftemp)

    widgets["time3"].append(l_lbl) 
    grid.addWidget(widgets["time3"][-1],5,ftemp)
    #------------------ lunch ---------------------

    #------------------ evening snakes ---------------------
    es_lable = QLabel("Evening snakes: ")
    es_lable.setAlignment(QtCore.Qt.AlignCenter)
    es_lable.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 25px;"+
        "color: 'white';"+
        "margin-top: 20px;"
    )

    widgets["as"].append(es_lable)
    grid.addWidget(widgets["as"][-1],6,ftemp)

    widgets["time4"].append(es_lbl) 
    grid.addWidget(widgets["time4"][-1],7,ftemp)
    #------------------ evening snakes ---------------------

    #------------------ dinner ---------------------
    d_lable = QLabel("Dinner: ")
    d_lable.setAlignment(QtCore.Qt.AlignCenter)
    d_lable.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 25px;"+
        "color: 'white';"+
        "margin-top: 20px;"
    )

    widgets["dinner"].append(d_lable)
    grid.addWidget(widgets["dinner"][-1],8,ftemp)

    widgets["time5"].append(d_lbl) 
    grid.addWidget(widgets["time5"][-1],9,ftemp)
    #------------------ dinner ---------------------

    #------------------ Bottom logo ---------------------

    image1 = QPixmap("khabar_chai_bottom_logo.png")
    logo1 = QLabel()
    logo1.setPixmap(image1)
    logo1.setAlignment(QtCore.Qt.AlignCenter)
    logo1.setStyleSheet("margin-bottom: 0px;")
    

    widgets["logo"].append(logo1)
    grid.addWidget(widgets["logo"][-1],11,ftemp)

    #radio buttorn
    
    b1 = QRadioButton("Green")
    b1.setStyleSheet("color: 'white';"+
                     "margin-right: 0px;"+
                     "padding: 0px;"
                     )
    b1.toggled.connect(lambda:btnstate(b1))
    widgets["rb1"].append(b1)
    grid.addWidget(widgets["rb1"][-1],10,1)
        
    b2 = QRadioButton("Red")
    b2.setStyleSheet("color: 'white';")
    b2.toggled.connect(lambda:btnstate(b2))
    widgets["rb2"].append(b2)
    grid.addWidget(widgets["rb2"][-1],10,2)

    b3 = QRadioButton("Grey")
    b3.setStyleSheet("color: 'white';")
    b3.toggled.connect(lambda:btnstate(b3))
    widgets["rb3"].append(b3)
    grid.addWidget(widgets["rb3"][-1],10,4)

    b4 = QRadioButton("reset")
    b4.setStyleSheet("color: 'white';")
    b4.toggled.connect(lambda:btnstate(b4))
    widgets["rb4"].append(b4)
    grid.addWidget(widgets["rb4"][-1],10,5)

    #radio buttorn

    #time input button
    button1 = QPushButton("Time input")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button1.setStyleSheet(
        
            "*{border: 2px solid '#BC006C';"+
            "border-radius: 18px;"+
            "font-size: 12px;"+
            "color: 'white';"+
            "padding: 12px ;"+
            "margin-top: 20px;}"+
            "*:hover{background: '#BC006C';}"
        
        
    )
    
    #button callback
    button1.clicked.connect(start_game1)

    widgets["button"].append(button1)
    grid.addWidget(widgets["button"][-1], 0, 1)

    #time input button


#frame 1

#frame 2

def buttonWork():
    window1 = QWidget()
    #window.setFixedWidth(1000)
    #window.setFixedHeight(1000)
    window1.move(550, 200) #window's position on the screen
    window1.setStyleSheet("background: #161219;"+"color: white;")
    text, ok = QInputDialog.getText(window1,"Enter Your Time", "Format= hh:mm:ss")

    if ok:
        btime = text
        in_label = QLabel(str(btime))
        in_label.setAlignment(QtCore.Qt.AlignCenter)
        in_label.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 12px;"+
        "color: 'white';"+
        "margin-top: 20px;"
    )

    
    

    
    
    widgets["label"].append(in_label)
    grid.addWidget(widgets["label"][-1],0,1)


def frame2():
    button2 = QPushButton("Breakfast")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2.setStyleSheet(
        
            "*{border: 2px solid '#BC006C';"+
            "border-radius: 18px;"+
            "font-size: 12px;"+
            "color: 'white';"+
            "padding: 12px ;"+
            "margin-top: 20px;}"+
            "*:hover{background: '#BC006C';}"
         
    )
    widgets["button"].append(button2)
    grid.addWidget(widgets["button"][-1], 0, 0)

    button2.clicked.connect(buttonWork)
    


#frame 2










mainf()






window.setLayout(grid)

window.show()
sys.exit(app.exec())