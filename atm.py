
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
ent= tk.Entry(font=("Arial",15), bd=5)
def destroy():
    atm.destroy()
def update():##########################
    global pin
    global pincheck
    nxt1.destroy()
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
    nxt2.destroy()
    ent.destroy()
    Sa.pack(pady=10)
    Cu.pack()  

def option():
    label.destroy()
    Sa.destroy()
    Cu.destroy()
    balancebutton.pack(pady=10)
    withdraw.pack()
def Balanceshow():
    withdraw.destroy()
    balancebutton.destroy()
    label1.config(text="Your Account Balance is " + str(balance))
    label1.pack()
    label1.pack()
    label2 = tk.Label(text='Thank You 🙏', font=("Arial",20))
    label2.pack()
    atm.after(10000,atm.destroy)
def withdrawamount():
    withdraw.destroy()
    balancebutton.destroy()
    label3.pack()    
    entry.pack(pady=10)    
    nxt.pack()#bhut bdhiya button ko pack kiya 
def errorcheck():
    try:
        global z
        global balance
        z = int(entry.get())
        entry.destroy()
        nxt.destroy()
        label3.destroy()#tthis should be focused 
        if (((z % 500) == 0) and (z<= balance)):#first time i used condiitional in it
            balance = (balance - z)
            print(balance)
            label4= tk.Label(text="Your Payment is under Process", font=("Arial",25))
            label4.pack()
            def lab():
                label4.config(text= "Thank You  ", font=("Arial",25))
                labelx=tk.Label(text="🙏",font=("Segoe UI Emoji", 16))
                labelx.pack()
                atm.after(10000,atm.destroy)
                
            label4.after(5000, lab)###########bhut bdhiya combination of label timing and lablel show()
                    
        else:
            label5= tk.Label(text="Error",font=("Arial",20)) 
            label5.pack()
            atm.after(5000,atm.destroy)## yha bhi destroy wala concept use hua h
    except:
        entry.destroy()
        nxt.destroy()
        label3.destroy()
        labelz=tk.Label(text="Please Enter valid literals",font=("Arial",20))
        labelz.pack()

    
    ## atm.after(15000,atm.destroy())
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
atm.mainloop()


    
    
