from tkinter import *


fields = ('Pay Rate','Weekdays and Saturday Hours', 'Sunday Hours', 'Public Holiday Hours', 'Saving Amount', 'Total Pay')
    
def Total_Pay(entries):
    Week_Rate = str(entries["Pay Rate"].get())
    print("Pay Rate", Week_Rate)
    Week_Rate = float(Week_Rate)
    Public_Rate = Week_Rate * 2.5
    Sunday_Rate = Week_Rate * 1.5

    Week_Hours = str(entries["Weekdays and Saturday Hours"].get())
    print("Week Hours", Week_Hours)
    Sunday_Hours = str(entries["Sunday Hours"].get())
    print("Sunday Hours", Sunday_Hours)
    Public_Hours = str(entries["Public Holiday Hours"].get())
    print("Public Hours", Public_Hours)

    Week_Hours = int(Week_Hours)
    Sunday_Hours = int(Sunday_Hours)
    Public_Hours = int(Public_Hours)
    
    Week_Pay = Week_Hours * Week_Rate
    Sunday_Pay = Sunday_Hours * Sunday_Rate
    Public_Pay = Public_Hours * Public_Rate
    Total_Pay = Sunday_Pay + Week_Pay + Public_Pay
    Bank_Pay = Total_Pay * .25

    Week_Pay = format(Week_Pay, '.2f')
    Sunday_Pay = format(Sunday_Pay, '.2f')
    Public_Pay = format(Public_Pay, '.2f')
    Total_Pay = format(Total_Pay, '.2f')
    Bank_Pay = format(Bank_Pay, '.2f')
        
    entries['Total Pay'].delete(0,END)
    entries['Total Pay'].insert(0, Total_Pay)
    print("Total Pay:", Total_Pay)


def Total_Bank(entries):
    Week_Rate = str(entries["Pay Rate"].get())
    print("Pay Rate", Week_Rate)
    Week_Rate = float(Week_Rate)
    Public_Rate = Week_Rate * 2.5
    Sunday_Rate = Week_Rate * 1.5

    Week_Hours = str(entries["Weekdays and Saturday Hours"].get())
    print("Week Hours", Week_Hours)
    Sunday_Hours = str(entries["Sunday Hours"].get())
    print("Sunday Hours", Sunday_Hours)
    Public_Hours = str(entries["Public Holiday Hours"].get())
    print("Public Hours", Public_Hours)

    Week_Hours = int(Week_Hours)
    Sunday_Hours = int(Sunday_Hours)
    Public_Hours = int(Public_Hours)
    
    Week_Pay = Week_Hours * Week_Rate
    Sunday_Pay = Sunday_Hours * Sunday_Rate
    Public_Pay = Public_Hours * Public_Rate
    Total_Pay = Sunday_Pay + Week_Pay + Public_Pay
    Bank_Pay = Total_Pay * .25

    Week_Pay = format(Week_Pay, '.2f')
    Sunday_Pay = format(Sunday_Pay, '.2f')
    Public_Pay = format(Public_Pay, '.2f')
    Total_Pay = format(Total_Pay, '.2f')
    Bank_Pay = format(Bank_Pay, '.2f')
        
    entries['Saving Amount'].delete(0,END)
    entries['Saving Amount'].insert(0, Bank_Pay)
    print("Saving Amount:", Bank_Pay)

def makeform(root, fields):
    entries = {}
    for field in fields:
      row = Frame(root)
      lab = Label(row, width=30, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")              
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
    return entries

def colour(entries):
    return

if __name__ == '__main__':
   root = Tk()
   root.title("Pay Calculator")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: colour(e)))
   b1 = Button(root, text='Total Pay',
          command=(lambda e=ents: Total_Pay(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Saving Amount',
          command=(lambda e=ents: Total_Bank(e)))
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=RIGHT, padx=5, pady=5)
   root.mainloop()
