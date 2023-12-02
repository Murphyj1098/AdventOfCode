#!/usr/bin/env python3
'''
Advent of Code: Day 1

--- Part 1 ---

The newly-improved calibration document consists of lines of text; each line originally contained
a specific calibration value that the Elves now need to recover. On each line, the calibration value
can be found by combining the first digit and the last digit (in that order) to form a single
two-digit number.

For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these
together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part 2 ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with
letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each
line.

For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these
together produces 281.

What is the sum of all of the calibration values?
'''

import regex as re

def strToDigit(stringIn: str) -> str:
    LUT = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    try:
        return LUT[stringIn]
    except KeyError:
        return None


def part1() -> int:
    runningTotal = 0
    with open('input.txt', 'r') as f:
        for line in f:
            pattern = re.compile("[0-9]")
            lineList = pattern.findall(line, overlapped=True)
            runningTotal += int((lineList[0]+lineList[-1]))
    return runningTotal


def part2() -> int:
    runningTotal = 0
    indexer = 0
    with open('input.txt', 'r') as f:
        for line in f:
            pattern = re.compile("one|two|three|four|five|six|seven|eight|nine|[0-9]")
            lineList = pattern.findall(line, overlapped=True)
            
            firstDigit = lineList[0] if (strToDigit(lineList[0]) is None) else strToDigit(lineList[0])
            lastDigit = lineList[-1] if (strToDigit(lineList[-1]) is None) else strToDigit(lineList[-1])

            runningTotal += int((firstDigit + lastDigit))

    return runningTotal


if __name__ == '__main__':
    print("Part 1 Answer: {}".format(part1()))
    print("Part 2 Answer: {}".format(part2()))