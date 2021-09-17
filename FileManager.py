from tkinter import messagebox
from tkinter import ttk 
from tkinter import *
from textloader import files
from Deadline import t
import time
import random
from Advisor import ad
from collections import defaultdict





'''
This module contains functionality of the student 

'''



class App(Tk):
    #Initialize the class variables
    information={}
    course_tally=defaultdict(int)
    students=1
    def __init__(self):
        #Initialize the instance variables
        super().__init__()

        self.title("Zayed University Registration System")
        self.geometry('1080x720')
        self.create_root_frame()
        self.create_root_text()
        self.rowconfigure(1,weight=1)
        self.columnconfigure(1,weight=1)
       
      


    def create_root_frame(self):
        '''
        Generate the main registration  form input that performs validation and event callbacks
        '''
        self.header=Frame(self,bg='grey') #Create a header frame that  will contain the contents of the modules
        #Define the customized handlers
        def name_handler(event):
            '''
            Checks the validity of the name entered to see if it has an empty string, contains integers or
            excessive word characters in which case the exception block is executed and a pop up relayed
            '''
            try:
                if not  self.name.get():
                    raise  ValueError("Empty String")
                    self.name.delete(0,'end')
                if not self.name.get().replace(' ','').isalpha():
                    raise  ValueError(" wrong data type")
                    self.name.delete(0,'end')

                if len(self.name.get())>50:
                    raise ValueError("Excessive character")
                    self.name.delete(0,'end')
            except ValueError as ve:
                val=f"You have {ve} in the name field"
                messagebox.showerror("Validation Error",val)

        def email_handler(event):
            '''
            Checks the validity of the email input by the user to see if it has an empty string and contains
            the @ and . symbol in which case an error is raised in the exception block
            '''
            email=self.email.get()
            try:
                if not email:
                    raise  ValueError("Empty String")
                    self.email.delete(0,'end')
                if not ('@' in email and '.' in email):
                    raise  ValueError(" Wrong Email Format")
                    self.email.delete (0,'end')

                if not email.split('@')[0].isalpha():
                    raise ValueError("Wrong Email Format")
                    self.email.delete(0,'end')
            except ValueError as ve:
                val=f"You have {ve} in the email field"
                messagebox.showerror("Validation Error",val)

        def contact_handler(event):
            '''
            Checks the validity of the contact entered by the user to see if contains an empty string
            or  a wrong data type in which the exception block is triggered and a popup created with
            a warning message
            '''
            contact=self.contact.get()
            try:
                if not contact:
                    raise  ValueError("Empty String")
                    self.contact.delete(0,'end')
                if  contact.isalpha():
                    raise  ValueError("wrong data type")
                    self.contact.delete(0,'end')

            except ValueError as ve:
                val=f"You have {ve} in the contact field"
                messagebox.showerror("Validation Error",val)   

        
           


        

        #Create the header configuration
        self.header.columnconfigure(0,weight=1) #Designates how the header  column 0 frame will expand relative to the expansion  by the user
        self.header.columnconfigure(1,weight=2) #Designates how the header  row  0 frame will expand relative to the expansion  by the user

        #Create the Label handlers
        self.targeter=StringVar(self.header)
        self.target=ttk.Label(self.header,textvariable=self.targeter,width=60,font=('Arial',10),foreground='green')
        self.target.grid(row=1,column=1)

        self.name_label=ttk.Label(self.header,text="Name:")
        self.name_label.grid(row=2,column=0,sticky=W)

        self.email_label=ttk.Label(self.header,text="Email:")
        self.email_label.grid(row=3,column=0,sticky=W)

        self.contact_label=ttk.Label(self.header,text="Contact")
        self.contact_label.grid(row=4,column=0,sticky=W)

     
        self.gender_label=ttk.Label(self.header,text="Gender")
        self.gender_label.grid(row=5,column=0,sticky=W)

        self.religion_label=ttk.Label(self.header,text="Religion: ")
        self.religion_label.grid(row=7,column=0,sticky=W)

        self.age_label=ttk.Label(self.header,text="Age:")


        self.religions=[' ','Islam','Christiniaty','Buddhism','Judaism','Hinduism'] # The religion options
        self.current_religion=StringVar(self.header) #Create a string variable that contains the religion selected
        self.current_religion.set(self.religions[0])
        self.religion_options=OptionMenu(self.header,self.current_religion,*self.religions) #Create an option menu for choosing the types of relgion
        self.religion_options.config(width=90,font=('Arial',10))
        self.religion_options.grid(row=7,column=1,sticky=W) 


        #Create a label for the advisor
        self.advisor_name=StringVar(self.header,value='') #String variable that automatilly updates the name of the advisor
        self.advisor_label=ttk.Label(self.header,textvariable=self.advisor_name,width=20)
        self.advisor_label.grid(row=14,column=1,pady=10)
        def get_advisor():
            '''
            Call the underlying  textloader module to  randomly assign a faculty advisor
            '''
            name=files.get_single_advisor()
            self.advisor_name.set(name)
            App.information['advisor']=name
        

       

        #create the entry widgets
        self.name=ttk.Entry(self.header)
        self.name.grid(row=2,column=1,sticky=NSEW,pady=10)
        self.name.bind('<Tab>',name_handler) #Bind the name_handler that checks  the correctness of the name entry when the tab key is pressed

        self.email=ttk.Entry(self.header)
        self.email.grid(row=3,column=1,sticky=NSEW,pady=10)
        self.email.bind('<Tab>',email_handler) #Bind the email_handler that checks the correctness of the  email input when Tab is pressed

        self.contact=ttk.Entry(self.header)
        self.contact.grid(row=4,column=1,sticky=NSEW,pady=10)
        self.contact.bind('<Tab>',contact_handler) #Bind the contact handler to the event when Tab is pressed

        #create radio buttons for gender
        self.gender=StringVar(self.header) #Create a string variable to hold the gender 
        ttk.Radiobutton(self.header,text="Male",variable=self.gender,value='Male').grid(row=5,column=1,padx=10,pady=10)
        ttk.Radiobutton(self.header,text="Female",variable=self.gender,value='Female').grid(row=5,column=2,padx=10,pady=10)

        #create radio buttons for marital status
        self.marital_status=StringVar(self.header) #Create a string variable to hold the content 
        self.marital_label=ttk.Label(self.header,text="Marital Status")
        self.marital_label.grid(row=12,column=0,sticky=W,pady=10)
        ttk.Radiobutton(self.header,text="Married",variable=self.marital_status,value=1).grid(row=12,column=1,pady=10)
        ttk.Radiobutton(self.header,text="Single",variable=self.marital_status,value=2).grid(row=12,column=2,pady=10)

        def submiter():
            '''
            Callback functions that  relays the content of the form
            '''
            App.information['gender']=self.gender.get()
            App.information['marital_status']=self.marital_status.get()
            App.information['religion']=self.current_religion.get()
            App.information['name']=self.name.get()
            App.information['email']=self.email.get()
            App.information['contact']=self.contact.get()
            # App.course_tally['']
            
            # print(App.information)

            self.targeter.set("You have successfully completed the form")
        #Create a submit button for all the tasks
        self.submit=ttk.Button(self.header,text='Submit',command=submiter) #This remits all the contents of the form to underlying dictionary
        self.submit.grid(row=18,column=0,pady=20)

        def resetter():
            '''
            Callback function called to clear all the entry box, radiobutton and albels
            '''
            self.gender.set('')
            self.marital_status.set('')
            self.current_religion.set('')
            self.name.delete(0,'end')
            self.email.delete(0,'end')
            self.contact.delete(0,'end')
            self.advisor_label.config(text='')
            App.information.clear()
        
        
        #Create a reset button 
        self.reset=ttk.Button(self.header,text='reset',command=resetter) #This buttons clears the student's form content
        self.reset.grid(row=18,column=1,pady=20,padx=20) #Position the button 
        
        
        self.advisor=ttk.Button(self.header,text="Get Advisor",command=get_advisor) #Automatically generates a faculty advisor for the student
        self.advisor.grid(row=14,column=0,pady=10)

        def generate_courses():
            '''
            Automatically generates courses for the students  and performs checks to see whether the courses are full
            in which case they offer the warning. 
            '''
            a_course=files.advise_courses()
            App.information['courses']=a_course #Update the class variable
            self.targeter.set("Successfully generated courses") 
            for item in a_course:
                try:
                    App.course_tally[item[1]]+=1
                    if item[3]=='Theory' and App.course_tally[item[1]]>50: #check the course category and the number of students
                        raise ValueError("The number of students for the  theory  course have exceeded")
                    if item[3]=='Lab' and App.course_tally[item[1]]>24:
                        raise ValueError("THe number of students for the lab have exceeded 24 ")

                except ValueError as ve:
                    messagebox.showerror("Full Course!",ve) #Creuate a pop window showing the error message


                    



        #Create the generate course button
        self.courses=ttk.Button(self.header,text='Generate Courses',command=generate_courses)
        self.courses.grid(row=17,column=0,pady=10)

        self.header.grid(column=0, row=0,sticky=NSEW)

       

    def create_root_text(self):
        '''
        Create a bottom frame  that contains three buttons responsible for the report generation.
        '''
        self.frame=Frame(self,bg='grey')
        self.intro_label=ttk.Label(self.frame,text="Select the report you want to generate")
        self.intro_label.grid(row=0,column=0,pady=20)

        def student_report_callback():
            '''
            Generates a top level window containing the student report
            '''
            student=Student() #instantiate the student object
            s_window=Toplevel(self) #create a top window
            s_window.title("Student Report generation")
            s_window.state('zoomed') #Make the window maximized

            displayer=Text(s_window,height=200,width=200) #Create an entry widget to display the message
            displayer.pack()
            report=student.create_report() #Generate the report
            print(f'The value of the report is {type(report)}')
            displayer.insert('1.0',report) #Display the report

        def advisor_report_callback():
            '''
            Generate a top level widnow containing the Advisor report
            '''
            s=Student() #Instantiate the student object
            s_window=Toplevel(self)
            s_window.title("Advisor Report generation")
            s_window.state('zoomed')

            displayer=Text(s_window,height=200,width=200) #Create the entry widget
            displayer.pack()
            report=ad.advise_report(App.information['advisor'],App.information['name'],s.timer()) #Generate report from the advisor module
            displayer.insert('1.0',report)

        def course_report_callback():
            '''
            Generates the report about the course
            '''
            s=Student() #Instantiate the student object
            s_window=Toplevel(self)
            s_window.title("Course Report generation")
            s_window.state('zoomed')
            

            displayer=Text(s_window,height=200,width=200)
            displayer.pack()
            report=files.course_report(App.information['name'],App.information['advisor'],App.course_tally) #Generate a report from the File Manager module
            displayer.insert('1.0',report)
            



        self.student_report=ttk.Button(self.frame,text='Student',command=student_report_callback) #Create button to create student report
        self.student_report.grid(row=2,column=0,padx=20)
        self.course_report=ttk.Button(self.frame,text='Course',command=course_report_callback) #Generate button to create course_report
        self.course_report.grid(row=2,column=1,padx=20)
        self.adviser_report=ttk.Button(self.frame,text='Advisor',command=advisor_report_callback) #Generate button to create advisor report
        self.adviser_report.grid(row=2,column=2,padx=20)

        

        self.frame.grid(row=1,column=0,sticky=W)
