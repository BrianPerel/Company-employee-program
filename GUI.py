'''
Author @ Brian Perel
HW7 - GUI Employee Management System
-> Python program that will store information\nabout employees in a company using a dictionary 
'''

import tkinter as tk 
import tkinter.messagebox
import Employee_Management_System
import mysql.connector 

class MyGUI:
    def __init__(self):
        #print(__doc__)
        self.main_window = tk.Tk() # make the GUI window
        self.main_window.geometry('520x345') # width x height
        self.main_window.configure(background='lightgrey')
        self.main_window.title('Company')
        
       
        # create a GUI label (display EMPLOYEE MANAGEMENT SYSTEM) = the header of the GUI app
        self.header = tk.Label(text = 'EMPLOYEE MANAGEMENT SYSTEM', font = 'Times 12 bold', bg='lightgrey')
                
        # GUI button 1
        self.my_button1 = tk.Button(text = 'Look Up Employee', \
                        command = self.look_up_employee, font = 'Courier 10')


        # GUI message displayed in window (Label)
        self.label1 = tk.Label(text = '\tEmployee ID:', font = 'Courier 10', \
                                                               bg='lightgrey')

        # create a StringVar variable to stroe value input into entry box widget 
        self.output_entry_var = tk.StringVar()

        # create an output box (GUI entry)
        self.output_entry = tk.Entry(width = 20, \
                                textvariable = self.output_entry_var) 
        

        # GUI button
        self.my_button2 = tk.Button(text = 'Add Employee', font = 'Courier 10', \
                            command = self.add_employee)

        self.label2 = tk.Label(text = '\tEmployee Name:', font = 'Courier 10', \
                                                               bg='lightgrey')

        # create a StringVar variable to stroe value input into entry box widget 
        self.output_entry_var1 = tk.StringVar()

        self.output_entry1 = tk.Entry(width = 20, \
                            textvariable = self.output_entry_var1)

        
        # GUI button
        self.my_button3 = tk.Button(text = 'Update Employee', \
                                    font = 'Courier 10', \
                                    command = self.update_employee)

        self.label3 = tk.Label(text = '\tEmployee Dept:', font = 'Courier 10', \
                                                       bg='lightgrey')

        self.output_entry_var2 = tk.StringVar()

        self.output_entry2 = tk.Entry(width = 20, \
                                textvariable = self.output_entry_var2)

        
        # GUI button
        self.my_button4 = tk.Button(text = 'Delete Employee', \
                                        font = 'Courier 10', \
                                        command = self.delete_employee)

        self.label4 = tk.Label(text = '\tEmployee Title:', font = 'Courier 10', \
                                                       bg='lightgrey')

        self.output_entry_var3 = tk.StringVar()

        self.output_entry3 = tk.Entry(width = 20, \
                                           textvariable = self.output_entry_var3)


        self.label5 = tk.Label(text = '\tPay Rate:', font = 'Courier 10', \
                                                               bg='lightgrey')

        self.output_entry_var4 = tk.StringVar()

        self.output_entry4 = tk.Entry(width = 20, \
                                    textvariable = self.output_entry_var4)

        self.label6 = tk.Label(text = '\tPhone Number:', font = 'Courier 10', \
                                                               bg='lightgrey')

        self.output_entry_var5 = tk.StringVar()

        self.output_entry5 = tk.Entry(width = 20, \
                                    textvariable = self.output_entry_var5)

        self.cb_var1 = tk.IntVar()
        self.cb_var1.set(0)
        self.cb1 = tk.Checkbutton(text='Part Time Employee', variable=self.cb_var1, \
                                    bg='lightgrey')

        self.cb_var2 = tk.IntVar()
        self.cb_var2.set(0)
        self.cb2 = tk.Checkbutton(text='Full Time Employee', variable=self.cb_var2, \
                                    bg='lightgrey')
        

        #GUI button
        self.reset_button = tk.Button(text='Reset System', font = 'Courier 10', \
                                           command = self.reset_system)
        

        self.quit_button = tk.Button(text='Quit Program', font = 'Courier 10', \
                                          command=self.main_window.destroy)

        self.canvas = tk.Canvas(self.main_window, width=495, height=40, bd=0, \
                                borderwidth=0, bg='lightgrey', highlightthickness=0.5, \
                                highlightbackground='lightgrey')

        self.canvas.create_line(2, 25, 800, 25)

        # make program position and display
        self.header.place(x = 120, y = 0)

        self.my_button1.place(x = 10, y = 65)
        
        # make program position and display 
        self.label1.place(x = 203, y = 67)
        
        self.output_entry.place(x = 380, y = 67)
        
        self.my_button2.place(x = 10, y = 105)
        
        self.label2.place(x = 186, y = 107)
        
        self.output_entry1.place(x = 380, y = 107)
        
        self.my_button3.place(x = 10, y = 145)
        
        self.label3.place(x = 187, y = 147)
        
        self.output_entry2.place(x = 380, y = 147)
        
        self.my_button4.place(x = 10, y = 185)

        self.label4.place(x = 180, y = 187)
        
        self.output_entry3.place(x = 380, y = 187)

        self.label5.place(x = 230, y = 225)
    
        self.output_entry4.place(x = 380, y = 227)
        
        self.label6.place(x = 200, y = 265)
        
        self.output_entry5.place(x = 380, y = 267)
        
        self.cb1.place(x = 240, y = 305)

        self.cb2.place(x = 380, y = 305)
        
        self.reset_button.place(x = 10, y = 225)

        self.quit_button.place(x = 10, y = 265)
    
        self.canvas.place(x = 10, y = 20)
       


