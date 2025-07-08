import logging
logging.basicConfig(level=logging.DEBUG, filename="logs/demologs.log", filemode="a",
format="%(asctime)s - %(levelname)s : %(message)s")
#filemode = "w" to overwright the file, "a" to append logs in the same file
#dir ..\logs\demologs.log
#datefmt = for example, ‘%Y-%m-%d %H:%M:%S,uuu’

class DemoLogging1:
    def add_numbers(self, a, b):
        return a + b

    def multyply_numbers(self, a, b):
        return a * b

dl = DemoLogging1()
sum_result = dl.add_numbers(3,5)
logging.warning("the sum is: {}".format(sum_result))
logging.error("the sum is: {}".format(sum_result))

multyply_result = dl.multyply_numbers(3,5)
logging.warning("the multiplication is: {}".format(multyply_result))
logging.error("the multiplication is: {}".format(multyply_result))