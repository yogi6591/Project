#CALCULATOR

from tkinter import *
root=Tk()
root.config(bg="grey")
root.title("Calculator")

operator=" "
input=StringVar()

def click_button(number):
    global operator
    operator=operator+str(number)
    input.set(operator)

def click_clear():
    global operator
    operator=""
    input.set("")

def click_equal():
    global operator
    result=str(eval(operator))
    input.set(result)
    operator=""





entry=Entry(root,width="32",textvariable=input,bd=5,bg="pink",justify='right')
entry.grid(row=0,column=0,columnspan=4)

#Buttons
b1=Button(root,text="7",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(7))
b1.grid(row=2,column=0,)

b2=Button(root,text="8",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(8))
b2.grid(row=2,column=1)

b3=Button(root,text="9",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(9))
b3.grid(row=2,column=2)

b4=Button(root,text="x",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button("*"))
b4.grid(row=2,column=3)

b5=Button(root,text="4",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(4))
b5.grid(row=3,column=0)

b6=Button(root,text="5",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(5))
b6.grid(row=3,column=1)

b7=Button(root,text="6",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(6))
b7.grid(row=3,column=2)

b8=Button(root,text="-",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button("-"))
b8.grid(row=3,column=3)

b9=Button(root,text="1",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(1))
b9.grid(row=4,column=0)

b10=Button(root,text="2",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(2))
b10.grid(row=4,column=1)

b11=Button(root,text="3",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(3))
b11.grid(row=4,column=2)

b12=Button(root,text="+",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button("+"))
b12.grid(row=4,column=3)

b13=Button(root,text="C",width=5,height=2,bd=5,bg="skyblue",command=click_clear)
b13.grid(row=5,column=0)

b14=Button(root,text="0",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button(0))
b14.grid(row=5,column=1)

b15=Button(root,text=".",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button("."))
b15.grid(row=5,column=2)

b16=Button(root,text="/",width=5,height=2,bd=5,bg="skyblue",command=lambda:click_button("/"))
b16.grid(row=5,column=3)

b16=Button(root,text="=",width=27,height=2,bd=5,bg="skyblue",command=click_equal)
b16.grid(row=6,column=0,columnspan=4)


#Label for Search History
label=Label(root,text="Search History")
label.place(x=300,y=30)


root.geometry("150x300")
root.minsize(300,500)
root.maxsize(900,650)
root.mainloop()