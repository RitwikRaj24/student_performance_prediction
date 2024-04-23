import sys # sys provides various functions and variables that are used 
# to manipulate different parts of the Python runtime environment 
from src.logger import logging

def error_message_detail(error, error_detail:sys): # whenever an error is raised , this function will be called
    _,_,exc_tb = error_detail.exc_info() # the third variable will give all the information regarding 
    # which file the error has occured , on which line number etc. (first two arent required)
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occured in Python script \nName : [{0}]\nLine Number : [{1}]\nError Message : [{2}]".format(file_name,line_number,str(error))

    return error_message

class CustomException(Exception): # custom exception class which is inheriting from Exception 
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # overriding the __init__ method 
        self.error_message = error_message_detail(error_message, error_detail=error_detail) 

    def __str__(self):
        return self.error_message
    
#  Testing

# if __name__ == "__main__": 
#     try : 
#         a = 1/0
#     except Exception as e: 
#         logging.info("Divide by Zero error.")
#         raise CustomException(e, sys)


