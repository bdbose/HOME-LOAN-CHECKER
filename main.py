
import pandas as pd
import sms
import tkinter as tk

file=pd.read_csv("Contact Information.csv")

num_vbl=["What is your age?",
         "Phone number",
         "Loan Amount Required?",
         "Your Salary?(if unemployed write 0)",
         "Loan repay time?(in years)"]

variables=["Name" ,"Email" ,
           "Where are you from?" ,"Phone number" ,
           "What is your age?" ,"Loan Amount Required?" ,
           "Loan repay time?(in years)" ,
           "Your Salary?(if unemployed write 0)",
           "Do you have any emi?"]

for var in num_vbl:
    file[var] = file[var].fillna(value = file[var].mean())

age=[]
phn=[]
loan=[]
time=[]    
name=[]
email=[]
place=[]
salary=[]
emi=[]
c=0
a=[name,email,place,phn,age,loan,time,salary,emi]

for i in variables:
    for j in file[i]:
        a[c].append(j)
    c=c+1    
#print(a)
emi_a=[]
eli=[]
class check:  
    f=0
    def rate(n):
        if(n>=0 and n<=12):
            return 10/1200
        elif(n>12 and n<=36):
            return 12/1200
        else:
            return 14/1200
        
    def emi_calc(p,n):
        r=check.rate(n)
        emi=(p*r*(1+r)**n)/(((1+r)**n)-1)
        emi_a.append(emi)
        total=emi*n
        return total
        
    def check_eli():
        y=0
        n=0
        tex1.delete(0.0,tk.END)
        tex1.insert(tk.END,"STARTING......")
        tex1.insert(tk.END,"\nTHEIR ARE {:<3} ENTRIES...".format(len(age)))
        for i in range(len(age)):
            total=check.emi_calc(loan[i],time[i]*12)
            fu=salary[i]*time[i]*12*0.9
            if(age[i]>=18 and age[i]<=70 and salary[i]>=25000 and fu>=total and emi[i]=="No"):
                msg=name[i]+" is Eligible for Rs"+str(loan[i])+" and can extend Up to Rs"+str(fu)+"."
                sms.send_email(email[i],msg)
                eli.append("Y")
                y=y+1
            else:
                msg=name[i]+" is Not Eligible for Rs"+str(loan[i])+" and can give Up to Rs"+str(fu)+"."
                sms.send_email(email[i],msg)
                eli.append("N")
                n=n+1
        print("DONE")
        tex1.insert(tk.END,"\nNO. of ELigible person are {:<3}".format(y))
        tex1.insert(tk.END,"\nNO. of NON-ELigible person are {:<3}".format(n))
        tex1.insert(tk.END,"\nALL MAIL SENT SUCCESSFULLY")
    def end():
        root.destroy()
          

#print(emi_a)

root=tk.Tk()
root.title("HOME LOAN CHECKER")
root.geometry("300x300")

tk.Label(text="DREAM HOUSING FINANCE",font=40,bg="#CCFFF7").pack()
root.configure(background="#CCFFF7")
tex1=tk.Text(root,height=10,width=35)
tex1.pack()
bu1=tk.Button(root,text="CHECK",command=check.check_eli).place(x=90,y=250)
bu2=tk.Button(root,text="END",command=check.end).place(x=170,y=250)
tex1.insert(0.0,"CLICK CHECK TO START \n AND END BUTTON TO STOP")
root.mainloop()

file['EMI']=emi_a
file['ELIGIBLE']=eli
file.to_csv('result.csv',columns=['Name','EMI','ELIGIBLE',"Loan Amount Required?"],index=False)
