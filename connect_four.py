import random

print("🎮 Welcome to Connect Four!")
print("----------------------------")

# Board setup
possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]

rows = 6
cols = 7

def printGameBoard():
    """Prints the game board with column letters and row numbers."""
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print("   ", end=" |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
    """Places a chip on the board."""
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
    """Checks board for a winner."""
    # Horizontal
    for x in range(rows):
        for y in range(cols - 3):
            if (gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and
                gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip):
                print(f"\n🏆 Game over! {chip} wins! 🎉")
                return True

    # Vertical
    for y in range(cols):
        for x in range(rows - 3):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and
                gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip):
                print(f"\n🏆 Game over! {chip} wins! 🎉")
                return True

    # Diagonal (top-left to bottom-right)
    for x in range(rows - 3):
        for y in range(cols - 3):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and
                gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip):
                print(f"\n🏆 Game over! {chip} wins! 🎉")
                return True

    # Diagonal (top-right to bottom-left)
    for x in range(rows - 3):
        for y in range(3, cols):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and
                gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip):
                print(f"\n🏆 Game over! {chip} wins! 🎉")
                return True

    return False

def coordinateParser(inputString):
    """Converts user input like 'A0' into board coordinates."""
    inputString = inputString.upper()
    coordinate = [None, None]

    if inputString[0] in possibleLetters:
        coordinate[1] = possibleLetters.index(inputString[0])
    else:
        print("❌ Invalid column letter.")
        return None

    try:
        coordinate[0] = int(inputString[1])
    except:
        print("❌ Invalid row number.")
        return None

    if coordinate[0] < 0 or coordinate[0] >= rows:
        print("❌ Row out of range.")
        return None

    return coordinate

def isSpaceAvailable(coord):
    """Checks if a spot is free."""
    return gameBoard[coord[0]][coord[1]] not in ['🔵', '🔴']

def gravityChecker(coord):
    """Ensures tokens fall to the lowest available row in a column."""
    spaceBelow = [coord[0] + 1, coord[1]]
    if spaceBelow[0] == rows:  # bottom row
        return True
    if not isSpaceAvailable(spaceBelow):  # something below
        return True
    return False

# Game loop
leaveLoop = False
turnCounter = 0

while not leaveLoop:
    if turnCounter % 2 == 0:  # Player's turn
        printGameBoard()
        while True:
            move = input("\n🔵 Your move (e.g., A0): ").strip()
            coord = coordinateParser(move)
            if coord and isSpaceAvailable(coord) and gravityChecker(coord):
                modifyArray(coord, '🔵')
                break
            else:
                print("❌ Invalid move. Try again.")
        winner = checkForWinner('🔵')
        turnCounter += 1
    else:  # CPU's turn
        while True:
            cpuChoice = random.choice(possibleLetters) + str(random.randint(0, 5))
            coord = coordinateParser(cpuChoice)
            if coord and isSpaceAvailable(coord) and gravityChecker(coord):
                modifyArray(coord, '🔴')
                print(f"\n🤖 CPU played: {cpuChoice}")
                break
        winner = checkForWinner('🔴')
        turnCounter += 1

    if winner:
        printGameBoard()
        leaveLoop = True
