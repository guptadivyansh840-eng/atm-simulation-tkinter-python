
import tkinter as tk
pincheck = 0
balance= 5000
z=0
pin= 3864
atm= tk.Tk()
atm.configure(bg="lightblue")
atm.title("ATM")
atm.geometry("300x300")
label=tk.Label(text="PLEASE ENTER YOUR CARD",font=("Arial",25, "bold"), bg="lightblue")
label.pack()
def mainmenu():
    # You must reset the text here, otherwise it stays as "Select your Account Type"
    label.config(text="PLEASE ENTER YOUR CARD") 
    label.pack()
    nxt1.pack() # Bring back the button to start the process again
    ent.delete(0,tk.END)


def restart():
    label4.pack_forget()
    mainmenu()

ent= tk.Entry(font=("Arial",15), bd=5)
def remaining_bal():
    rembutton.pack_forget()  
    label4.config(text= "Your Remaining Balance is " + str(balance),font=("Arial",20))
    
    atm.after(5000, restart)
    
def update():##########################
    global pin
    global pincheck
    nxt1.pack_forget()
    label.config(text="Enter you pin")
    ent.pack(pady=10)
    nxt2.pack()
def check():
    pincheck = int(ent.get())#####
    
    if pincheck == pin:
        changelabeltext()
    else:
        label.config(text="your password is wrong")
        nxt2.config(state= "disabled")
        
        atm.after(10000, destroy)######### Yha destroy() likhne pe turant execute ho ja rha tha properly not working
                                ########## whhi destroy likhne pe shi chal rha h
    
def changelabeltext():#######################
    label.config(text="Select your Account Type")
    nxt2.pack_forget()
    ent.pack_forget()
    Sa.pack(pady=10)
    Cu.pack()  

def option():
    label.pack_forget()
    Sa.pack_forget()
    Cu.pack_forget()
    balancebutton.pack(pady=10)
    withdraw.pack()
def Balanceshow():
    withdraw.pack_forget()
    balancebutton.pack_forget()
    label1.config(text="Your Account Balance is " + str(balance))
    label1.pack()
    label2 = tk.Label(text='Thank You ', font=("Arial",20))
    label2.pack()
    atm.after(10000,atm.destroy)
def withdrawamount():
    withdraw.pack_forget()
    balancebutton.pack_forget()
    label3.pack()    
    entry.pack(pady=10)    
    nxt.pack()#bhut bdhiya button ko pack kiya 
def errorcheck():
    try:
        global z
        global balance
        z = int(entry.get())
        entry.pack_forget()
        nxt.pack_forget()
        label3.pack_forget()#tthis should be focused 
        if (((z % 500) == 0) and (z<= balance)):#first time i used condiitional in it
            balance = (balance - z)#balance updated
            print(balance)
            label4.pack()
            def lab():
                label4.config(text= "Thank You  ", font=("Arial",25))
            
    
                rembutton.pack(pady=10)
            label4.after(5000, lab)
                
        else:
            label5= tk.Label(text="Error",font=("Arial",20)) 
            label5.pack()
            atm.after(5000,atm.destroy)## yha bhi destroy wala concept use hua h
    except:
        entry.pack_forget()
        nxt.pack_forget()
        label3.pack_forget()
        labelz=tk.Label(text="Please Enter valid literals",font=("Arial",20))
        labelz.pack()

    
    ## atm.after(15000,atm.destroy())

label4= tk.Label(text="Your Payment is under Process", font=("Arial",25))
nxt1= tk.Button(text="NEXT",font=("Arial",20),command=update,bg="Yellow",bd=10)
nxt1.pack()
nxt2= tk.Button(text="NEXT",font=("Arial",15, "bold"),command= check ,bd=10)
label3= tk.Label(text="***Enter Your Withdrawal Amount in multiples of 500")
entry= tk.Entry(font=("Arial",15), bd=5)
withdraw = tk.Button(text="Withdraw Money",font=("Arial",14),command= withdrawamount)
label1 = tk.Label(font=("Arial",20))
balancebutton =tk.Button(text="Check Balance",font=("Arial",14),command= Balanceshow)
Sa=tk.Button(text="Savings",font=("Arial",14),command= option)
Cu=tk.Button(text="Current", font=("Arial",14),command= option)
nxt= tk.Button(text="ENTER",font=("Arial",15),command = errorcheck)
rembutton = tk.Button(text="Remaining Balance", font=("Arial",18),fg="Red",command= remaining_bal)
atm.mainloop()


    
    
