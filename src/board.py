from enum import Enum

class State:
    @classmethod
    def generateFromTxt(cls, path):
        f = open(path, "r")
        fileStr = f.read()
        [cols, rows] = getDimensionsFromString(fileStr)
        board = Board(cols, rows)
        
        x = 0
        y = 0
        totalBoxes = 0
        boxesInObjective = 0
        for c in fileStr:
            if c == '@' or c == '+':
                player = Player(x, y)
            elif c == '$':
                boxesInObjective += 1
                totalBoxes += 1
            elif c == '\n':
                y = 0
                x += 1
                continue
            board.tiles[x][y] = Tile(c)
            y += 1
            

        if player is None:
            raise InvalidBoardException()
        return cls(player, board, totalBoxes, boxesInObjective)
                

    def __init__(self, player, board, totalBoxes, boxesInObjective):
        self.board = board
        self.player = player
        self.totalBoxes = totalBoxes
        self.boxesInObjective = boxesInObjective

    def __str__(self):
        str = ""
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                str += (self.board.tiles[i][j].__str__())
            str += "\n"
        return str
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.tiles = [ [ Tile(' ') for i in range(cols) ] for j in range(rows) ]


class Tile:
    def __init__(self, char):
        if char == '+':
            self.type = TileType.OBJECTIVE
        elif char == '$':
            self.type = TileType.BOX
        elif char == '*':
            self.type = TileType.BOXINOBJ
        elif char == '#':
            self.type = TileType.WALL
        elif char == '.':
            self.type = TileType.OBJECTIVE
        elif char == '@':
            self.type = TileType.GROUND
        elif char == ' ':
            self.type = TileType.GROUND

    def __str__(self):
        if self.type == TileType.OBJECTIVE:
            return '+'
        elif self.type == TileType.BOX:
            return '$'
        elif self.type == TileType.BOXINOBJ:
            return '*'
        elif self.type == TileType.WALL:
            return '#'
        elif self.type == TileType.OBJECTIVE:
            return '.'
        elif self.type == TileType.GROUND:
            return ' '


class TileType(Enum):
    GROUND = 0
    WALL = 1
    OBJECTIVE = 2
    BOX = 3
    BOXINOBJ = 4

def getDimensionsFromString(string):
    x_curr = 0
    x_max = 0
    y_curr = 1
    for c in string:
        if c == '\n':
            x_max = max(x_curr, x_max)
            x_curr = 0
            y_curr += 1
        else:
            x_curr += 1
    return [x_max, y_curr]
    
class InvalidBoardException(Exception):
    pass