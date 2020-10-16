from tkinter import *
from PIL import Image,ImageTk,ImageDraw
import time
from math import *

class Clock:
    def __init__(self,root):   #initializing
        self.root=root
        self.root.title("GUL Analog Clock")  #assiging title to the window
        self.root.geometry("1350x700+0+0")   #assigning sizes to window
        self.root.config(bg="#c28285")       #giving background colour to window

        #assigning title name by calling Lable class and placing it using .place() and giving them the location to set
        title=Label(self.root,text="ANALOG CLOCK",bg="#c28285",fg="white",font=("times new roman",50,"bold")).place(x=0,y=50,relwidth=1)

        #drawing a frame using lable class and placing it
        self.frame=Label(self.root,bd=20,relief=SUNKEN)   #setting border and its style
        self.frame.place(x=440,y=150,width=400,height=400)
        self.working()

    def clockimg(self,hr,mins,sec):
        clock=Image.new("RGB",(400,400),("white")) #creating new image using new module
        draw=ImageDraw.Draw(clock)                #where to draw that image

        bg=Image.open("clock.jpg")    #opening my clock face image
        bg=bg.resize((300,300),Image.ANTIALIAS) #resizing the image and used antialias for quality purpose
                                                # (not to damage the quality of the image which we are importing)

        clock.paste(bg,(50,50))               #we have created plan frame in clock
                                            #now we are pasting the clock face inside the plan frame.
       #--clock lines for hours.. did math function for rotating the hand in clock using math module x1,y1,x2,y2
        # used radians for converting into Theta---
        draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=6)
        # --clock lines for minutes---
        draw.line((200, 200, 200+80*sin(radians(mins)),200-80*cos(radians(mins))), fill="blue", width=4)
        # --clock lines for seconds--
        draw.line((200, 200,200+100*sin(radians(sec)),200-100*cos(radians(sec))), fill="green", width=2)
        clock.save("clock_new.png")               #where to save the image

    def working(self):
        h=time.strftime("%H")    #using time module for getting hour
        m=time.strftime("%M")    #using time module for getting minute
        s = time.strftime("%S")  #using time module for getting seconds
        #print(h,m,s)
        hr = (int(h)/12)*360
        mins = (int(m)/60)*360
        sec = (int(s)/60) * 360
        #print(hr,mins,sec)
        self.clockimg(hr, mins, sec)  # calling clockimg function
        self.img=ImageTk.PhotoImage(file="clock_new.png") #uploading our clock_new file in frame
        self.frame.config(image=self.img)      #imposing clock_new image into white frame which we have created earlier
        self.frame.after(200,self.working)   #kept in loop so that it will keep running 

root=Tk()
obj=Clock(root)
root.mainloop()



#---formula---
'''angle_in_radians = angle_in_degrees * math.pi/180
length_of_line = 100
centre_x1 = 250 #we have defined them on line 32
centre_y1 = 250
centre_x2 = centre_x1 + length_of_line * math.sin(angle_in_radians)
centre_y2 = centre_y2 + length_of_line * math.cos(angle_in_radians)'''