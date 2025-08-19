from time import sleep
from random import random



def wait(seconds):
    """
    Wait for at least the specified number of seconds and at most
    20% more than that.
    """
    sleep(seconds + seconds * random() * 0.2)
