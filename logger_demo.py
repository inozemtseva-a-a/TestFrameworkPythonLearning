import logging

class LoggerDemo:
    def sample_logger(self):
        #create logger
        logger = logging.getLogger(LoggerDemo.__name__) #display the name of the file where the log is coming from and class
        logger.setLevel(logging.DEBUG)
        #create console handler or file handler and set the log level
        ch = logging.StreamHandler()
        fh = logging.FileHandler("demolog.log")
        #create formatter
        formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s : %(message)s")
        formatter1 = logging.Formatter(fmt="%(asctime)s - %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        #add formatter to console or file handler
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)
        #add console handler to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        #application code - log massages
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")

ld = LoggerDemo()
ld.sample_logger()