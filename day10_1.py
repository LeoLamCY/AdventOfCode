import re
from collections import defaultdict


class Bot():

    def __init__(self, number):
        self.number = number
        self.high = None
        self.high_target = None
        self.low = None
        self.low_target = None
        self.chip1 = None
        self.chip2 = None

    def set_high_low(self, target_high, high, target_low, low):
        if target_high == 'output':
            self.high_target = outputs
        else:
            self.high_target = bots

        if target_low == 'output':
            self.low_target = outputs
        else:
            self.low_target = bots

        self.high = high
        self.low = low

    def get_chip(self, chip):
        if not self.chip1:
            self.chip1 = chip
        elif not self.chip2:
            self.chip2 = chip
        if self.chip1 and self.chip2:
            self.give_chips()

    def give_chips(self):
        if self.high and self.low:
            max_chip = max(self.chip1, self.chip2, key=int)
            min_chip = min(self.chip1, self.chip2, key=int)
            self.high_target[self.high].get_chip(max_chip)
            self.low_target[self.low].get_chip(min_chip)
            if max_chip in ['61', '17'] and min_chip in ['61', '17']:
                print("Answer is", self.number)
            self.chip1, self.chip2 = None, None


class Output():

    def __init__(self, number):
        self.chip = None
        self.number = number

    def get_chip(self, chip):
        self.chip = chip


class keydefaultdict(defaultdict):

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret

bots = keydefaultdict(Bot)
outputs = keydefaultdict(Output)
command_list = []


def parse_line(line):
    exp_1 = r'bot (\d+).* (\w+) (\d+).* (\w+) (\d+)'
    exp_2 = r'value (\d+).* bot (\d+)'
    m = re.match(exp_1, line)
    m2 = re.match(exp_2, line)
    if m:
        bot_num, target_low, low, target_high, high = m.groups()
        bots[bot_num].set_high_low(target_high, high, target_low, low)

    elif m2:
        chip, bot_num = m2.groups()
        command_list.append((bot_num, chip))


def process_commands():
    for command in command_list:
        bots[command[0]].get_chip(command[1])

with open('day10_input.txt', 'r') as input_file:
    for line in input_file:
        parse_line(line)

    process_commands()