class Student:
    '''
    Class that contains the student logic and helper function that helps to maintain cohesion
    '''
    reg_id=1000
    
    def __init__(self):
        #Perform  initialization
        self.reg_id=Student.reg_id
        self.name=App.information['name']
        self.age=random.randint(18,24)
        self.email=App.information['email']
        self.address=App.information['contact']
        self.courses=App.information['courses']
        self.advisor=App.information['advisor']
        self.time_eligible=t.run()

        Student.reg_id+=1

    def calculate_course_weight(self):
        '''
        Calculate the course weight associated with each of the course for a single student and perform summation
        '''
        weight=0
        for item in self.courses:
            weight+=int(item[2])
        return weight




    def timer(self):

        def random_date(start, end, prop):
                def time_converter(start, end, format, prop):
                
                    stime = time.mktime(time.strptime(start, format))
                    etime = time.mktime(time.strptime(end, format))

                    ptime = stime + prop * (etime - stime)

                    return time.strftime(format, time.localtime(ptime))
                days={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday'}
    
                val=time_converter(start, end, '%m/%d/%Y %I:%M %p', prop)
                dater=days[random.randint(1,5)]+' '+val.split(' ')[1]
                return dater
        return random_date("1/1/2021 1:30 PM", "4/30/2021 4:50 AM", random.random())




    def random_date(self,start, end, prop):

        def time_converter(start, end, format, prop):
        
            stime = time.mktime(time.strptime(start, format))
            etime = time.mktime(time.strptime(end, format))

            ptime = stime + prop * (etime - stime)

            return time.strftime(format, time.localtime(ptime))
        days={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday'}
        val=time_converter(start, end, '%m/%d/%Y %I:%M %p', prop)
        dater=days[random.randint(1,5)]+' '+val.split(' ')[1]
        return dater

    def random_time(self):
        days=random.randint()

    def create_report(self):
        '''
        Generates report for the student 
        '''
        report=f"""
                                                            ZAYED UNIVERSITY

                                                            Personal information
    ---------------------------------------------------------------------------------------------------------------------------------------------
    |
    |   Student's Name:   ------{self.name}--------------                                              Registration  id:     {self.reg_id}       |
    |
    |   Student's Email:     {self.email}                                                              Student's Address:    {self.address}      |
    |                                                                                                                                             |
    |   Total course weight: {self.calculate_course_weight()}                                          
    |       
    |   Faculty Advisor's Name: {self.advisor}                                                                                                                                      |
    |                                                                                                                                             |
    |   Time Eligible: {self.time_eligible}
    |---------------------------------------------------------------------------------------------------------------------------------------------|


                                                            Course Details
    ==============================================================================================================================================
    |
    |   TIME                                                                                  COURSES
                                                                                
    |   {self.timer()}                                                           {self.courses[0][0].strip()}   {self.courses[0][1]}
    |   {self.timer()}                                                           {self.courses[1][0].strip()}   {self.courses[1][1]}
    |   {self.timer()}                                                           {self.courses[2][0].strip()}   {self.courses[2][1]}
    |   {self.timer()}                                                           {self.courses[3][0].strip()}   {self.courses[3][1]}
    |   {self.timer()}                                                           {self.courses[4][0].strip()}   {self.courses[4][1]}
    |
    |




        """




        return report


   
if __name__=="__main__":
    app=App()
    app.mainloop()

        


