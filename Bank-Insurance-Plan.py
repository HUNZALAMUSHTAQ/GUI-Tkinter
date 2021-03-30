# Making GUI with help of Tkinter
from tkinter import Tk, Label, Button, Frame, Entry,Listbox,Scrollbar,filedialog
# Importing Keywords
from tkinter import  END,Y,VERTICAL,EXTENDED,RIGHT,ANCHOR
# importing Matplotlib for insurance plan bar plots
from matplotlib import pyplot as plt

master_db = []

def delete_it():
    data_list.delete(ANCHOR)
    print(data_list.get(ANCHOR))
    print(data_list.get(ANCHOR))
    print(master_db)

def save_file():
    print('Saving..')
    file_save=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    for data in data_list.get(0,END):
        data=list(data)
        file_save.write(data[0] + ',')
        file_save.write(data[1] + ',')
        file_save.write(data[2] + ',')
        file_save.write(str(data[3]))
        file_save.write(',' + '\n')
    file_save.close()

def show():
    data_list.delete(0, END)
    if entry_search.get() == '':
        browse_show.configure(text="File Opened: " + filen)
        print('No Data Exists')
        for i in master_db:
            data_list.insert(END,i)

    else:
        browse_show.configure(text="File Opened: " + filen)
        data_list.delete(0, END)
        for i in master_db:
            data_list.insert(END,i)
def search():
    for x in range(len(master_db)):

        if master_db[x][0] == entry_search.get():
            browse_show.configure(text=":)" , fg='green')
            data_list.delete(0, END)
            return data_list.insert(0, master_db[x])
        elif entry_search.get()=='':
            browse_show.configure(text="Enter any data")
        else:
            browse_show.configure(text="Not found")

def append_data():
    name=entry_name.get()
    age=entry_age.get()
    amount=entry_amount.get()
    cnic=entry_cnic.get()
    if name=='' or age=='' or amount=='' or cnic=='':
        browse_show.configure(text="Please Enter Full Data")
    else:
        browse_show.configure(text=":)",fg='blue')
        data=[name,age,amount,cnic]
        data_list.insert(END,data)
        master_db.append(data)
        print(master_db)
filen=''
def load_file():
    global filen
    master_db.clear()
    data_list.delete(0, END)
    g_filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("Text files","*.txt*"),("all files","*.*")))
    if g_filename=='':
        browse_show.configure(text="No File Opened")
    else:
        browse_show.configure(text="File Opened: " + g_filename)

        filen=g_filename
    f = open(g_filename, 'r')
    for records in f:
        records = records.split(',')
        master_db.append([records[0], records[1], records[2],records[3]])
    f.close()
    print(master_db)
    f = open(g_filename, 'r')
    for i in master_db:
        data_list.insert(END,i)
    f.close()

def insurance_analysis():

    present_year=str(present_year_entry.get())
    year_plans=[]
    how_many_years=int(insurance_years.get())
    for x in range(how_many_years):
        k = int(present_year[2:4]) + x # this will slice str present year into like 2021 to 21 and iterate 21
        y = str(present_year[0:2]) + str(k) # this will slice str present year 2021 to 20 and concetenate iterate years
        year_plans.append(y)
    profit_y=[] # profit per year

    amount=int(entry_amount.get())
    for x in range(len(year_plans)):
        y = 0
        y = amount * 0.1 * 12 # 10% of profit per month
        amount = y + amount
        profit_y.append(amount)
    total_profit=sum(profit_y) # its the total profit you will get after completion of given years
    return  year_plans,profit_y,total_profit
def placing_graph():
    data = insurance_analysis()
    x_year=data[0] # x denotes that it will be on x axis
    y_profit_per_year=data[1] # y denotes that it will b in y axis
    total_profit=data[2]
    plt.style.use('fivethirtyeight')
    plt.bar(x_year,y_profit_per_year)
    plt.title('Profit Analysis')
    plt.xlabel('Years')
    plt.ylabel('Profits')
    plt.tight_layout()
    plt.show()

def button_graph():
    if present_year_entry.get()=='' or insurance_years.get() == '' or entry_amount.get()=='':
        browse_show.configure(text="Please Enter the valid data Amount P year , Till Years", fg='red')
    else:
        total=insurance_analysis()
        total_profit=total[2]
        text0='Your Total Profit After '+insurance_years.get()+' years will be '+str(total_profit)
        browse_show.configure(text=text0, fg='green')
        placing_graph()