# App operations: 

    # create an empty dictionary
    employees = {}


    def look_up_employee(self):
        # Get an employee ID number to look up.
        ID = self.output_entry.get()

        if ID in self.employees:
            message = self.employees.get(ID)
        else:
            message = 'No employee found of this ID'

        tk.messagebox.showinfo('Employee Info', str(message))

        # set all entry widgets to a blank value
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')
        

    def db_add(self, ID, name, dept, title, pay_rate, phone_number, work_type):
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='')
        mycursor = mydb.cursor()
        mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_db')

        mycursor.execute('use employee_db')
        mycursor.execute('CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), dept VARCHAR(30), title VARCHAR(30), pay_rate FLOAT(4,2), phone_number INT, work_type VARCHAR(30))')

        sql = 'INSERT INTO employees (id, name, dept, title, pay_rate, phone_number, work_type) values (%s, %s, %s, %s, %s, %s, %s)'
        val = (ID, name, dept, title, pay_rate, phone_number, work_type)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, 'record inserted')
        
            
    def add_employee(self):
        # get values from entry box widget
        check = True
        message = ''
        work_type = '' 
        
        try:
            ID = self.output_entry.get()
            name = self.output_entry1.get()
            dept = self.output_entry2.get()
            title = self.output_entry3.get()
            pay_rate = self.output_entry4.get()
            phone_number = self.output_entry5.get()
            
            int(ID)
            
            
        except ValueError:
            check = False 
            tk.messagebox.showinfo('Info', 'Error!')

        if self.cb_var1.get() == 1:
            work_type = 'Part time'
        elif self.cb_var2.get() == 1:
            work_type = 'Full time'


        # create instance and send the values 
        new_emp = Employee_Management_System.Employee(name, ID, dept, title, pay_rate, phone_number, work_type)

        if ID not in self.employees and check and len(ID) == 6 and name != '' and dept != '' and title != '' and pay_rate != '' and phone_number != '':
            self.employees[ID] = new_emp
            message = 'The new employee has been added'
        elif check == False:
            message = 'Could not add employee!\nEmployee ID must be digit format'
        elif len(ID) < 6 or len(ID) > 6:
            message = 'Could not add employee!\nEmployee ID must be 6 digits'
        elif name == '' or dept == '' or title == '' or pay_rate == '' or phone_number == '':
            message = 'Could not add employee.\nMissing data!'

        
        elif ID in self.employees:
            message = 'An employee with that ID already exists'

        self.db_add(ID, name, dept, title, pay_rate, phone_number, work_type)
           
        tk.messagebox.showinfo('Info', message)
        
        # set all entry widgets to a blank value
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')
        self.cb_var1.set(0), self.cb_var2.set(0)

    def update_employee(self):
        message = ''
        check = True 
        # get values from entry box widget
        try:
            ID = self.output_entry.get()
            int(ID)

        except ValueError:
            check = False
       
        if ID in self.employees:
            name, dept = self.output_entry1.get(), self.output_entry2.get()
            title, pay_rate = self.output_entry3.get(), self.output_entry4.get()
            phone_number = self.output_entry5.get()

            if self.cb_var1.get() == 1:
                work_type = 'Part time'
            elif self.cb_var2.get() == 1:
                work_type = 'Full time'

            new_emp = Employee_Management_System.Employee(name, ID, dept, \
                                                    title, pay_rate, phone_number, work_type)
            
            self.employees[ID] = new_emp
            
            message = 'The new employee has been updated'

        elif check == False:
            message = 'Error!'
        elif ID not in self.employees:
            message = 'No employee found of this ID'

        tk.messagebox.showinfo('Info', message)

        # set all entry widgets to a blank value
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')
        self.cb_var1.set(0), self.cb_var2.set(0)

        
    def delete_employee(self):
        # get values from entry box widget 
        ID = self.output_entry.get()

        if ID in self.employees:
            del self.employees[ID]
            message = 'Employee information deleted'
        else:
            message = 'The specified ID number was not found'

        tk.messagebox.showinfo('Info', message)
        
        # set all entry widgets to a blank value
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')

    def reset_system(self):
        self.employees = {}

        mydb = mysql.connector.connect(host='localhost', user='root', passwd='')
        mycursor = mydb.cursor()
        try:
            mycursor.execute('DROP DATABASE employee_db')
            tk.messagebox.showinfo('Info', 'System has been reset, database deleted')


        except mysql.connector.Error as err:
            tk.messagebox.showinfo('Info', 'Error, database not found')            

        # set all entry widgets to a blank value        
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')
 
my_gui = MyGUI()
