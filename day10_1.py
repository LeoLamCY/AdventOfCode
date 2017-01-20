import re
from collections import defaultdict


class Bot():
    def __init__(self):
        self.high = -1
        self.low = -1
        self.chip1 = -1
        self.chip2 = -1
    
    def set_high(self, high):
        self.high = high

    def set_low(self, low):
        self.low = low

    def set_chip1(self, chip1):
        self.chip1 = chip1

    def set_chip2(self, chip2):
        self.chip2 = chip2

bots = defaultdict(Bot)
         
def parse_line(line):
    bots[1].chip1 = "test"
    print(bots[1].chip1)

with open('day10_input.txt', 'r') as input_file:
    for line in input_file:
        parse_line(line)

