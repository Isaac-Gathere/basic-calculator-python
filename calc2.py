from tkinter import*

def btnClick(numbers):
           global operator
           operator = operator + str(numbers)
           text_Input.set(operator)         
def ClrButton():
         global operator
         operator =""
         text_Input.set("")

def equals():
         global operator
         total = str(eval(operator))
         text_Input.set(total)
         operator = ""
            
cal = Tk()
cal.title('SIMPLE CALCULATOR')

operator = ""
text_Input = StringVar()
 
 # entry field
txtDisplay = Entry(cal,font = ("arial",20,"bold"),textvariable=text_Input, bd=30, insertwidth=4, bg="red",justify="right").grid(columnspan=4)


# row 1

btn7=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="7", bg='powder blue',command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="8",bg='powder blue',command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="9",bg='powder blue',command=lambda:btnClick(9)).grid(row=1,column=2)

btn_add=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="+",bg='powder blue',command=lambda:btnClick("+")).grid(row=1,column=3)

# row 2
btn4=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="4", bg='powder blue',command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="5",bg='powder blue',command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="6",bg='powder blue',command=lambda:btnClick(6)).grid(row=2,column=2)

btnsub=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="-",bg='powder blue',command=lambda:btnClick('-')).grid(row=2,column=3)

# row 3

btn1=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="1",bg='powder blue',command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="2",bg='powder blue',command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="3", bg='powder blue',command=lambda:btnClick(3)).grid(row=3,column=2)


btn_multiply=Button(cal,padx=16,pady=16,bd=8, fg='black'
,font=('arial',20,'bold'),text="*",bg='powder blue',command=lambda:btnClick("*")).grid(row=3,column=3)

#row 4

btn_zero=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="0", bg='powder blue',command=lambda:btnClick(0)).grid(row=4,column=0)

btn_clear=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="C",bg='powder blue',command=lambda:ClrButton()).grid(row=4,column=1)

btn_div=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="/",bg='powder blue',command=lambda:btnClick('/')).grid(row=4,column=2)
btn_equals=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="=",bg='powder blue',command=lambda:equals()).grid(row=4,column=3)

# row 5
# press exit to quit

button_quit= Button(cal,padx=120,pady=16,bd=8, fg='black',font=('arial',20,'bold'),text="EXIT",bg='powder blue',command=cal.quit).grid(row=5,columnspan=4)



cal.mainloop()

