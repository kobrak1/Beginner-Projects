




import sys
import keyboard

if keyboard.press_and_release("Esc"):
    sys.exit()

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print('--+-+--')
    print('|'+board['7'] + '|' + board['8'] + '|' + board['9']+'|')
    print('--+-+--')
    print('|'+board['4'] + '|' + board['5'] + '|' + board['6']+'|')
    print('--+-+--')
    print('|'+board['1'] + '|' + board['2'] + '|' + board['3']+'|')
    print('--+-+--')


def game():
    turn='X'
    count=0

    for i in range(10):
        printBoard(theBoard)
        print("ıt's your turn,"+turn+".Move to which place?")
        move=input()

        if theBoard[move]==' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place already filled.\nMove to which place?")
            continue

        if count >=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over!")
                print(f"{turn} won.")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
        if count== 9:
            print("\nGame Over!\n\nIt's Tie!!")

        if turn=='X':
            turn='O'
        else:
            turn='X'
    restart=input("Do you want to play again?(y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            theBoard[key]=' '

        game()
    else:
        sys.exit()
if __name__=="__main__":
    game()



