import numpy as np

class display:

    def __init__(self):
        # self.refresh_rate = 0.1
        self.display_height = 35
        self.display_length = 120
        self.display = [['*']*self.display_length]*self.display_height
        self.display = np.array(self.display)

refresh_rate = 0.05