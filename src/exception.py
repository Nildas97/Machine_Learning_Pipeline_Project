# importing libraries
import os
import sys
from src.logger import logging


# defining the error_message_detail function
# error and error_detail as params
def error_message_detail(error, error_detail: sys):

    # ignoring first and second function, focus on exc_tb i.e. execution_tryblock
    # it will start collecting execution from first try block.
    # starts collecting detail execution information
    _, _, exc_tb = error_detail.exc_info()

    # defining file_name variable for execution_tryblock
    # tb_frame = starts executing one by one from try block
    # f_code = points block from where execution and exception starts
    # co_filename = starts executing function inside try and exception
    # by going into each and every file from
    file_name = exc_tb.tb_frame.f_code.co_filename

    # defining error_message variable
    # it will show error message showing
    # python script name from exc_tb
    # line number from tb_frame
    # error message from f_code
    # rest file number will also be mention
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


# defining custom exception class
# Exception as params
class CustomException(Exception):

    # constructor
    def __init__(self, error_message, error_detail: sys):

        # calling super class
        # inheriting __init__
        # calling error message
        super().__init__(error_message)

        # calling error_message for calling error_message_detail
        # calling error_message and error_detail as params
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Division by 0")
        raise CustomException(e, sys)
