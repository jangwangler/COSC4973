from Tkinter import *
#from test.reperf import timefunc
#from PIL import ImageTk, Image
import Tkinter as tk
#from distutils import command
#from _bisect import bisect_left
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import subprocess
import matplotlib
from matplotlib.pyplot import ylim
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



#initializing  Scores 

scoreH = 0
passH = 0
shotsH = 0
scoreA = 0
passA = 0
shotsA = 0
started = False
T_left = 90
dispdata = [.5]
timeplot = [0]
timeplot1=0
fig, ax = plt.subplots()
line, = ax.plot(dispdata)


root = Tk()

#Clock Functions
def cClick():
    global T_left
    global timeClock
    T_left+= 1
    timeClock['text'] = "%(T_left)d"% {"T_left": T_left}
    
def c1Click():
    global T_left
    global timeClock
    T_left-= 1
    timeClock['text'] = "%(T_left)d"% {"T_left": T_left}

def countdown():
    #change text in label
    global T_left
    global started
    global timeClock
    global dispdata, timeplot, timeplot1
    global passH, passA, shotsA, shotsH, scoreH, scoreA
    timeClock['text'] = "%(T_left)d"% {"T_left": T_left}
    if started == True:
        if T_left > 0:
        #call countdown again after 1000ms (1s)
            T_left -=1
            
        #Calculations
            totalPasses = passH + passA +.001

            if scoreH > scoreA:
                p_g_h= scoreH - scoreA
                p_g_a = 0
            elif scoreA>scoreH:
                p_g_h = 0
                p_g_a =scoreA-scoreH
            else: 
                p_g_a = 0
                p_g_h =0 
            T= (1/180.)*T_left*3.14
            pointsHome = p_g_h  #+(1/180)*T_left*((shotsH/10)+(passH/totalPasses))*3.14 +.001
            pointsHome += T*shotsH/10. + T*passH/totalPasses
            pointsHome += .001
            pointsAway = p_g_a #+ (1/180)*T_left*((shotsA/10)+(passA/totalPasses))*3.14 +.001
            pointsAway += T*shotsA/10. + T*passA/totalPasses
            pointsAway += .001
            pointsTot = pointsHome+pointsAway

            ProbHome= pointsHome/pointsTot
            print(ProbHome)
            print(pointsHome)
            
            dispdata.append(ProbHome)
            timeplot1 += 1
            timeplot.append(timeplot1)
            refresh()
            
            root.after(297000, countdown)
    else:
        root.after(1000, countdown)


#changing the numbers
def starting():
    global started
    started = True
 
    
def stopping():
    global started
    started = False
    
#changes the values for home team
def nClick():
    global scoreH
    global score_home
    scoreH += 1
    score_home['text'] = "Score: %(scoreH)d"% {"scoreH": scoreH}
    
def n1Click():
    global scoreH
    global score_home
    scoreH -= 1
    score_home['text'] = "Score: %(scoreH)d"% {"scoreH": scoreH} 
    
def n2Click():
    global passH
    global passes_home, bind, n2Click
    passH += 1
    passes_home['text'] = "Passes: %(passH)d"% {"passH": passH}
    


def n3Click():
    global passH
    global passes_home
    passH -= 1
    passes_home['text'] = "Passes: %(passH)d"% {"passH": passH}    
    
def n4Click():
    global shotsH
    global shots_home
    shotsH += 1
    shots_home['text'] = "Shots: %(shotsH)d"% {"shotsH": shotsH}
def n5Click():
    global shotsH
    global shots_home
    shotsH -= 1
    shots_home['text'] = "Shots: %(shotsH)d"% {"shotsH": shotsH}
    
 #changes the values for away team
def mClick():
    global scoreA
    global score_away
    scoreA += 1
    score_away['text'] = "Score: %(scoreA)d"% {"scoreA": scoreA}
       
def m1Click():
    global scoreA
    global score_away
    scoreA -= 1
    score_away['text'] = "Score: %(scoreA)d"% {"scoreA": scoreA} 
    
def m2Click():
    global passA
    global passes_away
    passA += 1
    passes_away['text'] = "Passes: %(passA)d"% {"passA": passA}
    
def m3Click():
    global passA
    global passes_away
    passA -= 1
    passes_away['text'] = "Passes: %(passA)d"% {"passA": passA}    
    
def m4Click():
    global shotsA
    global shots_away
    shotsA += 1
    shots_away['text'] = "Shots: %(shotsA)d"% {"shotsA": shotsA}
    
def m5Click():
    global shotsA
    global shots_away
    shotsA -= 1
    shots_away['text'] = "Shots: %(shotsA)d"% {"shotsA": shotsA} 
    
    



   
#Frames for each thingy
homeFrame = Frame(root)
homeFrame.pack(side=LEFT)


awayFrame = Frame(root)
awayFrame.pack(side=RIGHT)

timeFrame= Frame(root)
timeFrame.pack(side=TOP)

graphFrame = Frame(root,width=200, height=200)
graphFrame.pack(side=BOTTOM)


#top section of the gui
Team1=Label(timeFrame, text ="HOME",relief="solid")
Team1.grid(row=10, column=1)

