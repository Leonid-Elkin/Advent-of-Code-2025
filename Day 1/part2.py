class dialClass:
    def __init__(self):
        self.position = 50
        self.zeroCount = 0
    def rightRotation(self, amount):
        old = self.position
        amount = int(amount)
        passes = (old + amount) // 100
        self.position = (old + amount) % 100
        self.zeroCount += passes
    def leftRotation(self, amount):
        old = self.position
        amount = int(amount)
        if old == 0:
            passes = amount // 100
        else:
            if amount >= old:
                passes = ((amount - old) // 100 + 1)
            else:
                passes = 0
        self.position = (old - amount) % 100
        self.zeroCount += passes
    def checkZero(self):
        return self.position == 0

def extractNumber(string):
    numString = ""
    for char in string:
        if char.isdigit():
            numString += char
    return int(numString)

def main():
    fileName = "Day 1/data.txt"
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

if __name__ == "__main__":
    main()
