'''
Author @ Brian Perel
GUI Employee Management System
-> Python program that will store information\nabout employees in a company using a dictionary.\nUses an employee class to set and get employee attributes. 
'''

import tkinter as tk 
import tkinter.messagebox
import Employee_Management_System
import mysql.connector
import sys as system
import re 
from datetime import * 


class MyGUI:
    def __init__(self):
        ''' create and place main gui window, buttons, labels, entry's, canvas line '''
        print(__doc__)
        self.main_window = tk.Tk() # make the GUI window
        self.main_window.geometry('520x345') # width x height
        self.main_window.configure(background='lightgrey')
        self.main_window.title('Company')
        print(system.copyright)

        # create datetime object and use today() to assign the current date and time values 
        today = datetime.today()
        print('\nToday is: 0', today.day, '/0', today.month, '/', \
              today.year, sep='', end='. ')
        print(today.strftime('%A'), today.strftime('%B'), \
              str(today.day) + 'th,', today.year)
        print('It\'s ', today.strftime('%I'), ':', today.strftime('%M'), today.strftime(' %p'), sep='')
        
        try:
            self.mydb = mysql.connector.connect(
                host='localhost', user='root', passwd='', database='employee_db')

        except mysql.connector.Error as err:
            self.mydb = mysql.connector.connect(
                host='localhost', user='root', passwd='')

        self.mycursor = self.mydb.cursor(buffered=True)
        self.mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_db')
        self.mycursor.execute('use employee_db')
        self.mycursor.execute('CREATE TABLE IF NOT EXISTS employees (id INT, \
                            name VARCHAR(30), dept VARCHAR(30),\
                            title VARCHAR(30), pay_rate FLOAT(10,2), \
                            phone_number INT, \
                            work_type VARCHAR(30))')

        # create a GUI label (display EMPLOYEE MANAGEMENT SYSTEM) = the header of the GUI app
        self.header = tk.Label(text = 'EMPLOYEE MANAGEMENT SYSTEM',
                               font = 'Times 12 bold', bg='lightgrey')
                
        # GUI button 1
        self.my_button1 = tk.Button(text = 'Look Up Employee', \
                        command = self.look_up_employee, font = 'Courier 10')

        # GUI message displayed in window (Label)
        self.label1 = tk.Label(text = '\tEmployee ID:', font = 'Courier 10', \
                                                               bg='lightgrey')

        # create a StringVar variable to store value input into entry box widget 
        self.output_entry_var = tk.StringVar()

        # create an output box (GUI entry)
        self.output_entry = tk.Entry(width = 20, \
                                textvariable = self.output_entry_var) 
        
        # GUI button
        self.my_button2 = tk.Button(text = 'Add New Employee',
                            font = 'Courier 10', \
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

        self.radio_var = tk.IntVar()
        self.radio_var.set(0)
        
        self.rb1 = tk.Radiobutton(text='Part Time Employee', variable=self.radio_var, \
                                    bg='lightgrey', value=1)

        self.rb2 = tk.Radiobutton(text='Full Time Employee', variable=self.radio_var, \
                                    bg='lightgrey', value=2)

        #GUI button
        self.reset_button = tk.Button(text='Reset System', font = 'Courier 10', \
                                           command = self.reset_system)
        
        self.quit_button = tk.Button(text='Quit Program', font = 'Courier 10', command = quit)

        self.canvas = tk.Canvas(self.main_window, width=495, height=40, bd=0, \
                            borderwidth=0, bg='lightgrey', highlightthickness=0.5, \
                            highlightbackground='lightgrey')

        self.canvas.create_line(2, 25, 800, 25)

        self.cb_var1 = tk.IntVar()
        self.cb_var1.set(0)
        self.conn_close = tk.Checkbutton(text='Close MySQL Connection', variable = self.cb_var1, bg='lightgrey')

        if self.cb_var1.get() == 1:
            self.mydb.close()

        # make program position and display
        self.header.place(x = 120, y = 0)
        self.canvas.place(x = 10, y = 20)
        self.my_button1.place(x = 10, y = 65)
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
        self.rb1.place(x = 240, y = 305)
        self.rb2.place(x = 380, y = 305)
        self.reset_button.place(x = 10, y = 225)
        self.quit_button.place(x = 10, y = 300)
        self.conn_close.place(x = 10, y = 265)
       

# App operations: 

    # create the empty dictionary
    employees = {}


    def look_up_employee(self):
        ''' function to look up an employee's info in dictionary,
        by the ID attained from GUI '''
        # Get an employee ID number to look up.
        ID = self.output_entry.get()

        # ternary operator 
        message = self.employees.get(ID) if (ID in self.employees) else 'No employee found of this ID'

        tk.messagebox.showinfo('Employee Info', str(message))

        # set all entry widgets to a blank value
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')

        try:
            sql = "SELECT * FROM employees WHERE id = %s"
            self.mycursor.execute(sql, (ID,))
            display = self.mycursor.fetchall()
            for data in display:
                print(data)
        except mysql.connector.Error as err:
            print(err)
            
    def add_employee(self):
        ''' function to add an employee to dictionary, by info gathered from GUI '''
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


        pattern = bool(re.match('[a-zA-Z]+', name))

        if self.radio_var.get() == 0:
            tk.messagebox.showinfo('Info', 'Error!')
        elif self.radio_var.get() == 1:
            work_type = 'Part time'
        elif self.radio_var.get() == 2:
            work_type = 'Full time'

        # create instance and send the values 
        new_emp = Employee_Management_System.Employee(
                    name, ID, dept, title, pay_rate, phone_number, work_type)

        self.mycursor.execute('CREATE TABLE IF NOT EXISTS employees (id INT, \
                            name VARCHAR(30), dept VARCHAR(30), \
                            title VARCHAR(30), pay_rate FLOAT(4,2), \
                            phone_number INT, work_type VARCHAR(30))')

        
        if ID not in self.employees and check and len(ID) == 6 and name != '' \
           and dept != '' and title != '' and pay_rate != '' \
           and phone_number != '' and work_type != '' and pattern == True:
            self.employees[ID] = new_emp
            message = 'The new employee has been added'
            tk.messagebox.showinfo('Info', message)
            
            sql = 'INSERT INTO employees (id, name, dept, title, \
            pay_rate, phone_number, work_type) values (%s, %s, %s, %s, %s, %s, %s)'
                
            val = (ID, name, dept, title, pay_rate, phone_number, work_type)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, 'record inserted')
    
        elif ID == '' or name == '' or dept == '' or title == '' \
             or pay_rate == '' or phone_number == '' or work_type == '' \
             or check == False or len(ID) < 6 or len(ID) > 6 or pattern == False:
            message = 'Error! Could not add employee.'
        elif ID in self.employees:
            message = 'An employee with that ID already exists'

        
        # set all entry widgets to a blank value
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')
        self.radio_var.set(0)

    def update_employee(self):
        ''' function to update an already existing employee's info
            in dictionary, by attaining info from GUI '''
        message = ''
        check = True 
        # get values from entry box widget
        try:
            ID = self.output_entry.get()
            int(ID)

        except ValueError as err:
            check = False
            
       
        if ID in self.employees:
            name, dept = self.output_entry1.get(), self.output_entry2.get()
            title, pay_rate = self.output_entry3.get(), self.output_entry4.get()
            phone_number = self.output_entry5.get()

            if self.radio_var.get() == 0:
                tk.messagebox.showinfo('Info', 'Error!')
            elif self.radio_var.get() == 1:
                work_type = 'Part time'
            elif self.radio_var.get() == 2:
                work_type = 'Full time'

            new_emp = Employee_Management_System.Employee(name, ID, dept, \
                                    title, pay_rate, phone_number, work_type)
            
            self.employees[ID] = new_emp

            check = 'SELECT * FROM employees WHERE id=%s'
            self.mycursor.execute(check, (ID,))

            sql = 'UPDATE employees SET name=%s, dept=%s, title=%s, pay_rate=%s, phone_number=%s, work_type=%s WHERE id=%s'
            val = (f'{name}', f'{dept}', f'{title}', f'{pay_rate}', f'{phone_number}', f'{work_type}', f'{ID}')
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, 'record(s) updated')
            
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
        self.radio_var.set(0)

        
    def delete_employee(self):
        ''' function to delete an employee from app, by locating it
            by ID in dictionary '''
        # get values from entry box widget 
        ID = self.output_entry.get()

                
        sql = "DELETE FROM employees WHERE id = %s"
        self.mycursor.execute(sql, (ID,))
        self.mydb.commit()
        print(self.mycursor.rowcount, 'record(s) deleted')

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
        ''' function to reset app data, in case company leaves.
            This will delete all data in app and database ''' 
        self.employees = {}
        
        try:
            self.mycursor.execute('DROP TABLE employees')
            tk.messagebox.showinfo('Info', 'System has been reset, table deleted')
        except mysql.connector.Error as err:
            tk.messagebox.showinfo('Info', 'Error, database not found')            

        # set all entry widgets to a blank value        
        self.output_entry_var.set(''), self.output_entry_var1.set('')
        self.output_entry_var2.set(''), self.output_entry_var3.set('')
        self.output_entry_var4.set(''), self.output_entry_var5.set('')
                
my_gui = MyGUI()
