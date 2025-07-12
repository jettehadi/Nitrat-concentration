from tkinter import *
from tkinter import ttk
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="mydatabase"
)




def submitact():
   prodactName = inppn.get()
   limsNumber = inpln.get()
   concetration = inpcon.get()
   mycursor = mydb.cursor()
   sql = "INSERT INTO nitrateconcentration (productName, limsNumber, Concentration) VALUES (%s, %s, %s)"
   val = (prodactName , limsNumber, concetration)
   mycursor.execute(sql, val)
   mydb.commit()

def submitactk(event):
   prodactName = inppn.get()
   limsNumber = inpln.get()
   concetration = inpcon.get()
   mycursor = mydb.cursor()
   sql = "INSERT INTO nitrateconcentration (productName, limsNumber, Concentration) VALUES (%s, %s, %s)"
   val = (prodactName , limsNumber, concetration)
   mycursor.execute(sql, val)
   mydb.commit()

def reset():
    inppn.set("")
    limsnuberz.set("")
    tubwight.set("")
    samplewight.set("")
    totalewight.set("")
    peaka1.set("")
    peaka2.set("")
    peaka3.set("")
    dilutionf.set("")
    concentration.set("")
    return

def resetk(event):
    inppn.set("")
    limsnuberz.set("")
    tubwight.set("")
    samplewight.set("")
    totalewight.set("")
    peaka1.set("")
    peaka2.set("")
    peaka3.set("")
    dilutionf.set("")
    concentration.set("")
    return

def go_to_next_element(event):
    event.widget.tk_focusNext().focus()

def go_to_frist_element(event):
    inppn.focus_set()

def jafa (event):
  x = inppn.get()

  if x == "Cucumber" or x=="Tomato" or x=="Carrots" or x=="Onions" or x=="Watermelon" or x=="Melon" or x=="Split pea":

    inpdf .delete(0, END)
    inpdf.insert(0,1)
  else:
    inpdf .delete(0, END)
    inpdf.insert(0,6)


window = Tk()

# Creating object of photoimage class
# Image should be in the same folder
# in which script is saved
p1 = PhotoImage(file = 'info.png')

# Setting icon of master window
window.iconphoto(False, p1)



window.title ("Nitrate calculation Software")
window.geometry('650x600')
#fanctions
def cal_sum():
   ws=float(inpws.get())
   wtu=float(inpwtu.get())
   wto=float(inpwto.get())
   pa1=float(inppa1.get())
   pa2=float(inppa2.get())
   pa3=float(inppa3.get())
   df=float(inpdf.get())

   concetration=((((pa1+pa2+pa3)/3)-62.622)/220.33)*((wto-wtu)/ws)*df
   concetrationR = round(concetration)
   inpcon.delete(0, END)
   inpcon.insert(0,concetrationR)

def cal_sumk(event):
   ws=float(inpws.get())
   wtu=float(inpwtu.get())
   wto=float(inpwto.get())
   pa1=float(inppa1.get())
   pa2=float(inppa2.get())
   pa3=float(inppa3.get())
   df=float(inpdf.get())

   concetration=((((pa1+pa2+pa3)/3)-62.622)/220.33)*((wto-wtu)/(ws-wtu))*df
   concetrationR = round(concetration)
   inpcon.delete(0, END)
   inpcon.insert(0,concetrationR)



# title of the programm
lbl= Label(window, text="Nitrate Concetration Calculator",borderwidth=3, relief="solid", bg= '#00ADB5', fg='#222831',
 font=('Arial', 25),padx=50, pady=30)
lbl.grid(columnspan=4, row=0)


#Enter the product name
lbpn= Label(window, text="Product Name")
lbpn.grid(column=0, row=2, pady=10 )
inppn=ttk.Combobox(window, width = 17)
inppn.bind("<Return>", go_to_next_element)
inppn.bind("<FocusOut>",jafa)


