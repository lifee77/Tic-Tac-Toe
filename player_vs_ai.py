#This is a version of the game where the user can play with the AI. It should be tough.

from enum import Enum

#This will import the function minimax from the algorithm file
from minimax_algorithm import minimax

#Setting a class to define a grid out of nine total

class GridSquare():
    state = "" # -1 is empty, 0 is O and 1 is X
    pos = 0

    #setting a constructor to give position to each instance

    def __init__(self, x):#x is the position
        self.pos = x
        self.state = "-1" #This will only run in the beginning of the program so by default everything will be empty

    #This function will draw the symbol X or O or will keep the number of grid if it's empty.

    def draw_space(self):
        if self.state == "1":
            return "X"
        elif self.state == "0":
            return "O"
        else:
            return str(self.pos)[0]
class TicTacToe():
    rows = 3
    cols = 3
    total_turns = 0
    winner = -1

    #This is to show the state of the game
    class GameState(Enum):
        OVER = 0
        RUNNING = 1

    current_state = GameState.OVER
#Settting up the board
    board = None
    #This is the primary game setup
    def setup(self):
        self.board = [[None] * self.cols for _ in range(self.rows)]
        position = 1
        r = 0 #counter
        while r < self.rows:
            c = 0 #control for nested loops
            while c < self.cols:
                self.board[r][c] = GridSquare(position)
                position += 1
                c += 1
            r += 1


        #Setting the game state to running and calling the play game method
        TicTacToe.current_state = TicTacToe.GameState.RUNNING
        self.play_game()

#This method will call one of next three methods based on needs
    def play_game(self):
        while TicTacToe.current_state == TicTacToe.GameState.RUNNING:
            self.display_board()
            self.make_move()
        if TicTacToe.current_state == TicTacToe.GameState.OVER:
            self.display_game_over()

    def display_board(self):
        print("\n  " + str(self.board[0][0].draw_space()) + " | " + str(self.board[0][1].draw_space()) + "  | " + str(self.board[0][2].draw_space()))
        print(" ___|____|___ ")
        print("\n  " + str(self.board[1][0].draw_space()) + " | " + str(self.board[1][1].draw_space()) + "  | " + str(self.board[1][2].draw_space()))
        print(" ___|____|___ ")
        print("\n  " + str(self.board[2][0].draw_space()) + " | " + str(self.board[2][1].draw_space()) + "  | " + str(self.board[2][2].draw_space()))
        print(" ___|____|___ ")
    def make_move(self):
        final_board = [self.board[0][0].draw_space(), self.board[0][1].draw_space(), self.board[0][2].draw_space(),self.board[1][0].draw_space(), self.board[1][1].draw_space(), self.board[1][2].draw_space(),self.board[2][0].draw_space(), self.board[2][1].draw_space(), self.board[2][2].draw_space()]
        if str(self.get_player()) == 'X':
            best_outcome = -10
            best_move = 0

            for i in range(len(final_board)):
                if final_board[i] != 'X' and final_board[i] != 'O':
                    final_board[i] = 'X'
                    get_move = minimax(final_board, False)
                    final_board[i] = i
                    if get_move > best_outcome:
                        best_outcome = get_move
                        best_move = i + 1

            print("Player " + str(self.get_player()) + " chose " + str(best_move))
            i = 0
            while i < self.cols:
                j = 0
                while j < self.rows:
                    if str(self.board[i][j].state) == "-1" and str(self.board[i][j].pos) == str(best_move):
                        self.board[i][j].state = str(self.total_turns % 2)
                        self.total_turns += 1
                        self.check_win(i, j, str(self.board[i][j].state))
                    j += 1
                i += 1
            self.display_board()
        if str(self.get_player()) == "O":
            #print("Player " + str(self.get_player()) + " choose a pos: ")
            spot = input("Player " + str(self.get_player()) + " choose a position: ")

            i = 0
            while i < self.cols:
                j = 0
                while j < self.rows:
                    if str(self.board[i][j].state) == "-1" and str(self.board[i][j].pos) == spot:
                        self.board[i][j].state = str(self.total_turns % 2)
                        self.total_turns += 1
                        self.check_win(i, j, str(self.board[i][j].state))
                    j += 1
                i += 1


    def display_game_over(self):
        self.display_board()
        print("GAME OVERRRRRRRRR!!!!!!!!!!!!!!")
        if self.winner == "1":
            print("Player X won")
        elif self.winner == "0":
            print("Player O won")
        elif self.total_turns == 9 and not (self.winner == "1") and not self.winner == "0":
            print("It's a tie")


    #This will return the player playing currently.
    def get_player(self):
        if self.total_turns % 2 == 0:
            return 'O'
        return "X"

    #Method to check if someone won the game

    def check_win(self, x, y, turn):
        col_win = 0
        row_win = 0
        diag1_win = 0
        diag2_win = 0
        i = 0
        while i < 3:
            if self.board[x][i].state == turn:
                col_win += 1
            if self.board[i][y].state == turn:
                row_win +=1
            if self.board[i][i].state == turn:
                diag1_win += 1
            if self.board[i][2-i].state == turn:
                diag2_win += 1
            i += 1
        if col_win == 3 or row_win == 3 or diag1_win ==3 or diag2_win == 3:
            self.winner = turn
            if self.winner != "-1":
                TicTacToe.current_state = TicTacToe.GameState.OVER
        if self.total_turns == 9:
            TicTacToe.current_state = TicTacToe.GameState.OVER



game_Play = TicTacToe()
game_Play.setup()