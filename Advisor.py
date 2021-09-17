import random 
import csv
'''
Module that contains the functionality of the Advisor
'''
resource="c:\\Users\\user\\Registration_System\\resources\\faculty.csv"
class Advisor:
    
    def __init__(self):
       
        self.resource="resources\\faculty.txt"
        self.advisor=self.get_faculty()
        self.faculty=[]
        


    def get_faculty(self):
        self.faculty=[]
        with open(self.resource,'r') as f:
            cv_reader=csv.reader(f)
            next(cv_reader)
            for line in cv_reader:
                self.faculty.append(line)
        return self.faculty



    def advise_report(self,tutor,student,schedule):
        report=f"""
                                                                    ZAYED UNIVERSITY 

        
        The following report contains the information details for the  Faculty advisor and the students

                                                                INSTRUCTOR'S NAME: {tutor} 

            STUDENT'S NAME                     SCHEDULE                                 ACADEMIC STANDING GPA

        
            {student}                        {schedule}                                     {str(random.randrange(2,4)).zfill(2)}
        
        
        
        
        
        
        
        
        """
        return report
ad=Advisor()



        

        






