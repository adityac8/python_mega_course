from Tkinter import *
import backend

def get_selected_row(event):
	global selected_tuple
	index=list1.curselection()[0]
	selected_tuple=list1.get(index)
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)
	e1.insert(END,selected_tuple[1])
	e2.insert(END,selected_tuple[2])
	e3.insert(END,selected_tuple[3])
	e4.insert(END,selected_tuple[4])

def view_command():
	list1.delete(0,END)
	rows=backend.view()
	for row in rows:
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	Title  = titleTf.get()
	Author = authorTf.get()
	Year   = yearTf.get()
	ISBN   = isbnTf.get()
	rows   = backend.search(Title,Author,Year,ISBN)
	for row in rows:
		list1.insert(END,row)

def insert_command():
	list1.delete(0,END)
	Title  = titleTf.get()
	Author = authorTf.get()
	Year   = yearTf.get()
	ISBN   = isbnTf.get()
	rows   = backend.insert(Title,Author,Year,ISBN)
	list1.insert(END,"Success")

def update_command():
	list1.delete(0,END)
	Id     = selected_tuple[0]
	Title  = titleTf.get()
	Author = authorTf.get()
	Year   = yearTf.get()
	ISBN   = isbnTf.get()
	rows   = backend.update(Id,Title,Author,Year,ISBN)
	list1.insert(END,"Success")

def delete_command():
	list1.delete(0,END)
	# rows   = backend.delete(1)
	t = selected_tuple[0]
	backend.delete(t)
	list1.insert(END,"Success")

def clear_command():
	list1.delete(0,END)

window=Tk()

window.wm_title("Book Store")

lbl1=Label(window,text="Title")
lbl2=Label(window,text="Author")
lbl3=Label(window,text="Year")
lbl4=Label(window,text="ISBN")

titleTf=StringVar()
authorTf=StringVar()
yearTf=StringVar()
isbnTf=StringVar()

e1=Entry(window,textvariable=titleTf)
e2=Entry(window,textvariable=authorTf)
e3=Entry(window,textvariable=yearTf)
e4=Entry(window,textvariable=isbnTf)

list1=Listbox(window,height=6,width=35)

scroll1=Scrollbar(window)

b1=Button(window,text="View All"    ,width=12,command=view_command)
b2=Button(window,text="Search Entry",width=12,command=search_command)
b3=Button(window,text="Add Entry"   ,width=12,command=insert_command)
b4=Button(window,text="Update"      ,width=12,command=update_command)
b5=Button(window,text="Delete"      ,width=12,command=delete_command)
b6=Button(window,text="Clear"       ,width=12,command=clear_command)
b7=Button(window,text="Close"       ,width=12,command=window.destroy)

e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)

lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=2)
lbl3.grid(row=1,column=0)
lbl4.grid(row=1,column=2)

list1.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll1.grid(row=2,column=2,rowspan=6)

b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=5,column=3)
b5.grid(row=6,column=3)
b6.grid(row=7,column=3)
b7.grid(row=8,column=3)

list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()