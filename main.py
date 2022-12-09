import re
import unittest


def filereader(f):
    with open(f) as f:
        return f.read().splitlines()


class Day(unittest.TestCase):
    def __init__(self, day, test1, test2):
        super().__init__()
        self.day = day
        self.data = filereader(f'Input/test{day}.txt')
        self.preprocess()
        if test1:
            self.assertEqual(self.part1(), test1)
        if test2:
            self.assertEqual(self.part2(), test2)
        self.data = filereader(f'Input/day{day}.txt')
        self.preprocess()
    def preprocess(self):
        return
    def part1(self):
        return "Unimplemented"

    def part2(self):
        return "Unimplemented"


class Day1(Day):
    def __init__(self):
        super().__init__(1, 24000, 45000)

    def preprocess(self):
        self.elves = []
        elf = (0, 0)
        for line in self.data:
            if line == '':
                self.elves.append(elf)
                elf = (0, 0)
            else:
                elf = (elf[0] + 1, elf[1] + int(line))
        if elf != (0, 0):
            self.elves.append(elf)
        self.elves.sort(reverse=True, key=lambda x: x[1])

    def part1(self):
        return (self.elves[0])[1]

    def part2(self):
        return [sum(tup) for tup in zip(*self.elves[:3])][1]



class Day2(Day):
    def __init__(self):
        super().__init__(2, 15, 12)

    def part1(self):
        scorematrix = {
            'A X': 4, 'A Y': 8, 'A Z': 3,
            'B X': 1, 'B Y': 5, 'B Z': 9,
            'C X': 7, 'C Y': 2, 'C Z': 6}
        return sum(map(lambda x: (scorematrix[x]), self.data))

    def part2(self):
        scorematrix = {
            'A X': 3, 'A Y': 4, 'A Z': 8,
            'B X': 1, 'B Y': 5, 'B Z': 9,
            'C X': 2, 'C Y': 6, 'C Z': 7}
        return sum(map(lambda x: (scorematrix[x]), self.data))


class Day3(Day):
    def __init__(self):
        super().__init__(3, 157, 70)

    def preprocess(self):
        self.prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.count = 0

    def getPrio(self, line):
        return self.prio.index(line) + 1

    def part1(self):
        lines = map(lambda line: ''.join(set(line[:(len(line) // 2)]).intersection(line[(len(line) // 2):])), self.data)
        return sum(map(self.getPrio, lines))

    def part2(self):
        groups = []
        for group in range(len(self.data) // 3):
            groups.append(''.join(set(self.data[3 * group + 0]).intersection(self.data[3 * group + 1]).intersection(
                self.data[3 * group + 2])))
        return sum(map(self.getPrio, groups))


class Day4(Day):
    def __init__(self):
        super().__init__(4, 2, 3)

    def preprocess(self):
        def parselines(line):
            return re.split(r'[,-]', line)

        self.data = list(map(parselines, self.data))

    def part1(self):
        def enclosed(line):
            return (int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3])) or (
                        int(line[2]) <= int(line[0]) and int(line[3]) >= int(line[1]))

        return sum(map(enclosed, self.data))

    def part2(self):
        def overlap(line):
            return int(line[2]) <= int(line[1]) <= int(line[3]) or int(line[1]) >= int(line[3]) >= int(line[0])

        return sum(map(overlap, self.data))


class Day5(Day):
    def __init__(self):
        super().__init__(5, None, None)


day = Day5()
print(day.data)
print(day.part1())
print(day.part2())
