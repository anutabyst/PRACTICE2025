from datetime import datetime
import sys


class Formatter:
    def __init__(self, fmt="%Y-%m-%d %H:%M:%S"):
        self.fmt = fmt

    def format(self, message):
        time_str = datetime.now().strftime(self.fmt)
        return "[" + time_str + "] " + message

class Handler:
    def __init__(self, where):
        self.where = where  

    def emit(self, message):
        if self.where == sys.stdout or self.where == sys.stderr:
            self.where.write(message + "\n")
        else:
            with open(self.where, "a", encoding="utf-8") as f:  
                f.write(message + "\n")

class Logger:
    def __init__(self, formatter):
        self.formatter = formatter
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def log(self, message):
        formatted_message = self.formatter.format(message)
        for h in self.handlers:
            h.emit(formatted_message)

formatter = Formatter()
logger = Logger(formatter)

stdout_handler = Handler(sys.stdout)
stderr_handler = Handler(sys.stderr)
file_handler = Handler("logfile.txt")

logger.add_handler(stdout_handler)
logger.add_handler(stderr_handler)
logger.add_handler(file_handler)

logger.log("Привіт, це тестове повідомлення!")
logger.log("Ще одне повідомлення")
