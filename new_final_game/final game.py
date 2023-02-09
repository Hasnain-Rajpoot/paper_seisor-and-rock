import tkinter as tk
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk,Image
import random
y=tk.Tk()
y.geometry("350x500")

def hi ():
	  f=open("highscore.txt","r")
	  t=f.read()
	  
	  a=tmsg.showinfo("S_C","heigh score   ="+t)
	
#functions
f=open("highscore.txt","r")
t=f.read()
t=int(t)
def reset():
	cmp.set(0)
	pl.set(0)
	cmscore.config(textvariable=cmp)
	plscore.config(textvariable=pl)
def help():
    a=tmsg.showinfo("help","hasnain will help you")
def rate():
    a=tmsg.askquestion("was your experience good","was you experience good")
    if a=="yes":
        tmsg.showinfo("nice","rate us on playstore")
    else:
        tmsg.showinfo("ohh no","tell us whats wrong we will fix")

def te():
    y.configure(bg="teal")
    fb.configure(bg="teal")
def pu():
    y.configure(bg="purple")
def wall():
    y.configure(bg="teal")
def gr():
    y.configure(bg="gray")
def ora():
    y.configure(bg="#6b59b6")    
    
    
    #images
    
y.configure(bg="#6b59b6")
f=Frame(y).place(x=0,y=0)
#r2=ImageTk.PhotoImage(file="bd2.jpg")
#global com
#background=Label(y,image=r2,bd=0).place(x=0,y=0)
y.title("game")
global p22
p22=ImageTk.PhotoImage(file="p222.jpg")
global s22
s22=ImageTk.PhotoImage(file="s222.jpg")
global r22	
r22=ImageTk.PhotoImage(Image.open("r222.jpg"))

play=Label(y,image=p22,bd=0)
play.place(x=430,y=300)



#main functions
def sei():
	global com
	global play
	c=cmp.get()
	l=pl.get()
	a=random.randrange(1,4)
	if a==1:
			#c=c+1
		#cmp.set(c)
		l=l+1
		pl.set(l)
		cmscore.config(textvariable=cmp)
		plscore.config(textvariable=pl)
		wi.set("you win")
		win.config(textvariable=wi)
		comp_img.config(image=p22)
		play.config(image=s22)
	if a==2:
		#cmscore.config(textvariable=cm)
		plscore.config(textvariable=pl)
		wi.set("   Draw")
		win.config(textvariable=wi)
		comp_img.config(image=s22)
		play.config(image=s22)
	if a==3:
		c=c+1
		cmp.set(c)
		#l=l+1
		#pl.set(l)
		cmscore.config(textvariable=cmp)
		plscore.config(textvariable=pl)
	#	cmscore.config(textvariable=cm)
		plscore.config(textvariable=pl)
		wi.set("you lose")
		win.config(textvariable=wi)
		comp_img.config(image=r22)
		play.config(image=s22)
	if l > t:
                f=open("highscore.txt","w")
                f.write(str(l))
                f.close()


def rock ():
	global com
	global play
	#cmp global
	c=cmp.get()
	l=pl.get()
	
	
	a=random.randrange(1,4)
	if a==1:
			#c=c+1
		#cmp.set(c)
		l=l+1
		pl.set(l)
		cmscore.config(textvariable=cmp)
		plscore.config(textvariable=pl)
		
		
		wi.set("you win")
		win.config(textvariable=wi)
		comp_img.config(image=p22)
		play.config(image=r22)
	if a==2:
		#c=c+1
		#cmp.set(c)
		l=l+1
		pl.set(l)
		cmscore.config(textvariable=cmp)
		plscore.config(textvariable=pl)
		wi.set("you win")
		win.config(textvariable=wi)
		comp_img.config(image=s22)
		play.config(image=r22)
	if a==3:
	
		wi.set("   Draw")
		win.config(textvariable=wi)
		comp_img.config(image=r22)
		play.config(image=r22)
	if l > t:
                f=open("highscore.txt","w")
                f.write(str(l))
                f.close()

