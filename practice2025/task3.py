import sys
import datetime

class Logger:
    def __init__(self, stream=sys.stderr, time_format="%Y-%m-%d %H:%M:%S"):
        self.stream = stream
        self.time_format = time_format
        
    def log(self, message):
        current_time = datetime.datetime.now().strftime(self.time_format)
        print("[" + current_time + "] " + message, file=self.stream)

log_output = sys.stderr
formatter = "%Y-%m-%d %H:%M:%S"
logger = Logger(log_output, formatter)

logger.log("Logging massage")