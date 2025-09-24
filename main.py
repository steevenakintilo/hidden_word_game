# pylint: disable=C0200
# Hidden Word
# Grille de mots cachés

class WordGame():
    """Word Game class init"""
    def __init__(self,board_game):
        self.board_game: list[list[str]] = board_game
        self.good_word_list: list[str]
        self.max:int = 4
        self.all_correct_word = self.print_file_info("list_of_french_words_3_to_6_char_lenght.txt").split("\n")[0:-2]

    def display_board(self):
        """Display board function"""
        for line_word in self.board_game:
            for letter in line_word:
                print(letter,end=" ")
            print("")

    def display_board_better(self):
        """Display board function"""
        for i in range(len(self.board_game)):
            print(f"--- {self.board_game[i][0]} --- {self.board_game[i][1]} --- {self.board_game[i][2]} --- {self.board_game[i][3]} --- {self.board_game[i][4]} ---")
            print()

    def print_file_info(self,path):
        """Print File Info"""
        f = open(path, 'r',encoding="utf-8")
        content = f.read()
        f.close()
        return content

    def word_search_algorithm(self,search_y=-1,search_x=-1):
        """Word Search Algorithm"""
        current_word:str = ""
        list_of_word:list[str] = []
        max_len = 6

        for y in range(len(self.board_game)):
            for x in range(len(self.board_game[y])):
                #print(self.board_game[y],self.board_game[y][x],y,x)
                if x == 0 and y == 0:
                    list_of_good_moves , list_of_good_moves_letter = self.list_of_possible_moves(y,x)
                    for position , letter in zip(list_of_good_moves,list_of_good_moves_letter):
                        print(self.board_game[y][x] + letter)
                        print([(x,y),position])
                    #current_word+=self.board_game[y][x]
                    #print(self.board_game[y][x])  
                    #print(list_of_good_moves , list_of_good_moves_letter)
                #list_of_good_moves = self.list_of_possible_moves(y,x)
                #print(y,x,self.board_game[y][x],list_of_good_moves)
    def list_of_possible_moves(self,y,x):
        """List Of Possible Moves"""
        list_of_good_moves:list[list[int]] = []
        list_of_good_moves_letter:list[str] = []
        
        # CASE 1
        if x - 1 >= 0 and y - 1 >= 0:
            #print(self.board_game, self.board_game , self.board_game[y-1][x-1] , y - 1, x - 1 , " case 1")
            list_of_good_moves.append((y-1,x-1))
            list_of_good_moves_letter.append(self.board_game[y-1][x-1])
        # CASE 2
        if y - 1 >= 0:
            #print(self.board_game, self.board_game , self.board_game[y-1][x] , y - 1, x , " case 2")
            list_of_good_moves.append((y-1,x))
            list_of_good_moves_letter.append(self.board_game[y-1][x])
        
        # CASE 3
        if x + 1 <= self.max and y - 1 >= 0:
            #print(self.board_game, self.board_game , self.board_game[y-1][x+1] , y - 1, x + 1 , " case 3")
            list_of_good_moves.append((y-1,x+1))
            list_of_good_moves_letter.append(self.board_game[y-1][x+1])
        # CASE 4
        if x - 1 >= 0:
            #print(self.board_game, self.board_game , self.board_game[y][x-1] , y , x - 1 , " case 4")
            list_of_good_moves.append((y,x-1))
            list_of_good_moves_letter.append(self.board_game[y][x-1])
        
        # CASE 5
        if x + 1 <= self.max:
            #print(self.board_game, self.board_game , self.board_game[y][x+1] , y , x + 1 , " case 5")
            list_of_good_moves.append((y,x+1))
            list_of_good_moves_letter.append(self.board_game[y][x+1])
        
        # CASE 6
        if x - 1 >= 0 and y + 1 <= self.max:
            #print(self.board_game, self.board_game , self.board_game[y+1][x-1] , y + 1, x - 1 , " case 6")
            list_of_good_moves.append((y+1,x-1))
            list_of_good_moves_letter.append(self.board_game[y+1][x-1])
        # CASE 7
        if y + 1 <= self.max:
            #print(self.board_game, self.board_game , self.board_game[y+1][x] , y + 1 , x, " case 7")
            list_of_good_moves.append((y+1,x))
            list_of_good_moves_letter.append(self.board_game[y+1][x])
    
        # CASE 8
        if x + 1 <= self.max and y + 1 <= self.max:
            #print(self.board_game, self.board_game , self.board_game[y+1][x+1] , y + 1, x + 1, " case 8")
            list_of_good_moves.append((y+1,x+1))
            list_of_good_moves_letter.append(self.board_game[y+1][x+1])
        
        #print(f"Board Piece: {self.board_game[y][x]} Y: {y} X: {x} List_of_good_moves: {list_of_good_moves}")

        return list_of_good_moves , list_of_good_moves_letter
        
        
# letter_list: list[list[str]] = [
#     ["E","A","Qu","U","E"],
#     ["F","R","I","T","R"],
#     ["I","L","O","H","S"],
#     ["I","S","S","O","T"],
#     ["A","H","G","U","X"]
#     ]

game_letter_list: list[list[str]] = [
    ["O","P","E","E","M"],
    ["C","S","J","A","A"],
    ["D","E","E","P","T"],
    ["B","U","D","J","E"],
    ["E","E","An","Z","R"]
    ]

word = WordGame(game_letter_list)

word.word_search_algorithm()
word.display_board_better()
