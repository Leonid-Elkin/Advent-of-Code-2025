class dialClass:
    def __init__(self):
        self.position = 50
    def turnRight(self, amount, mode = 0):
        amount = amount % 100
        self.position += amount
        if self.position > 99:
            self.position -= 100
    def turnLeft(self, amount):
        amount = amount % 100
        self.position -= amount
        if self.position < 0:
            self.position += 100
    def checkZero(self):
        return self.position == 0
    
def extractNumber(string):
    numberString = ""
    for char in string:
        if char.isdigit():
            numberString += char
    return int(numberString)
    
def part1():
    count = 0
    fileName = "data.txt"
    dial = dialClass()
    with open(fileName, 'r') as file:
        for line in file:
            parts = line.split()
            code = parts[0]
            number = extractNumber(parts[0])
            if code[0] == "R":
                dial.turnRight(number)
                if dial.checkZero():
                    count += 1
            elif code[0] == "L":
                dial.turnLeft(number)
                if dial.checkZero():
                    count += 1
    print(count)
part1()