def pap():
	global com
	global play
	c=cmp.get()
	l=pl.get()
	a=random.randrange(1,4)
	if a==1:
		wi.set("    Draw")
		win.config(textvariable=wi)
		comp_img.config(image=p22)
		play.config(image=p22)
	if a==2:
		c=c+1
		cmp.set(c)
		#l=l+1
		#pl.set(l)
		cmscore.config(textvariable=cmp)
		plscore.config(textvariable=pl)
		wi.set("You lose")
		win.config(textvariable=wi)
		comp_img.config(image=s22)
		play.config(image=p22)
	if a==3:
		c=c+1
		cmp.set(c)
		#l=l+1
		#pl.set(l)
		cmscore.config(textvariable=cmp)
		plscore.config(textvariable=pl)
		wi.set("You lose")
		win.config(textvariable=wi)
		comp_img.config(image=r22)
		play.config(image=p22)
		
	if l > t:
                f=open("highscore.txt","w")
                f.write(str(l))
                f.close()
	
def exit():
	y.destroy()
	pass
	
	
fb=Label(y,text="paper seisor and rock",fg="white",bg="#6b59b6",font="comiscansms 18 bold")
fb.pack(fill=X,pady=6)



#labels
comp_img=tk.Label(y,image=p22)
comp_img.place(x=20,y=300)


f=Label(y,text="computer",fg="white",bg="#6b59b6",font="comiscansms 15 bold")
f.place(x=20,y=200)
f=Label(y,text="vs",fg="white",bg="#6b59b6",font="comiscansms 15 bold")
f.place(x=340,y=400)

wi=StringVar()
wi.set("who win?")
win=Label(y,textvariable=wi,fg="white",font="comiscansms 15 bold",bd=0,bg="#6b59b6",pady=10)
win.place(x=240,y=740)
fhjb=Label(y,text="player",fg="white",bg="#6b59b6",font="comiscansms 15 bold",width=7)
fhjb.place(x=480,y=200)
paper=Button(y,text="Paper",width=13,font="comiscansms 9 bold",fg="white",bg="red",command=pap).place(x=20,y=1000)
seisor=Button(y,text="Seisor",width=13,font="comiscansms 9 bold",fg="red",bg="yellow",command=sei).place(x=380,y=1000)
rock=Button(y,text="Rock",width=16,font="comiscansms 9 bold",fg="white",bg="orange",command=rock).place(x=150,y=1120)
reset=Button(y,text="Restart",width=9,font="comiscansms 9 bold",fg="white",bg="teal",command=reset).place(x=260,y=1300)
exit=Button(y,text="Exit",width=5,font="comiscansms 9 bold",fg="white",bg="teal",command=exit)
exit.place(x=520,y=1380)
highscore=Button(y,text="heigh score",width=8,font="comiscansms 9 bold",fg="white",bg="teal",command=hi).place(x=20,y=1380)
cmp=IntVar()
cmp.set(0)
cmscore=Label(y,textvariable=cmp,font="comiscansms 18 bold",bg="#6b59b6",fg="white")
cmscore.place(x=50,y=740)
pl=IntVar()
pl.set(0)
plscore=Label(y,textvariable=pl,font="comiscansms 18 bold",bg="#6b59b6",fg="white")
plscore.place(x=620,y=740)


#menues
            
menu2=Menu(y)
m1=Menu(menu2,tearoff=0)
m1.add_command(label="teal",command=te)
m1.add_command(label="purple",command=pu)
m1.add_command(label="wall",command=wall)
m1.add_command(label="gray",command=gr)
m1.add_command(label="orange",command=ora)
menu2.add_cascade(label="background colour change",menu=m1)
menu2.add_command(label="help",command=help)
menu2.add_command(label="Rate us",command=rate)
y.config(menu=menu2)             
menu2=Menu(y)
m1=Menu(menu2,tearoff=0)
m1.add_command(label="teal",command=te)
m1.add_command(label="purple",command=pu)
m1.add_command(label="wall",command=wall)
m1.add_command(label="gray",command=gr)
m1.add_command(label="Default colur",command=ora)
menu2.add_cascade(label="background colour change",menu=m1)
menu2.add_command(label="help",command=help)
menu2.add_command(label="Rate us",command=rate)
y.config(menu=menu2)


y.mainloop()
