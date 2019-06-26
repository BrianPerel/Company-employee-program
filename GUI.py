'''
Brian Perel
HW7 - GUI Employee Management System
'''

import tkinter
import tkinter.messagebox
import Employee_Management_System

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() # make the GUI window
        
        self.frame_row1 = tkinter.Frame() # create the top frame = row 1 of GUI
        self.frame_row2 = tkinter.Frame() # create row 2 of GUI
        self.frame_row3 = tkinter.Frame() # create row 3 of GUI
        self.frame_row4 = tkinter.Frame() # create row 4 of GUI
        self.frame_row5 = tkinter.Frame() # create row 5 of GUI
        self.frame_row6 = tkinter.Frame() # create row 6 of GUI

        
        # create a GUI label (display EMPLOYEE MANAGEMENT SYSTEM) = the header of the GUI app
        self.header = tkinter.Label(self.frame_row1, \
                            text = '\tEMPLOYEE MANAGEMENT SYSTEM\t\t')

        ''' row 1 '''
        
        # GUI button 1
        self.my_button1 = tkinter.Button(self.frame_row2, \
                            text = 'Look Up Employee', \
                            command = self.look_up_employee)

        # GUI message displayed in window (Label)
        self.label1 = tkinter.Label(self.frame_row2, \
                            text = '\tEmployee ID:')

        # create a StringVar variable to stroe value input into entry box widget 
        self.output_entry_var = tkinter.StringVar()

        # create an output box (GUI entry)
        self.output_entry = tkinter.Entry(self.frame_row2, width = 15, \
                                          textvariable = self.output_entry_var)


        ''' row 2 '''

        # GUI button
        self.my_button2 = tkinter.Button(self.frame_row3, \
                            text = 'Add Employee', \
                            command = self.add_employee)

        self.label2 = tkinter.Label(self.frame_row3, \
                            text = '\tEmployee Name:')

        # create a StringVar variable to stroe value input into entry box widget 
        self.output_entry_var1 = tkinter.StringVar()

        self.output_entry1 = tkinter.Entry(self.frame_row3, width = 15, \
                                           textvariable = self.output_entry_var1)

        ''' row 3 '''
        
        # GUI button
        self.my_button3 = tkinter.Button(self.frame_row4, \
                            text = 'Update Employee', \
                            command = self.update_employee)

        self.label3 = tkinter.Label(self.frame_row4, \
                            text = '\tEmployee Dept:')

        self.output_entry_var2 = tkinter.StringVar()

        self.output_entry2 = tkinter.Entry(self.frame_row4, width = 15, \
                                           textvariable = self.output_entry_var2)

        ''' row 4 '''

        # GUI button
        self.my_button4 = tkinter.Button(self.frame_row5, \
                            text = 'Delete Employee', \
                            command = self.delete_employee)

        self.label4 = tkinter.Label(self.frame_row5, \
                            text = '\tEmployee Title:')

        self.output_entry_var3 = tkinter.StringVar()

        self.output_entry3 = tkinter.Entry(self.frame_row5, width = 15, \
                                           textvariable = self.output_entry_var3)
        
        ''' row5 '''

        #GUI button
        self.quit_button = tkinter.Button(self.frame_row6,
                                          text='Quit',
                                          command=self.main_window.destroy)

        ''' frame packs '''
      
        # make program position 
        self.frame_row1.pack()

        # make program position 
        self.frame_row2.pack()

        self.frame_row3.pack()

        self.frame_row4.pack()

        self.frame_row5.pack()

        self.frame_row6.pack(side='left')

        ''' row1 '''

        # make program position and display above message 
        self.header.pack(side='top')

        ''' row2 '''

        # make program display button
        self.my_button1.pack(side='left')

        # make program position and display above message 
        self.label1.pack(side='left')

        self.output_entry.pack(side='right')

        ''' row3 '''

        # make program display button
        self.my_button2.pack(side='left')

        self.label2.pack(side='left')

        self.output_entry1.pack(side='right')

        ''' row4 '''
        
        # make program display button
        self.my_button3.pack(side='left')

        self.label3.pack(side='left')

        self.output_entry2.pack(side='right')

        ''' row5 '''

        # make program display button
        self.my_button4.pack(side='left')

        self.label4.pack(side='left')

        self.output_entry3.pack(side='right')

        ''' row6 '''

        # make program display button
        self.quit_button.pack(side='left')
        
        
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


my_gui = MyGUI()
