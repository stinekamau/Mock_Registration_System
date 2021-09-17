'''
Module that provides a higher abstraction over the text file that make up the
data
'''
import csv
import random
class FileManager:
    def __init__(self):
        self.resource="resources\\faculty.txt" #Path to the Advisors data types
        self.courses_resource="resources\\final_courses.txt" #Path to the courses
        self.courses=[]
        self.faculty=[]

    def get_courses(self):
        '''
        Returns
        a list of list containing the individual contents of  the courses
        '''
        with open(self.courses_resource,'r') as f:
            csv_reader=csv.reader(f)
            next(csv_reader)
            for line in csv_reader:
                self.courses.append(line)
        return self.courses

    def advise_courses(self):
        '''
        Calls the get_courses first and subsequently  samples the courses that will be offered
        to the student
        '''
        courses=self.get_courses()
        rander=[random.randint(0,98) for i in range(5)]
        return [courses[i] for i in rander]
        

    def get_single_advisor(self):
        '''
        Returns the name of a single Faculty advisor
        '''
        courses=self.get_faculty()
        num=random.randint(0,98)
        return courses[num][0].replace('Â','').strip() #Stips away the unncessary characters

    def get_faculty(self):
        '''
        Provides functionality for  loadign the  faculty text file  and returning it as a list
        '''
        resource_name="resources\\faculty.csv"
        with open(self.resource,'r') as f:
            cv_reader=csv.reader(f)
            next(cv_reader)
            for line in cv_reader:
                self.faculty.append(line)
        return self.faculty

    def course_report(self,student,tutor,courses):
        '''
        Generates a report about the courses 
        '''
    
        c=list(courses.keys())
      
        report=f"""
        
        COURSES                                          NUMBER OF STUDENTS                            
        
        {c[0].rjust(30,' ')}                                                {courses[c[0]]}                               
        {c[1].rjust(30,' ')}                                                {courses[c[1]]}
        {c[2].rjust(30,' ')}                                                {courses[c[2]]}
        {c[3].rjust(30,' ')}                                                {courses[c[3]]}
       

        FACULTY ASSIGNED: {tutor}


        """
        return report

    


files=FileManager()


