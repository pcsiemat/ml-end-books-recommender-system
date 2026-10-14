#TEST LOGS
from ml_books_recommender_system.logger.log import logging
#logging.info("Application started.")


#TEST EXCEPTION
from ml_books_recommender_system.exception.exception_handler import AppException
import sys  

try:
    a = 1 / 0
except Exception as e:
    raise AppException(e, sys)