r = Tk()
r.geometry('750x550')

# Frame For Entry
f1 = Frame(r,bg='#F2F2F2')



# Search Data
heading_label=Label(f1,text='Bank Insurance Plan',font=("Courier", 16,'bold'))
heading_label.grid(row=0)
search_label = Label(f1, text='SEARCH :',font=("Helvetica", 9))
search_label.grid(row=1, column=0,padx=5,pady=5)

entry_search = Entry(f1,font=("Helvetica",9))
entry_search.grid(row=1, column=1,padx=5,pady=5)

show_btn=Button(f1,text='SEARCH',width=12,command=search,bg='#A0A0A0')
show_btn.grid(row=1,column=2,padx=5,pady=5)


# Name
name_label = Label(f1, text='NAME:',font=("Helvetica", 9))
name_label.grid(row=2, column=0,padx=5,pady=5)

entry_name = Entry(f1)
entry_name.grid(row=2, column=1,padx=20,pady=20)

# Age
age_label = Label(f1, text='AGE:',font=("Helvetica", 9))
age_label.grid(row=3, column=0,padx=5,pady=5)

entry_age = Entry(f1)
entry_age.grid(row=3, column=1)

# CNIC
CNIC_label = Label(f1, text='C.N.I.C',font=("Helvetica", 9))
CNIC_label.grid(row=2, column=2,padx=5,pady=5)

entry_cnic = Entry(f1)
entry_cnic.grid(row=2, column=3,padx=5,pady=5)

# Amount
amount_label = Label(f1, text='AMOUNT $',font=("Helvetica", 9))
amount_label.grid(row=3, column=2,padx=5,pady=5)

entry_amount = Entry(f1)
entry_amount.grid(row=3, column=3,padx=5,pady=5)


# Append Data Buttons
append_btn=Button(f1,text='ENTER',width=12, command=append_data,bg='#A0A0A0')
append_btn.grid(row=4,column=0,padx=5,pady=5)

# Adding Buttons
load_btn=Button(f1,text='LOAD',width=12,command=load_file,bg='#A0A0A0')
load_btn.grid(row=4,column=1,padx=5,pady=5)

# Save File
save_btn=Button(f1,text='SAVE',width=12,command=save_file,bg='#A0A0A0')
save_btn.grid(row=4,column=2,padx=5,pady=5)

# Show File
show_btn=Button(f1,text='SHOW',width=12,command=show,bg='#A0A0A0')
show_btn.grid(row=4,column=3,padx=5,pady=5)

# Insurance Analysis

insurance_Heading=Label(f1,text='Insurance Analysis',font=("Courier", 12),fg='red')
insurance_Heading.grid(row=5,column=0,padx=5,pady=5)

present_year=Label(f1,text='Present Year :')
present_year.grid(row=6,column=0,padx=5,pady=5)

present_year_entry=Entry(f1)
present_year_entry.grid(row=6,column=1,padx=5,pady=5)

insurance_extend_years=Label(f1,text='How Many Years :')
insurance_extend_years.grid(row=6,column=2,padx=5,pady=5)

insurance_years=Entry(f1)
insurance_years.grid(row=6,column=3,padx=5,pady=5)

show_graph=Button(f1,text='Graph Analysis',bg='#90ee90',command=button_graph)
show_graph.grid(row=7,column=2,padx=5,pady=5)

# Frame for Data Display
f2=Frame(r,bg='#F2F2F2')
delete_btn=Button(f2,text='Delect Selected',command=delete_it,bg='#ffcccb')
delete_btn.pack(side='bottom')
browse_show=Label(f2,text="No File Opened" ,fg='red')
browse_show.pack()
# Scroll Bar
scrollbar=Scrollbar(f2,orient=VERTICAL)

data_list=Listbox(f2,height=8,width=90,border=2,yscrollcommand=scrollbar.set,selectmode=EXTENDED,font=("Helvetica", 11))
scrollbar.config(command=data_list.yview)

scrollbar.pack(side=RIGHT,fill=Y)

data_list.pack(padx=20,pady=20)

exit_btn=Button(text='EXIT',bg='#FF4500',command=exit)
exit_btn.pack(side='bottom')



f1.pack(side='top', fill='x')
f2.pack(fill='x')
r.mainloop()
