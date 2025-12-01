class Dial:
    def __init__(self):
        self.position = 50

    def turnRight(self, amount):
        self.position = (self.position + amount) % 100

    def turnLeft(self, amount):
        self.position = (self.position - amount) % 100

    def isZero(self):
        return self.position == 0


def extractNumber(string):
    numString = ""
    for char in string:
        if char.isdigit():
            numString += char
    return int(numString)
def main():
    zeroCount = 0
    fileName = "Day 1/data.txt"
    dial = Dial()

    with open(fileName, 'r') as file:
        for line in file:
            code = line.strip()
            steps = extractNumber(code)

            if code.startswith("R"):
                dial.turnRight(steps)
            elif code.startswith("L"):
                dial.turnLeft(steps)

            if dial.isZero():
                zeroCount += 1

    print(zeroCount)


if __name__ == "__main__":
    main()
