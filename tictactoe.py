import struct, string

class TicTacToeBoard:

    def __init__(self):
        self.board = [['N','N','N'],['N','N','N'],['N','N','N']]
                                      
    def PrintBoard(self):
        print(self.board[0][0] + "|" + self.board[0][1] + "|" + self.board[0][2])
        
        print(self.board[1][0] + "|" + self.board[1][1] + "|" + self.board[1][2])
        
        print(self.board[2][0] + "|" + self.board[2][1] + "|" + self.board[2][2])
        
    def play_square(self, row, col, val):
        self.board[row][col] = val

    def get_square(self, row, col):
        return self.board[row][col]

    def full_board(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j]=='N'):
                    return False
        return True
    
    #if there is a winner this will return their symbol (either 'X' or 'O'),
    #otherwise it will return 'N'
    def winner(self):
        #check the cols
        for col in range(3):
            if(self.board[col][0]!='N' and self.board[col][0] == self.board[col][1] and self.board[col][0]==self.board[col][2] ):
                return self.board[col][0]
        #check the rows
        for row in range(3):
            if(self.board[0][row]!='N' and self.board[0][row] == self.board[1][row] and self.board[0][row]==self.board[2][row] ):
                return self.board[0][row]
        #check diagonals
        if(self.board[0][0]!='N' and self.board[0][0] == self.board[1][1] and self.board[0][0]==self.board[2][2] ):
            return self.board[0][0]
        if(self.board[2][0]!='N' and self.board[2][0] == self.board[1][1] and self.board[2][0]==self.board[0][2]):
            return self.board[2][0]
        return 'N'


def MinMax(board, cpuMove, humanMove, toggle=0, count=0):
    if board.winner()==cpuMove:
        return (1,None)
    elif board.winner()==humanMove:
        return (-1,None)
    elif board.full_board() and board.winner() == 'N':
        return (0,None)
        
    elif toggle == 0:
        best_move = (-2,None)
        for i in range(len(board.board)):
            for j in range(len(board.board[0])):
                if board.get_square(i,j)=='N':
                    board.play_square(i,j,cpuMove)
                    move = MinMax(board,cpuMove,humanMove,1,count+1)
                    if count == 0:
                        print "max : ", move, "count :",count
                    board.play_square(i,j,'N')
                    if move[0] > best_move[0] :
                        best_move = (move[0],i,j)
        return best_move

    else:
        best_move = (2,None)
        for i in range(len(board.board)):
            for j in range(len(board.board[0])):
                if board.get_square(i,j)=='N':
                    board.play_square(i,j,humanMove)
                    move = MinMax(board,cpuMove,humanMove,0,count+1)
                    if count == 0:
                        print "min :", move, "count :", count
                    board.play_square(i,j,'N')
                    if move[0] < best_move[0] :
                        best_move = (move[0],i,j)
        return best_move

def make_simple_cpu_move(board, cpuval):
    for i in range(3):
        for j in range(3):
            if(board.get_square(i,j)=='N'):
                board.play_square(i,j,cpuval)
                return True
    return False

def play():
    humanval =  'X'
    cpuval = 'O'
    Board = TicTacToeBoard()
    Board.PrintBoard()
    
    while( Board.full_board()==False and Board.winner() == 'N'):
        print("your move, pick a row (0-2)")
        row = int(input())
        print("your move, pick a col (0-2)")
        col = int(input())

        if(Board.get_square(row,col)!='N'):
            print("square already taken!")
            continue
        else:
            Board.play_square(row,col,humanval)
            if(Board.full_board() or Board.winner()!='N'):
                break
            else:
                Board.PrintBoard()
                print("CPU Move")
                #make_simple_cpu_move(Board,cpuval)
                score,i,j = MinMax(Board,cpuval,humanval)
                print score,i,j
                Board.play_square(i,j,cpuval)
                Board.PrintBoard()

    print("------------------------")
    Board.PrintBoard()
    if(Board.winner()=='N'):
        print("Cat game")
    elif(Board.winner()==humanval):
        print("You Win!")
    elif(Board.winner()==cpuval):
        print("CPU Wins!")

def main():
    play()

main()
            
