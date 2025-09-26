# pylint: disable=C0200
# Hidden Word
# Grille de mots cachés

import time
import sys
import random

class WordGame():
    """Word Game class init"""
    def __init__(self,board_game):
        self.board_game: list[list[str]] = board_game
        self.max:int = len(self.board_game) - 1
        self.board_str: str = ""
        self.list_of_final_position: list[tuple(int,int)] = []
        self.list_of_final_letter: list[str] = []
        self.board_to_str()

    def display_board(self) -> None:
        """A function that display the game board"""
        for line_word in self.board_game:
            for letter in line_word:
                print(letter,end=" ")
            print("")

    def board_to_str(self) -> None:
        "A fonction that convert the board game to a string"
        for line_word in self.board_game:
            for letter in line_word:
                self.board_str +=letter.lower()
           
    def display_board_better(self) -> None:
        """A function that display the game board but with a better design"""
        for i in range(len(self.board_game)):
            for j in range(len(self.board_game[i])):
                print(f"--- {self.board_game[i][j]} --- ",end=" ")
            print("\n")
    
    def print_file_content(self,path:str) -> str:
        """A function that print the content of a given file"""
        f = open(path, 'r',encoding="utf-8")
        content = f.read()
        f.close()
        return content

    def word_search_algorithm(self,short_word=False) -> None:
        """A function that does an algorithm to check all the posible move possible from words of 2 letter"""
        for y in range(len(self.board_game)):
            for x in range(len(self.board_game[y])):
                list_of_good_moves , list_of_good_moves_letter = self.list_of_possible_moves(y,x)
                for position , letter in zip(list_of_good_moves,list_of_good_moves_letter):
                    #print(self.board_game[y][x] + letter, [(y,x),(position[0],position[1])])
                    self.algo_recursive(self.board_game[y][x] + letter,position,[(y,x),(position[0],position[1])])

                    # To get word with only 2 letters:
                    if short_word:
                        self.list_of_final_position.append([(y,x),(position[0],position[1])])
                        self.list_of_final_letter.append((self.board_game[y][x] + letter).lower())
                    
    def algo_recursive(self,letters,position,list_of_position=None,print_=None) ->None:
        """A function that does a recurcive of (the word search algorithm) to get word of size 3 to X letters lenght"""
        print_list_position:list[list[int]] = []
        print_list_letter:list[str] = []
       
        for y in range(len(self.board_game)):
            for x in range(len(self.board_game[y])):
                current_position = (y,x)
                if current_position == position:
                    list_of_good_moves , list_of_good_moves_letter = self.list_of_possible_moves(y,x,list_of_position)
                    list_of_good_moves , list_of_good_moves_letter = self.remove_bad_position_from_list(list_of_position,list_of_good_moves,list_of_good_moves_letter)
                    
                    for position , letter in zip(list_of_good_moves,list_of_good_moves_letter):
                        self.list_of_final_position.append(list_of_position+ [position])
                        self.list_of_final_letter.append(str(letters+letter).lower())
                        print_list_position.append(list_of_position+ [position])
                        print_list_letter.append(str(letters+letter).lower())
                    if print_:
                        print(list_of_good_moves , list_of_good_moves_letter)
                        print(list_of_position+["regnergoirejgioerjgerjigo",position])
                        print(self.list_of_final_position)
                        print(print_list_position)
                        print(print_list_letter)
                    return
    
    def generate_random_board(board_len=5) -> list[list[str]]:
        """A function that generate a random board with random letter"""
        board:list[list[str]] = []
        alphabet:str = "abcdefghijklmnopqrstuvwxyz"
        random_list_of_letter:list[str] = []
        tiny_board:list[str] = []
        
        for i in range(board_len * board_len):
            random_list_of_letter.append(alphabet[random.randint(0,len(alphabet) - 1)])

        for letter in random_list_of_letter:
            tiny_board.append(letter)
            if len(tiny_board) == board_len:
                board.append(tiny_board)
                tiny_board = []
        return board
    
    def print_list_in_alphabetic_order(self,lista,listb) -> None:
        """A function that sort a the list_a in alphabetic order and also sort the list_b taking into account the sorting of list_a"""
        combined = list(zip(lista, listb))
        combined_sorted = sorted(combined, key=lambda x: x[0])
        sorted_a, sorted_b = zip(*combined_sorted)
        sorted_a = list(sorted_a)
        sorted_b = list(sorted_b)

        print("Sorted list_a:", sorted_a)
        print("Sorted list_b:", sorted_b)
    
    def remove_bad_position_from_list(self,position_to_avoid,list_of_positions,list_of_letters) -> tuple[list[tuple[int]],list[str]]:
        """A function that remove bad position from the list of position"""

        good_position_list = []
        good_letter_list = []
        
        for position , letter in zip(list_of_positions,list_of_letters):
            if position not in position_to_avoid:
                good_position_list.append(position)
                good_letter_list.append(letter)
        
        return good_position_list , good_letter_list

    def is_position_good(self,position_list,correct_word) -> bool:
        "A function that check if a possition is correct by checking if the letters of the position are equal to the correct word"
        word = ""
        for position in position_list:
            x , y = position[0] , position[1]
            word+= self.board_game[x][y]
        
        if word.lower() != correct_word.lower():
            print(f"Word: {word.lower()} Correct Word: {correct_word.lower()}")
        return word.lower() == correct_word.lower()


    def list_of_possible_moves(self,y,x,position=[]) -> tuple[list[tuple[int]],list[str]]:
        """A function that check all the possible moves the algorithm can do"""
        list_of_good_moves:list[tuple[int]] = []
        list_of_good_letter:list[str] = []

        ########### CASE 1
        if x - 1 >= 0 and y - 1 >= 0 and (y-1,x-1) not in position:
            #print(self.board_game, self.board_game , self.board_game[y-1][x-1] , y - 1, x - 1 , " case 1")
            list_of_good_moves.append((y-1,x-1))
            list_of_good_letter.append(self.board_game[y-1][x-1])
        ########### CASE 2
        if y - 1 >= 0 and (y-1,x) not in position:
            #print(self.board_game, self.board_game , self.board_game[y-1][x] , y - 1, x , " case 2")
            list_of_good_moves.append((y-1,x))
            list_of_good_letter.append(self.board_game[y-1][x])
        
        ########### CASE 3
        if x + 1 <= self.max and y - 1 >= 0 and (y-1,x+1) not in position:
            #print(self.board_game, self.board_game , self.board_game[y-1][x+1] , y - 1, x + 1 , " case 3")
            list_of_good_moves.append((y-1,x+1))
            list_of_good_letter.append(self.board_game[y-1][x+1])
        ########### CASE 4
        if x - 1 >= 0 and (y,x-1) not in position:
            #print(self.board_game, self.board_game , self.board_game[y][x-1] , y , x - 1 , " case 4")
            list_of_good_moves.append((y,x-1))
            list_of_good_letter.append(self.board_game[y][x-1])
        
        ########### CASE 5
        if x + 1 <= self.max and (y,x+1) not in position:
            #print(self.board_game, self.board_game , self.board_game[y][x+1] , y , x + 1 , " case 5")
            list_of_good_moves.append((y,x+1))
            list_of_good_letter.append(self.board_game[y][x+1])
        
        ########### CASE 6
        if x - 1 >= 0 and y + 1 <= self.max and (y+1,x-1) not in position:
            #print(self.board_game, self.board_game , self.board_game[y+1][x-1] , y + 1, x - 1 , " case 6")
            list_of_good_moves.append((y+1,x-1))
            list_of_good_letter.append(self.board_game[y+1][x-1])
        ########### CASE 7
        if y + 1 <= self.max and (y+1,x) not in position:
            #print(self.board_game, self.board_game , self.board_game[y+1][x] , y + 1 , x, " case 7")
            list_of_good_moves.append((y+1,x))
            list_of_good_letter.append(self.board_game[y+1][x])
    
        ########### CASE 8
        if x + 1 <= self.max and y + 1 <= self.max and (y+1,x+1) not in position:
            #print(self.board_game, self.board_game , self.board_game[y+1][x+1] , y + 1, x + 1, " case 8")
            list_of_good_moves.append((y+1,x+1))
            list_of_good_letter.append(self.board_game[y+1][x+1])
        
        return list_of_good_moves , list_of_good_letter
        
        