# Adding combobox drop down list
inppn['values'] = ('Tomato',
                   'Cucumber',
                   'Spinach',
                   'Carrots',
                   'Potatoes',
                   'Onions',
                   'Vegetables',
                   'Lettuce',
                   'Cabbage',
                   'Watermelon',
                   'Melon',
                   'Celery',
                   'Split pea')

inppn.grid(column=1, row=2, pady=10)
#Enter the lims number
lblln= Label(window, text="Lims Numbdr", )
lblln.grid(column=0, row=3,pady=10 )
limsnuberz = StringVar()
inpln=Entry(window, width=20, textvariable=limsnuberz)
inpln.grid(column=1, row=3, pady=10 )
inpln.bind("<Return>", go_to_next_element)
#Enter the weight of sample and continer and total
lblw= Label(window, text="Wieght           ", )
lblw.grid(column=0, row=4,pady=10 )
tubwight = StringVar()
inpwtu=Entry(window, width=20,textvariable=tubwight )
inpwtu.grid(column=1, row=4, pady=10)
inpwtu.bind("<Return>", go_to_next_element)
samplewight = StringVar()
inpws=Entry(window, width=20,textvariable=samplewight )
inpws.grid(column=2, row =4, pady=10 )
inpws.bind("<Return>", go_to_next_element)
totalewight = StringVar()
inpwto=Entry(window, width=20,textvariable=totalewight)
inpwto.grid(column=3, row=4,pady=10)
inpwto.bind("<Return>", go_to_next_element)
#Enter the surface area of sample and continer and total
lblw= Label(window, text="Surface Area   " )
lblw.grid(column=0, row=5,pady=10 , padx=2)
peaka1 = StringVar()
inppa1=Entry(window, width=20,textvariable=peaka1 )
inppa1.grid(column=1, row =5, pady=10, padx=2)
inppa1.bind("<Return>", go_to_next_element)
peaka2 = StringVar()
inppa2=Entry(window, width=20, textvariable=peaka2)
inppa2.grid(column=2, row=5, pady=10)
inppa2.bind("<Return>", go_to_next_element)
peaka3 = StringVar()
inppa3=Entry(window, width=20,textvariable=peaka3 )
inppa3.grid(column=3, row=5,pady=10)
inppa3.bind("<Return>", go_to_next_element)
#Enter dilution factor
lbldf=Label(window, text="Dilution Factor", )
lbldf.grid(column=0,row=6, pady=10)
dilutionf = StringVar()
inpdf=Entry(window, width=20,textvariable=dilutionf )
inpdf.grid(column=1, row=6, pady=10)
inpdf.bind("<Return>", go_to_next_element)
#Enter caculated Concentratin
lblcon=Label(window, text="Concentration  ", )
lblcon.grid(column=0,row=7, pady=10 )
concentration= StringVar()
inpcon=Entry(window, width=20,textvariable=concentration)
inpcon.grid(column=1, row=7, pady=10)
inpcon.bind("<Return>", go_to_next_element)
inpcon.bind("<FocusOut>",cal_sumk)


#add button for calculation
btncal=Button(window,text="Calculate", command=cal_sum, width=17)
btncal.grid(column=0,row=8, pady=10)
btncal.bind("<Return>", go_to_next_element)
btnsend=Button(window, text="Send", command=submitact,width=17 )
btnsend.grid(column=1, row=8, pady=10)
btnsend.bind("<Return>",go_to_next_element)
btnsend.bind("<FocusOut>",submitactk)

btnreset=Button(window, text="Reset",width=17, command=reset)
btnreset.grid(column=2, row=8, pady=20)
btnreset.bind("<Return>",go_to_frist_element)
btnreset.bind("<FocusOut>",resetk)
lbl= Label(window, text="Tabriz Food & Drug HPLC Lab",borderwidth=3, relief="solid", bg= '#393E46', fg='#EEEEEE',
font=('Arial', 25),padx=45, pady=30)
lbl.grid(columnspan=4, row=9)
lbl= Label(window, text="Dr. jafar Ettehadi Gargari",
font=('Arial', 10),padx=45)
lbl.grid(column=0, row=10)

window,mainloop()
