from tkinter import *
import random
import time

root=Tk()
root.geometry('1300x700+0+0')
root.title('Fast Food Management System')
textInput=StringVar()
operator=''

tops=Frame(root,width=1200,height=50,bg='salmon',relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root,width=850,height=650,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=400 ,height=650,relief=SUNKEN)
f2.pack(side=RIGHT)
#FOR time
localtime=time.asctime(time.localtime(time.time()))
####################################
#Heading lables
lblInfo=Label(tops,font=('arial',30,'bold'),text='Fast Food Management System',fg='Steel blue',bd=10)
lblInfo.grid(row=0,column=0)
lblInfo=Label(tops,font=('arial',10,'bold'),text=localtime,fg='Steel blue',bd=10)
lblInfo.grid(row=1,column=0)
####################################
#Display number for calculator

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    textInput.set(operator)
####clearing function

def clear_scr():
    global operator
    operator=''
    textInput.set('')
    

def equ():
    global operator
    sumup=str(eval(operator))
    textInput.set(sumup)
    operator = ''

def TOTAL():
    x=random.randint(12908,50879)
    randomRef=str(x)
    rand.set(randomRef)

    cost_fries=float(fries.get())
    cost_burger=float(burger.get())
    cost_filet=float(filet.get())
    cost_chicken=float(chicken.get())
    cost_cheese=float(cheese.get())
    cost_drink=float(drink.get())

    costFries=cost_fries * 99.0
    costBurger=cost_burger * 500.0
    costFilet=cost_filet * 326.0
    costChicken=cost_chicken * 230.0
    costCheese=cost_cheese * 290.0
    costDrink= cost_drink * 50.0

    costofMeal= 'Rs.',str('%.2f' % (costFries + costBurger + costFilet + costChicken + costCheese + costDrink))

    payTax=((costFries + costBurger + costFilet + costChicken + costCheese + costDrink) * 0.23)

    TotalCOST=(costFries + costBurger + costFilet + costChicken + costCheese + costDrink)
    service_CHARGE=((costFries + costBurger + costFilet + costChicken + costCheese + costDrink)/99)

    Service='Rs.' ,str('%.2f' % service_CHARGE)

    OverallCOST='Rs.',str('%.2f' % payTax)
    paidTax='Rs.',str('%.2f' % payTax)

    service.set(Service)
    cost.set(costofMeal)
    tax.set(payTax)
    sub.set(costofMeal)
    total.set(OverallCOST)
    
    
def exitl():
    root.destroy()

def reSet():
    rand.set('')
    fries.set('')
    burger.set('')
    filet.set('')
    chicken.set('')
    cheese.set('')
    drink.set('')
    cost.set('')
    service.set('')
    tax.set('')
    sub.set('')
    total.set('')

###############################
display=Entry(f2,font=('arial',20,'bold'),textvariable=textInput,bd=20,
              insertwidth=12,bg='pale green',justify='right')
display.grid(columnspan=4)
##Buttons
button7=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='7',bg='pale green',
               command=lambda:btnClick(7)).grid(row=2,column=0)
button8=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='8',bg='pale green',
               command=lambda:btnClick(8)).grid(row=2,column=1)
button9=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='9',bg='pale green',
               command=lambda:btnClick(9)).grid(row=2,column=2)
buttonAdd=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='+',bg='pale green',
               command=lambda:btnClick('+')).grid(row=2,column=3)
##################################
button4=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='4',bg='pale green',
               command=lambda:btnClick(4)).grid(row=3,column=0)
button5=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='5',bg='pale green',
               command=lambda:btnClick(5)).grid(row=3,column=1)
button6=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='6',bg='pale green',
               command=lambda:btnClick(6)).grid(row=3,column=2)
buttonSub=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='-',bg='pale green',
               command=lambda:btnClick('-')).grid(row=3,column=3)
#####################################
button1=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='1',bg='pale green',
               command=lambda:btnClick(1)).grid(row=4,column=0)
