import struct, string

class TicTacToeBoard:

    def __init__(self):
        self.board = (['N']*3,['N']*3,['N']*3)
        self.totalVisit = 0
        self.playHistory = []
                                      
    def PrintBoard(self):
        print(self.board[0][0] + "|" + self.board[1][0] + "|" + self.board[2][0])
        
        print(self.board[0][1] + "|" + self.board[1][1] + "|" + self.board[2][1])
        
        print(self.board[0][2] + "|" + self.board[1][2] + "|" + self.board[2][2])
        
    def play_square(self, col, row, val):
        self.playHistory.append((val, (col, row)))
        self.board[col][row] = val

    def get_square(self, col, row):
        return self.board[col][row]

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


global totalVisit

# By AvaGu
def mini_max_decision(Board,humanval,cpuval):
    current_min=2
    (v,min_row,min_col) = max_value(Board,current_min,humanval,cpuval)          
    return (min_row,min_col)

def min_value(Board,current_max,humanval,cpuval):
    Board.totalVisit +=1
    if Board.winner() == 'O':
        return (1,-1,-1)
    elif Board.winner() == 'X':
        return (-1,-1,-1)
    else:
        if Board.full_board():
            return (0,-1,-1)
        else:
            v = 2
            
            for col in range(3):
                for row in range(3):
                    if Board.board[row][col] == 'N':
                        Board.board[row][col] = humanval
                        (maximum,i,j) = max_value(Board,v,humanval,cpuval)
                        if maximum<current_max:
                            v=maximum
                            (max_row,max_col) = (row,col)
                            Board.board[row][col] = 'N'
                            break;
                        if maximum < v:
                            v = maximum
                            (max_row,max_col) = (row,col)
                        Board.board[row][col] = 'N'
                if v < current_max:
                    break
            return (v,max_row,max_col)

def max_value(Board,current_min,humanval,cpuval):
    Board.totalVisit +=1
    if Board.winner() == 'O':
        return (1,-1,-1)
    elif Board.winner() == 'X':
        return (-1,-1,-1)
    else:
        if Board.full_board():
            return (0,-1,-1)
        else:
            v = -2
            for col in range(3):
                for row in range(3):
                    if Board.board[row][col] == 'N':
                        Board.board[row][col] = cpuval
                        (minimum,i,j) = min_value(Board,v,humanval,cpuval)
                        if minimum>current_min:
                            v=minimum
                            (min_row,min_col) = (row,col)
                            Board.board[row][col] = 'N'
                            break;
                        elif v < minimum:
                            v = minimum
                            (min_row,min_col) = (row,col)
                        Board.board[row][col] = 'N'
                if v > current_min:
                    break;
            return (v,min_row,min_col)

def make_minimax_cpu_move(Board,humanval,cpuval):
    (i,j) = mini_max_decision(Board,humanval,cpuval)
    Board.play_square(i,j,cpuval)
    return True

def make_simple_cpu_move(board, cpuval):
    for i in range(3):
        for j in range(3):
            if(board.get_square(i,j)=='N'):
                board.play_square(i,j,cpuval)
                return True
    return False


def printHistory(Board):
    print "Output of trace of program in action"
    history = Board.playHistory
    for h in history:
        print str(h[0]) + " : " + str(h[1])

def play():
    Board = TicTacToeBoard()
    humanval =  'X'
    cpuval = 'O'
    Board.PrintBoard()
    
    while( Board.full_board()==False and Board.winner() == 'N'):
        print("your move, pick a row (0-2)")
        row = int(input())
        print("your move, pick a col (0-2)")
        col = int(input())

        if(Board.get_square(col,row)!='N'):
            print("square already taken!")
            continue
        else:
            Board.play_square(col,row,humanval)
            if(Board.full_board() or Board.winner()!='N'):
                break
            else:
                Board.PrintBoard()
                print("CPU Move")
                # make_simple_cpu_move(Board,cpuval)
                make_minimax_cpu_move(Board,humanval,cpuval)
                Board.PrintBoard()

    Board.PrintBoard()
    if(Board.winner()=='N'):
        print("Cat game")
    elif(Board.winner()==humanval):
        print("You Win!")
    elif(Board.winner()==cpuval):
        print("CPU Wins!")
    printHistory(Board)
    print "Total visit : " + str(Board.totalVisit)

def main():
    play()

main()
            
