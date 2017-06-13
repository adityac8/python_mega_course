from Tkinter import *
def km():
	print "Sucess"
	kilo=float(kiloTf.get())
	gram=kilo*1000
	pound=kilo*2.20462
	ounce=kilo*35.274
	t1.insert(END,gram)
	t2.insert(END,pound)
	t3.insert(END,ounce)


window = Tk()
kiloTf=StringVar()

lbl1 = Label(window,text="Kg")
e1 = Entry(window,textvariable=kiloTf)
b1 = Button(window,text="Convert",command=km)
t1 = Text(window,height=1,width=20)
t2 = Text(window,height=1,width=20)
t3 = Text(window,height=1,width=20)


lbl1.grid(row=0 , column=0)
e1.grid(row=0 , column=1) 
b1.grid(row=0 , column=2)
t1.grid(row=1 , column=0) 
t2.grid(row=1 , column=1) 
t3.grid(row=1 , column=2) 
window.mainloop()