button2=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='2',bg='pale green',
               command=lambda:btnClick(2)).grid(row=4,column=1)
button3=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='3',bg='pale green',
               command=lambda:btnClick(3)).grid(row=4,column=2)
buttonMul=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='*',bg='pale green',
               command=lambda:btnClick('*')).grid(row=4,column=3)
#####################################
button0=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='0',bg='pale green',
               command=lambda:btnClick(0)).grid(row=5,column=0)

buttonClear=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='C',bg='pale green',
               command=clear_scr).grid(row=5,column=1)


buttonEqual=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='=',bg='pale green',
               command=equ).grid(row=5,column=2)
buttonDiv=Button(f2,padx=16,bd=8,fg='black',font=('arial',20,'bold'),
               text='/',bg='pale green',
               command=lambda:btnClick('/')).grid(row=5,column=3)

#############################
#Info Panel
rand=StringVar()
fries=StringVar()
burger=StringVar()
filet=StringVar()
chicken=StringVar()
cheese=StringVar()
drink=StringVar()
cost=StringVar()
service=StringVar()
tax=StringVar()
sub=StringVar()
total=StringVar()

lblRef=Label(f1,font=('arial',16 ,'bold'),text='Reference#',bd=16,anchor='w')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1,font=('arial',16 ,'bold'),textvariable=rand,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtRef.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16 ,'bold'),text='Large Fries',bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16 ,'bold'),textvariable=fries,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtFries.grid(row=1,column=1)


lblBurger=Label(f1,font=('arial',16 ,'bold'),text='Burger Meal',bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16 ,'bold'),textvariable=burger,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtBurger.grid(row=2,column=1)

lblFilet=Label(f1,font=('arial',16 ,'bold'),text='Filet Meal',bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial',16 ,'bold'),textvariable=filet,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtFilet.grid(row=3,column=1)

lblChicken=Label(f1,font=('arial',16 ,'bold'),text='Chicken Meal',bd=16,anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial',16 ,'bold'),textvariable=chicken,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtChicken.grid(row=4,column=1)


lblCheese=Label(f1,font=('arial',16 ,'bold'),text='Cheese Meal',bd=16,anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial',16 ,'bold'),textvariable=cheese,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtCheese.grid(row=5,column=1)

lblDrink=Label(f1,font=('arial',16 ,'bold'),text='Drinks',bd=16,anchor='w')
lblDrink.grid(row=0,column=2)
txtDrink=Entry(f1,font=('arial',16 ,'bold'),textvariable=drink,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtDrink.grid(row=0 ,column=3)

##############costing part#############

lblCost=Label(f1,font=('arial',16 ,'bold'),text='Cost of Meal',bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16 ,'bold'),textvariable=cost,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtCost.grid(row=1,column=3)


lblService=Label(f1,font=('arial',16 ,'bold'),text='Service Charges',bd=16,anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial',16 ,'bold'),textvariable=service,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtService.grid(row=2,column=3)


lblStateTax=Label(f1,font=('arial',16 ,'bold'),text='State Tax',bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16 ,'bold'),textvariable=tax,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal=Label(f1,font=('arial',16 ,'bold'),text='Sub Total',bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16 ,'bold'),textvariable=sub,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotal=Label(f1,font=('arial',16 ,'bold'),text='Total Cost ',bd=16,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16 ,'bold'),textvariable=total,bd=10,insertwidth=4,
             bg='powder blue',justify='right')
txtTotal.grid(row=5,column=3)

#############################

###Buttons for calculation
buttonTotal=Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',20,'bold'),
              width=10, text='Total',bg='powder blue',
               command=TOTAL).grid(row=7,column=1)

buttonreset=Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',20,'bold'),
               width=10,text='Reset',bg='powder blue',
               command=reSet).grid(row=7,column=2)


buttonExit=Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',20,'bold'),
               width=10,text='Exit',bg='powder blue',
               command=exitl).grid(row=7,column=3)




root.mainloop()
