from random import randint,choice
class Board:
    _board = [" "]*9
    _order = ["x","o"]
    _turn = 0
    players = []
    def palyer1ltr(self,ltr):
        if ltr == "x":
            self._order = ["x","o"]
        else:
            self._order = ["o","x"]
    def __repr__(self):
        return f"{self._board[0]} {self._board[1]} {self._board[2]}\n{self._board[3]} {self._board[4]} {self._board[5]}\n{self._board[6]} {self._board[7]} {self._board[8]}"
    def choseStart(self):
        self._turn = randint(0,1)
        
    def checkWin(self):
        lines = [
            [self._board[0],self._board[1],self._board[2]],
            [self._board[3],self._board[4],self._board[5]],
            [self._board[6],self._board[7],self._board[8]],

            [self._board[0],self._board[3],self._board[6]],
            [self._board[1],self._board[4],self._board[7]],
            [self._board[2],self._board[5],self._board[8]],
            [self._board[0],self._board[4],self._board[8]],
            [self._board[2],self._board[4],self._board[6]],
        ]
        winLine = [self._order[self._turn]]*3
        return winLine in lines
    def playTurn(self):
        self.players[self._turn](self)
        r = self.checkWin()
        self._turn = 0 if self._turn == 1 else 1
        return r
    def play(self):
        result = False
        while (not result) and (self.posible() != []):
            result = self.playTurn()
        return ~self._turn if result else False
    def posible(self):
        r = []
        for i in range(len(self._board)):
            if self._board[i] == " ":
                r += [i]
        return r
    
    def move(self,num):
        if num in self.posible():
            self._board[num] = self._order[self._turn]
    def copy(self):
        b = Board()
        b._board = [i for i in self._board]
        b._turn = self._turn
        return b

def human(board:Board):
    print("0 1 2\n3 4 5\n6 7 8\n")
    print(board)
    moves = board.posible()
    move = -1
    while not (move in moves):
        move = int(input("Move: "))
    board.move(move)
def bogo(board:Board):
    board.move(choice(board.posible()))
def machine(board:Board):
    posible = board.posible()
    
    for i in posible:
        boardCopy = board.copy()
        boardCopy.move(i)
        if boardCopy.checkWin():
            board.move(i)
            return
    
    for i in posible:
        boardCopy = board.copy()
        boardCopy._turn = ~boardCopy._turn
        boardCopy.move(i)
        if boardCopy.checkWin():
            board.move(i)
            return
    
    corners = [i for i in [0,2,6,8] if i in posible]
    if corners != []:
        board.move(choice(corners))
        return
    
    if 4 in posible:
        board.move(i)
        return
    
    bogo(board)
    
        




board = Board()
board.players=[human,machine]
w = board.play()
r = board._order[w]
print(board)
print(f"{r if w != False else 'Nobody'} Wins")