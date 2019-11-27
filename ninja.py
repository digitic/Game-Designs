class Ninja:
    def __init__(self, x, y, board):
        self.weapon = 1
        self.board = board
        self.x = x
        self.y = y
        self.space = board[x][y]
    #.Get space of character
    def getSpace(self):
        return self.space
    # Get if char has weapon
    def getWeapon(self):
        return self.weapon
    # Get board
    def getBoard(self):
        return self.board
    # Conditional statements to determine if moving a direction is possible. If yes, move.
    def move(self, dir):
        if(dir == "left"):
            if(self.x != 0):
                self.x -= 1
                self.updateSpace(self.x, self.y)
                print("moved left to " + str(self.space) + ".")
            else:
                print("Invalid command.")
        if(dir == "right"):
            if(self.x != 7):
                self.x += 1
                self.updateSpace(self.x, self.y)
                print("moved right to " + str(self.space) + ".")
            else:
                print("Invalid command.")
        if(dir == "up"):
            if(self.y != 0):
                self.y -= 1
                self.updateSpace(self.x, self.y)
                print("moved up to " + str(self.space) + ".")
            else:
                print("Invalid command.")
        if(dir == "down"):
            if(self.y != 7):
                self.y += 1
                self.updateSpace(self.x, self.y)
                print("moved down to " + str(self.space) + ".")
            else:
                print("Invalid command.")
        #STILL NEED DIAGONAL MOVEMENT
    def attack(self):
        if(self.weapon > 0):
            #Determine throw direction
            self.weapon -= 1
        else:
            print("Invalid Command.")
    def updateSpace(self, x, y):
            self.space = self.board[x][y]
    def movePhase(self):
        


def main():
    #Set up 8x8 board, x value, y value.
    #A NOTE: INDICES FOR THIS ARE 0-7, NOT 1-8!
    board = [
    [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)], 
    [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)], 
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
    [(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 
    [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)], 
    [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)], 
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)], 
    [(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]]

    ninja = Ninja(1, 1, board)
    ninja.move("down")
    ninja.move("down")
    ninja.move("down")
    ninja.move("left")
    ninja.move("up")
    ninja.move("up")
    ninja.move("right")





