import a3

board_file = r'c:\users\andrew\documents\programming\python\learn_to_program_class\assignment3\board1.txt'
board = open(board_file,'r')

wordlist_file = r'c:\users\andrew\documents\programming\python\learn_to_program_class\assignment3\wordlist1.txt'
word_list = open(wordlist_file,'r')

words = a3.read_words(word_list)

gameboard = a3.read_board(board)

player1 = ['John',4]
player2 = ['Sam',3]
player3 = ['Jenny',5]


players = (player1, player2, player3)