# letter_list: list[list[str]] = [
#     ["E","A","Qu","U","E"],
#     ["F","R","I","T","R"],
#     ["I","L","O","H","S"],
#     ["I","S","S","O","T"],
#     ["A","H","G","U","X"]
#     ]

# game_letter_list: list[list[str]] = [
#     ["L", "A", "V", "E", "R"],
#     ["M", "O", "N", "T", "E"],
#     ["S", "U", "D", "I", "T"],
#     ["P", "A", "R", "I", "S"],
#     ["F", "Ê", "T", "E", "S"]
# ]

game_letter_list: list[list[str]] = [
    ["O","P","E","E","M"],
    ["C","S","J","A","A"],
    ["D","E","E","P","T"],
    ["B","U","D","J","E"],
    ["E","E","An","Z","R"]
    ]

game_letter_list: list[list[str]] = [
    ["N","B","B","E"],
    ["R","M","U","N"],
    ["I","N","E","A"],
    ["C","B","R","O"],
    ]


game_letter_list: list[list[str]] = [
    ["O","P","E","E","M"],
    ["C","S","J","A","A"],
    ["D","E","E","P","T"],
    ["B","U","D","J","E"],
    ["E","E","An","Z","R"]
    ]

game_letter_list: list[list[str]] = [
    ["L", "A", "V", "E", "R"],
    ["M", "O", "N", "T", "E"],
    ["S", "U", "D", "I", "T"],
    ["P", "A", "R", "I", "S"],
    ["F", "Ê", "T", "E", "S"]
]


start_time = time.time()
word = WordGame(game_letter_list)
# game_letter_list = generate_random_board(4)
# word = WordGame(game_letter_list)

correct_game_positions = []
correct_game_words = []
all_position = []
all_word = []
list_of_all_words_linked_to_their_lenght = []

try:
    max_word_lenght = int(sys.argv[1])
except:
    max_word_lenght = 5

for i in range(1,26):
    list_of_all_words_linked_to_their_lenght.append(word.print_file_content(f"list_of_french_words_{i}_char_lenght.txt").split("\n"))

for i in range(3,max_word_lenght):
    word.word_search_algorithm()
    for j in range(len(word.list_of_final_letter)):
        word.algo_recursive(word.list_of_final_letter[j],word.list_of_final_position[j][-1],word.list_of_final_position[j])
    all_position = all_position + word.list_of_final_position
    all_word = all_word + word.list_of_final_letter

end = True
if end:
    for position , letter in zip(all_position,all_word):
        if letter in list_of_all_words_linked_to_their_lenght[len(letter) - 1] and letter not in correct_game_words and position not in correct_game_positions:
            correct_game_positions.append(position)
            correct_game_words.append(letter)
    
    word.display_board_better()
    print(correct_game_positions)
    print(correct_game_words)
    print("Len ", max_word_lenght)
    print("Number of words found: " , len(correct_game_words))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")
