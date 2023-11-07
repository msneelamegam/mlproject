import sys
import logging

def error_message_detail(error, error_detail:sys):
    '''
    exc_info() gives the complete details of error informations.
    It return 3 values and we fetch only the "exc_tb".
    exc_tb provides which line of the code or which folder/function/file in error is triggered.
    '''    
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name,
     exc_tb.tb_lineno,
     str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

'''
case 1: 
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divided by Zero is not allowed.")
        raise CustomException(e,sys) 
'''