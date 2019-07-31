
'''
Brian Perel
HW7 - GUI Employee Management System
'''

import tkinter as tk 
import tkinter.messagebox
import Employee_Management_System

class MyGUI1:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry('320x100') # width x height
        self.main_window.title('Company X')
        self.frame_row1 = tk.Frame()
        self.frame_row2 = tk.Frame()

        self.header = tk.Label(self.frame_row1, \
                            text = 'Enter your companies name:', font = ('Times 12'))
       

        # create variable to store company name 
        self.output_entry_companyVar = tk.StringVar()

        # prompt for company name, then store that into output_entry1
        self.output_entry1 = tk.Entry(self.frame_row2, width = 20, \
                            textvariable = self.output_entry_companyVar)

        self.my_button1 = tk.Button(self.frame_row2, \
                            text = 'Submit', \
                            font = ('Courier 10'), command = self.main_window.destroy)

        self.frame_row1.pack()
        self.frame_row2.pack()
        self.header.pack()
        self.my_button1.pack(side='left')
        self.output_entry1.pack(side='left')

        tkinter.mainloop()
        
        

class MyGUI2:
    def __init__(self):
        self.main_window = tk.Tk() # make the GUI window
        self.main_window.geometry('520x260') # width x height
        self.main_window.configure(background='lightgrey')


        #message = company_name.output_entry1.get()
        #self.main_window.title(message)

        
       
        # create a GUI label (display EMPLOYEE MANAGEMENT SYSTEM) = the header of the GUI app
        self.header = tk.Label(text = 'EMPLOYEE MANAGEMENT SYSTEM', font = ('Times 12'), bg='lightgrey')
                
        # GUI button 1
        self.my_button1 = tk.Button(text = 'Look Up Employee', \
                            command = self.look_up_employee, font = ('Courier 10'))
        

        # GUI message displayed in window (Label)
        self.label1 = tk.Label(text = '\tEmployee ID:', font = ('Courier 10'), bg='lightgrey')

        # create a StringVar variable to stroe value input into entry box widget 
        self.output_entry_var = tk.StringVar()

        # create an output box (GUI entry)
        self.output_entry = tk.Entry(width = 20, \
                            textvariable = self.output_entry_var) 


        

        # GUI button
        self.my_button2 = tk.Button(text = 'Add Employee', font = ('Courier 10'), \
                            command = self.add_employee)

        self.label2 = tk.Label(text = '\tEmployee Name:', font = ('Courier 10'), bg='lightgrey')

        # create a StringVar variable to stroe value input into entry box widget 
        self.output_entry_var1 = tk.StringVar()

        self.output_entry1 = tk.Entry(width = 20, \
                            textvariable = self.output_entry_var1)

        
        
        # GUI button
        self.my_button3 = tk.Button(text = 'Update Employee', font = ('Courier 10'), \
                            command = self.update_employee)

        self.label3 = tk.Label(text = '\tEmployee Dept:', font = ('Courier 10'), bg='lightgrey')

        self.output_entry_var2 = tk.StringVar()

        self.output_entry2 = tk.Entry(width = 20, \
                            textvariable = self.output_entry_var2)

       
        
        # GUI button
        self.my_button4 = tk.Button(text = 'Delete Employee', font = ('Courier 10'), \
                            command = self.delete_employee)

        self.label4 = tk.Label(text = '\tEmployee Title:', font = ('Courier 10'), bg='lightgrey')

        self.output_entry_var3 = tk.StringVar()

        self.output_entry3 = tk.Entry(width = 20, \
                                           textvariable = self.output_entry_var3)
        

        #GUI button
        self.quit_button = tk.Button(text='Quit', font = ('Courier 10'), \
                                          command=self.main_window.destroy)

        self.reset_button = tk.Button(text='Reset', font = ('Courier 10'), \
                                           command = self.reset_system)


        

        ''' row1 '''

        # make program position and display above message 
        self.header.place(x = 130, y = 0)

        ''' row2 '''

        # make program display button
        self.my_button1.place(x = 10, y = 40)

        # make program position and display above message 
        self.label1.place(x = 203, y = 40)

        self.output_entry.place(x = 380, y = 40)

        ''' row3 '''

        # make program display button
        self.my_button2.place(x = 10, y = 80)


        self.label2.place(x = 186, y = 80)

        self.output_entry1.place(x = 380, y = 80)

        ''' row4 '''
        
        # make program display button
        self.my_button3.place(x = 10, y = 120)

        self.label3.place(x = 187, y = 120)

        self.output_entry2.place(x = 380, y = 120)

        ''' row5 '''

        # make program display button
        self.my_button4.place(x = 10, y = 160)

        self.label4.place(x = 180, y = 160)

        self.output_entry3.place(x = 380, y = 160)

        # display button 
        self.reset_button.place(x = 10, y = 200)

        # make program display button
        self.quit_button.place(x = 80, y = 200)

        # tkinter calls OS to get visual graphics 
        tkinter.mainloop()

    # create an empty dictionary
    employees = {}

    def look_up_employee(self):
        # Get an employee ID number to look up.
        # ID = input('Enter an employee ID number: ')
        ID = self.output_entry.get()

        if ID in self.employees:
            message = self.employees.get(ID)
        else:
            message = 'No employee found of this ID'
            
        
        
        # print(employees.get(ID, "The specified ID number was not found"))
        tkinter.messagebox.showinfo('Info', str(message))

        self.output_entry_var.set('')
        

    def add_employee(self):
        # get values from entry box widget 
        ID = self.output_entry.get()
        name = self.output_entry1.get()
        dept = self.output_entry2.get()
        title = self.output_entry3.get()

        # create instance and send the values 
        new_emp = Employee_Management_System.Employee(name, ID, dept, title)

        if ID not in self.employees:
            self.employees[ID] = new_emp
            message = 'The new employee has been added'
        else:
            message = 'An employee with that ID already exists'
           

        tkinter.messagebox.showinfo('Info', message)
        
        # set all entry widgets to a blank value 
        self.output_entry_var.set('')
        self.output_entry_var1.set('')
        self.output_entry_var2.set('')
        self.output_entry_var3.set('')

    def update_employee(self):
        # get values from entry box widget 
        ID = self.output_entry.get()
       
        if ID in self.employees:
            name = self.output_entry1.get()
            dept = self.output_entry2.get()
            title = self.output_entry3.get()

            new_emp = Employee_Management_System.Employee(name, ID, dept, title)
            self.employees[ID] = new_emp
            
            message = 'The new employee has been updated'
        else:
            message = 'No employee found of this ID'

        tkinter.messagebox.showinfo('Info', message)

        self.output_entry_var.set('')
        self.output_entry_var1.set('')
        self.output_entry_var2.set('')
        self.output_entry_var3.set('')
        
    def delete_employee(self):
        # get values from entry box widget 
        ID = self.output_entry.get()

        if ID in self.employees:
            del self.employees[ID]
            message = 'Employee information deleted'
        else:
            message = 'The specified ID number was not found'

        tkinter.messagebox.showinfo('Info', message)

        self.output_entry_var.set('')
        self.output_entry_var1.set('')
        self.output_entry_var2.set('')
        self.output_entry_var3.set('')

    def reset_system(self):
        self.employees = {}

        message = 'System has been reset'
        tkinter.messagebox.showinfo('Info', message)

        # set all entry widgets to a blank value 
        self.output_entry_var.set('')
        self.output_entry_var1.set('')
        self.output_entry_var2.set('')
        self.output_entry_var3.set('')

        
        
#company_name = MyGUI1()
my_gui = MyGUI2()
