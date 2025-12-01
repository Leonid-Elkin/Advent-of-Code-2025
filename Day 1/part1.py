class Dial:
    def __init__(self):
        self.position = 50

    def turnRight(self, amount):
        self.position = (self.position + amount) % 100

    def turnLeft(self, amount):
        self.position = (self.position - amount) % 100

    def isZero(self):
        return self.position == 0


def extractNumber(s):
    return int(''.join(ch for ch in s if ch.isdigit()))


def main():
    zero_hits = 0
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
                zero_hits += 1

    print(zero_hits)


if __name__ == "__main__":
    main()
