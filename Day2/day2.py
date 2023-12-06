#!/usr/bin/env python3
'''
Advent of Code: Day 2
'''

# Create a list of games where each game is a list with the structure [ID, red, blue, green]
def parseGame(line: str) -> list[int]:
    red = blue = green = 0
    currentRed = currentBlue = currentGreen = 0
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    line = line.split(":")
    gameNumber = int(line[0].split(" ")[-1].replace("Game", ""))
    rounds = line[1].split(";")
    for round in rounds:
        colors = round.split(",")
        for color in colors:
            if "red" in color:
                currentRed = int(color.replace("red", ""))
            elif "blue" in color:
                currentBlue = int(color.replace("blue", ""))
            elif "green" in color:
                currentGreen = int(color.replace("green", ""))

            if currentRed > red: red = currentRed
            if currentBlue > blue: blue = currentBlue
            if currentGreen > green: green = currentGreen

    return [gameNumber, red, blue, green]


def part1(GAMES: list[list[int]]) -> int:
    badGameTotal = 0
    
    for game in GAMES:
        if game[1] <= 12 and game[2] <= 14 and game [3] <= 13:
            badGameTotal += game[0]

    return badGameTotal

def part2(GAMES: list[list[int]]) -> int:
    runningTotal = 0

    for game in GAMES:
        runningTotal += game[1] * game[2] * game[3]

    return runningTotal


if __name__ == '__main__':
    LINES = []
    GAMES = []

    LINES = open("input.txt").readlines()
    for line in LINES:
        GAMES.append(parseGame(line))

    print("Part 1 Answer: {}".format(part1(GAMES)))
    print("Part 2 Answer: {}".format(part2(GAMES)))
