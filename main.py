from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk

root=Tk()
root.geometry("1350x750+0+0")
root.title("Fast Food Restaurant")

Tops=Frame(root, width=1350, height=100, bd= 12, relief="raise")
Tops.pack(side=TOP)
lblTitle= Label(Tops, font=('arial', 50, 'bold'),text="\tFast Food Restaurant\t\t\t")
lblTitle.grid(row =0, column=0)

BottomMainFrame= Frame(root, width=1350, height=650, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1= Frame(BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f1.pack(side=LEFT)
f2= Frame(BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f2.pack(side=LEFT)
f2TOP = Frame(f2, width=450, height=350, bd=4, relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM= Frame(f2, width=450, height=300, bd=4, relief="raise")
f2BOTTOM.pack(side=BOTTOM)

f3= Frame (BottomMainFrame, width=450, height=650, bd=12, relief="raise")
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varFries =StringVar()
varSalad= StringVar()
varHamBurger= StringVar()
varOnionRings= StringVar()
varChickenSalad= StringVar()
varFishSandwich= StringVar()
varCheeseSandwich= StringVar()
varChickenSandwich= StringVar()
varHashBrown= StringVar()
varToastedBagels= StringVar()
varPancakes= StringVar()
varPineappleStick= StringVar()
varChocolateMuffin= StringVar()

varFries.set("0")
varSalad.set("0")
varHamBurger.set("0")
varOnionRings.set("0")
varChickenSalad.set("0")
varFishSandwich.set("0")
varCheeseSandwich.set("0")
varChickenSandwich.set("0")
varHashBrown.set("0")
varToastedBagels.set("0")
varPancakes.set("0")
varPineappleStick.set("0")
varChocolateMuffin.set("0")


#Frame 1
lblMeal= Label(f1, font=('arial', 18, 'bold'), text="Fast Food Meal and Vegetarian")
lblMeal.grid(row=0, column=0)

Fries= Checkbutton(f1, text="Fries", variable=var1, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
txtFries= Entry(f1,font=('arial', 18, 'bold'), textvariable= varFries, width=6, justify='left', state=DISABLED)
txtFries.grid(row=1, column=1)

Salad= Checkbutton(f1, text="Salad", variable=var2, onvalue=1, offvalue=0,
                  font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
txtSalad= Entry(f1,font=('arial', 18, 'bold'), textvariable= varSalad, width=6, justify='left', state=DISABLED)
txtSalad.grid(row=2, column=1)

HamBurger= Checkbutton(f1, text="Hamburger", variable=var3, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)
txtHamburger= Entry(f1,font=('arial', 18, 'bold'), textvariable= varHamBurger, width=6, justify='left', state=DISABLED)
txtHamburger.grid(row=3, column=1)


OnionRings= Checkbutton(f1, text="Onion Rings", variable=var4, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)
txtOnionRings= Entry(f1,font=('arial', 18, 'bold'), textvariable= varOnionRings, width=6, justify='left', state=DISABLED)
txtOnionRings.grid(row=4, column=1)


ChickenSalad= Checkbutton(f1, text="Chicken Salad", variable=var5, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)
txtChickenSalad= Entry(f1,font=('arial', 18, 'bold'), textvariable= varChickenSalad, width=6, justify='left', state=DISABLED)
txtChickenSalad.grid(row=5, column=1)

lblSandwich= Label(f1, font=('arial', 20, 'bold'), text="\nSandwiches\n")
lblSandwich.grid(row=6, column=0)

FishSandwich= Checkbutton(f1, text="Fish Sandwich", variable=var6, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=7, column=0, sticky=W)
txtFishSandwich= Entry(f1,font=('arial', 18, 'bold'), textvariable= varFishSandwich, width=6, justify='left', state=DISABLED)
txtFishSandwich.grid(row=7, column=1)


CheeseSandwich= Checkbutton(f1, text="Cheese Sandwich", variable=var7, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=8, column=0, sticky=W)
txtCheeseSandwich= Entry(f1,font=('arial', 18, 'bold'), textvariable= varFries, width=6, justify='left', state=DISABLED)
txtCheeseSandwich.grid(row=8, column=1)


ChickenSandwich= Checkbutton(f1, text="Chicken Sandwich", variable=var8, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold')).grid(row=9, column=0, sticky=W)
txtChickenSandwich= Entry(f1,font=('arial', 18, 'bold'), textvariable= varChickenSandwich
                          , width=6, justify='left', state=DISABLED)
txtChickenSandwich.grid(row=9, column=1)

lblspace=Label(f1, text="\n\n\n\n\n\n\n\n\n")
lblspace.grid(row=10, column=0)

#Frame 2

lblMeal= Label(f2TOP, font=('arial', 18, 'bold'), text="Desserts\n")
lblMeal.grid(row=0, column=0)

HashBrown= checkbutton(f2TOP, text="Hash Brown", variable=var9, onvalue=1, offvalue=0,
                       font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
txtHashBrown= Entry(f2TOP, font=('arial', 18, 'bold'), textvariable= varHashBrown, width=6, justify='left', state=DISABLED)
txt.HashBrown.grid(row=1, column=1)

ToastedBagel= checkbutton(f2TOP, text="Toasted Bagel", variable=var10, onvalue=1, offvalue=0,
                       font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
txtToastedBagel= Entry(f2TOP, font=('arial', 18, 'bold'), textvariable= varHashBrown, width=6, justify='left', state=DISABLED)
txt.ToastedBagel.grid(row=2, column=1)

Pancakes= checkbutton(f2TOP, text="Hash Brown", variable=var9, onvalue=1, offvalue=0,
                       font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
txtHashBrown= Entry(f2TOP, font=('arial', 18, 'bold'), textvariable= varHashBrown, width=6, justify='left', state=DISABLED)
txt.HashBrown.grid(row=1, column=1)

    

root.mainloop()