Team2= Label(timeFrame,text="AWAY",relief="solid")
Team2.grid(row=10,column=100)


timeClock = Label(timeFrame, text= "90", relief="solid")
timeClock.grid(row=10, column=50, columnspan =4)
buttonUpc1 = Button(timeFrame, command = cClick,text = "^ ", fg= "green")
buttonDownc2 = Button(timeFrame,command = c1Click,text = "V  ", fg= "red")
buttonUpc1.grid(row=11,column=51)
buttonDownc2.grid(row=12,column=51)

Space1=Label(timeFrame,text="                                               ")
Space1.grid(row=10,column=2)
Space2=Label(timeFrame,text="                                               ")
Space2.grid(row=10,column=55)
start = Button(timeFrame, command = starting, text="Start")
start.grid(row=11,column=50)
stop= Button(timeFrame,command = stopping, text="Stop")
stop.grid(row=12,column=50)

score_home = Label(homeFrame, text= "Score: %(scoreH)d"% {"scoreH": scoreH},relief="solid")
score_home.grid(row=3,column=1)
buttonUp = Button(homeFrame, command = nClick, text = "^", fg= "green")
buttonDown = Button(homeFrame,command = n1Click, text = "V", fg= "red")
buttonUp.grid(row=2, column= 10)
buttonDown.grid(row =6, column= 10)

shots_home = Label(homeFrame, text= "Shots: %(shotsH)d"%{"shotsH": shotsH},relief="solid")
shots_home.grid(row = 12, column=1)
buttonUp2 = Button(homeFrame, command = n4Click,text = "^", fg= "green")
buttonDown2 = Button(homeFrame,command = n5Click,text = "V", fg= "red")
buttonUp2.grid(row=9, column= 10)
buttonDown2.grid(row =15, column= 10)

passes_home = Label(homeFrame, text= "Passes: %(passH)d"%{"passH":passH},relief="solid")
passes_home.grid(row=19,column=1)
buttonUp3 = Button(homeFrame,command = n2Click, text = "^", fg= "green")
buttonUp3.bind("<Shift-f>", n2Click)
buttonDown3 = Button(homeFrame,command = n3Click, text = "V", fg= "red")
buttonUp3.grid(row=17, column= 10)
buttonDown3.grid(row =22, column= 10)
    
score_away = Label(awayFrame, text= "Score: %(scoreA)d"% {"scoreA": scoreA},relief="solid")
score_away.grid(row=3,column=10)
buttonUp6 = Button(awayFrame,command=mClick,text = "^", fg= "green")
buttonDown6 = Button(awayFrame,command=m1Click,text = "V", fg= "red")
buttonUp6.grid(row=2, column= 1)
buttonDown6.grid(row =6, column= 1)

shots_away= Label(awayFrame, text= "Shots: %(shotsA)d"%{"shotsA": shotsA},relief="solid")
shots_away.grid(row = 12, column=10)
buttonUp5 = Button(awayFrame,command=m4Click,text = "^", fg= "green")
buttonDown5 = Button(awayFrame,command=m5Click,text = "V", fg= "red")
buttonUp5.grid(row=9, column= 1)
buttonDown5.grid(row =15, column= 1)

passes_away = Label(awayFrame, text= "Passes: %(passA)d"%{"passA":passA},relief="solid")
passes_away.grid(row=19,column=10)
buttonUp4 = Button(awayFrame,command=m2Click,text = "^", fg= "green")
buttonDown4 = Button(awayFrame,command=m3Click,text = "V", fg= "red")
buttonUp4.grid(row=17, column= 1)
buttonDown4.grid(row =22, column= 1)

line1=Label(homeFrame, text="------------------------")
line1.grid(row=7, column=1)

line2=Label(homeFrame, text="------------------------")
line2.grid(row=16, column=1)

line3=Label(homeFrame, text="------------------------")
line3.grid(row=23, column=1)

line3a=Label(homeFrame, text="------------------------")
line3a.grid(row=1, column=1)

line4=Label(awayFrame, text="------------------------")
line4.grid(row=7, column=10)

line5=Label(awayFrame, text="------------------------")
line5.grid(row=16, column=10)

line6=Label(awayFrame, text="------------------------")
line6.grid(row=23, column=10)

line7=Label(awayFrame, text="------------------------")
line7.grid(row=1, column=10)


f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
a.plot(timeplot,dispdata)

canvas = FigureCanvasTkAgg(f, graphFrame)
canvas.show()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2TkAgg(canvas, graphFrame)
toolbar.update()

canvas._tkcanvas.pack( fill=tk.BOTH, expand=True)

GraphLabel=  Label(graphFrame, text= "Home Team Win Probability", font=("Helvetica", 16),relief="solid")
GraphLabel.pack(side = TOP)



def refresh():
    global dispdata, timeplot, a, canvas,toolbar
    canvas.get_tk_widget().destroy()
    toolbar.destroy()
    a.plot(timeplot,dispdata)

    canvas = FigureCanvasTkAgg(f, graphFrame)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, graphFrame)
    toolbar.update()

    #canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



#Starts timer
countdown()



root.mainloop()
