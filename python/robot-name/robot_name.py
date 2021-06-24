import random
import string

class Robot:
    def __init__(self):
        self.name = Robot._generate_new_name()
        
    def reset(self):
        self.name = Robot._generate_new_name()
        
    @staticmethod
    def _generate_new_name():
        return f"{RandomGenerator.get_random_letters(2)}{RandomGenerator.get_random_numbers(3)}"


class RandomGenerator:
    @staticmethod
    def randomize_seed():
        random.seed()

    @staticmethod
    def get_random_letters(number_of_letters):
        RandomGenerator.randomize_seed()
        return "".join(random.choice(string.ascii_uppercase) for i in range(number_of_letters))
    
    @staticmethod
    def get_random_numbers(number_of_numbers):
        RandomGenerator.randomize_seed()
        return "".join(str(random.randint(0,9)) for i in range(number_of_numbers))

    
