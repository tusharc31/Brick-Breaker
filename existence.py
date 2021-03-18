import position
import random
import time

class existence():
    
    def __init__(self):
        self._still_exists = 1
        self._timeofbirth = time.time()

    def check_existence (self):
        return self._still_exists

    def kill (self):
        self._still_exists = 0
    
    def what_time (self):
        return self._timeofbirth