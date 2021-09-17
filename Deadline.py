'''
Module required to measure the total  Registration period 
'''

import time

class student_timer:
    def __init__(self,count=70):
        self.count=count #Generate the instance variable
    def run(self):
       
        min,sec=divmod(self.count,60)
        f_time=f'{str(min).zfill(2)}:{str(sec).zfill(2)}' #Format the time
        self.count-=1
      
        return f_time
    
t=student_timer() #instantiate the class

