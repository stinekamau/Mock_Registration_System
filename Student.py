

from Display import App


info=App.information
'''
This module contains functionality of the student 

'''
class Student:
    reg_id=1000
    def __init__(self):
        self.reg_id=reg_id
        self.name=info.name
        self.age=info.age
        self.email=info.email 
        self.address=info.address
        self.courses=info.courses
        self.advisor=info.advisor
        self.time_eligible=t.run()

        self.reg_id=self.reg_id+1

    def calculate_course_weight(self):
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

        val=time_converter(start, end, '%m/%d/%Y %I:%M %p', prop)
        dater=days[random.randint(1,5)]+' '+val.split(' ')[1]
        return dater

    def random_time(self):
        days=random.randint()

    def create_report(self):
        report=f"""
                                                            ZAYED UNIVERSITY

                                                            Personal information
    ---------------------------------------------------------------------------------------------------------------------------------------------
    |
    |   Student's Name    ------{self.name}--------------                                              Registration  id   -------{self.reg_id}---|
    |
    |   Student's Email   ------{self.email}-------------                                              Student's Address  --------{self.address}--|
    |                                                                                                                                             |
    |   Total course weight: {self.calculate_course_weight()}                                         Faculty Advisor's Name -----{self.advisor}
    |                                                                                                                                             |
    |                                                                                                                                             |
    |   Time Eligible: {self.time_eligible}
    |---------------------------------------------------------------------------------------------------------------------------------------------|


                                                            Course Details
    ==============================================================================================================================================
    |
    |   TIME                                                                                COURSES
    |   {self.timer()}                                                           {self.courses[0][0].rjust(8,' ')}   {self.courses[0][1].rjust(33,' ')}
    |   {self.timer()}                                                           {self.courses[1][0].rjust(8,' ')}   {self.courses[1][1].rjust(33,' ')}
    |   {self.timer()}                                                           {self.courses[2][0].rjust(8,' ')}   {self.courses[2][1].rjust(33,' ')}
    |   {self.timer()}                                                           {self.courses[3][0].rjust(8,' ')}   {self.courses[3][1].rjust(33,' ')}
    |   {self.timer()}                                                           {self.courses[4][0].rjust(8,' ')}   {self.courses[4][1].rjust(33,' ')}
    |
    |
    



        """




        return report



    

    