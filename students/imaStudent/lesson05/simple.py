import logging
import logging.handlers
import datetime

# define default formatter 
format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter = logging.Formatter(format)

# define handler for file 
file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".log"
file_handler = logging.FileHandler(file_name)
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

# define handler for console 
console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)          

# define format for server handler
server_format = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
server_formatter = logging.Formatter(server_format)

# define handler for server and set formatter
server_handler = logging.handlers.SysLogHandler(address=("127.0.0.1", 514))
server_handler.setLevel(logging.ERROR)          
server_handler.setFormatter(server_formatter)

# create logger and add handlers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(server_handler)

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)
