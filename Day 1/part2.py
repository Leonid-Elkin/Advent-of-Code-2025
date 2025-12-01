class dialClass:
    def __init__(self):
        self.position = 50
        self.zeroCount = 0
    def rightClick(self):
        self.position += 1
        if self.position > 99:
            self.position -= 100
    def leftClick(self):
        self.position -= 1
        if self.position < 0:
            self.position += 100
    def leftRotation(self,amount):
        for _ in range(amount):
            self.turnLeft()
            if self.checkZero():
                self.zeroCount += 1
    def rightRotation(self,amount):
        for _ in range(amount):
            self.turnRight()
            if self.checkZero():
                self.zeroCount += 1

    def checkZero(self):
        return self.position == 0
    
def extractNumber(string):
    numberString = ""
    for char in string:
        if char.isdigit():
            numberString += char
    return int(numberString)
    
def part2():
    count = 0
    fileName = "data.txt"
    dial = dialClass()
    with open(fileName, 'r') as file:
        for line in file:
            parts = line.split()
            code = parts[0]
            number = extractNumber(parts[0])
            if code[0] == "R":
                dial.rightRotation(number)
            elif code[0] == "L":
                dial.leftRotation(number)
    print(dial.zeroCount)
part2()