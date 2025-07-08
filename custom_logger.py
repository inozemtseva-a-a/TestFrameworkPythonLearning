import inspect
import logging

class customLogger:
    def custom_logger(self,log_level=logging.DEBUG):
        #Set class/method name from where it's called
        logger_name = inspect.stack()[1][3]
        #create logger
        logger = logging.getLogger(logger_name) #display the name of the file where the log is coming from and class
        logger.setLevel(log_level)
        #create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")
        #create formatter
        formatter1 = logging.Formatter(fmt="%(asctime)s - %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        #add formatter to console or file handler
        fh.setFormatter(formatter1)
        #add console handler to logger
        logger.addHandler(fh)
        return logger
