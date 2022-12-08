board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
print('1' + ' | ' + '2' + ' | ' + '3')
print('4' + ' | ' + '5' + ' | ' + '6')
print('7' + ' | ' + '8' + ' | ' + '9')
print("player 1 is 'x'")
print("player 2 is 'o'")
def draw_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
for i in range(9):
    try:
        take_spot = int(input("Enter the box number to play : "))
        spot = take_spot-1
    except:
        print("Error. ONLY NUMBER ARE ALLOWED, run the game again")
        exit()
    if spot >= 9:
        print("THERE ARE ONLY 9 BOXES")
    try:
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            board[spot] = 'x'
            draw_board()
        else:
            board[spot] = 'o'
            draw_board()
    except:
        print("Run the game again")
        exit()
    if board[0] == 'x' and board[4] == 'x' and board[8] == 'x' or board[0] == 'x' and board[3] == 'x' and board[6] == 'x' or board[1] == 'x' and board[4] == 'x' and board[7] == 'x' or board[2] == 'x' and board[5] == 'x' and board[8] == 'x' or board[2] == 'x' and board[4] == 'x' and board[6] == 'x' or board[0] == 'x' and board[1] == 'x' and board[2] == 'x' or board[3] == 'x' and board[4] == 'x' and board[5] == 'x' or board[6] == 'x' and board[7] == 'x' and board[8] == 'x':
        print("Player 'x' won the match")
        break
    elif board[0] == 'o' and board[4] == 'o' and board[8] == 'o' or board[0] == 'o' and board[3] == 'o' and board[6] == 'o' or board[1] == 'o' and board[4] == 'o' and board[7] == 'o' or board[2] == 'o' and board[5] == 'o' and board[8] == 'o' or board[2] == 'o' and board[4] == 'o' and board[6] == 'o' or board[0] == 'o' and board[1] == 'o' and board[2] == 'o' or board[3] == 'o' and board[4] == 'o' and board[5] == 'o' or board[6] == 'o' and board[7] == 'o' and board[8] == 'o':
        print("Player 'o' won the match")
        break
    if i == 8:
        print("Game over its a tie")
        
