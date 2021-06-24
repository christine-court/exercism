import random
import string

class Robot:
    def __init__(self):
        self.name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        
    def reset(self):
        self._randomize_seed()
        self.name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

    @staticmethod
    def _randomize_seed():
        random.seed()


    
