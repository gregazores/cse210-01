
#Week 2 Introduction: Ponder and Prove Solo Submission
#Tic-Tac-Toe assignment for week 2
#Author: Jeevee Greg Azores

from pickle import TRUE


grid_array = []

def create_grid():
    for x in range(1, 10):
        grid_array.append(x)

def print_grid():
    array2txt = ""
    grid2display= []
    print()
    for y in range(0, 9):
        array2txt += f"{grid_array[y]}"

    for i in range(0, 3):
        grid2display.append("|".join(array2txt[3*i:(3*i + 3)]))
    
    print(f"\n-+-+-\n".join(grid2display))

def is_it_draw():
    #create a new list and save the remining integers of grid_array
    newlist = [x for x in grid_array if type(x) == int]

    #if we can't find any more integers, this means 
    # all squares have already been taken by either x or o
    #otherwise there's still available square to be marked by either x or o
    if newlist == []:
        return True
    else:
        return False

def get_player_input(player):
        #make sure that the user provides a number between 1 and 9 and that the chosen number is no longer taken
        while True:
            print()
            user_input = int(input(f'{player}\'s turn to choose a square (1-9): '))

            if user_input > 9:
                print()
                print('Please provide a number between 1 and 9.')
            elif grid_array[user_input - 1] == "x" or grid_array[user_input - 1] == "o":
                    print()
                    print('This square is already taken')
            else:
                return user_input - 1

def check_winner():

    x1 = f'{grid_array[0]}{grid_array[1]}{grid_array[2]}'
    x2 = f'{grid_array[3]}{grid_array[4]}{grid_array[5]}'
    x3 = f'{grid_array[6]}{grid_array[7]}{grid_array[8]}'
    x4 = f'{grid_array[0]}{grid_array[3]}{grid_array[6]}'
    x5 = f'{grid_array[1]}{grid_array[4]}{grid_array[7]}'
    x6 = f'{grid_array[2]}{grid_array[5]}{grid_array[8]}'
    x7 = f'{grid_array[0]}{grid_array[4]}{grid_array[8]}'
    x8 = f'{grid_array[2]}{grid_array[4]}{grid_array[6]}'

    o1 = f'{grid_array[0]}{grid_array[1]}{grid_array[2]}'
    o2 = f'{grid_array[3]}{grid_array[4]}{grid_array[5]}'
    o3 = f'{grid_array[6]}{grid_array[7]}{grid_array[8]}'
    o4 = f'{grid_array[0]}{grid_array[3]}{grid_array[6]}'
    o5 = f'{grid_array[1]}{grid_array[4]}{grid_array[7]}'
    o6 = f'{grid_array[2]}{grid_array[5]}{grid_array[8]}'
    o7 = f'{grid_array[0]}{grid_array[4]}{grid_array[8]}'
    o8 = f'{grid_array[2]}{grid_array[4]}{grid_array[6]}'

    if x1 == "xxx" or x2 == "xxx" or x3 == "xxx" or x4 == "xxx" or x5 == "xxx" or x6 == "xxx" or x7 == "xxx" or x8 == "xxx":
        return 1

    if o1 == "ooo" or o2 == "ooo" or o3 == "ooo" or o4 == "ooo" or o5 == "ooo" or o6 == "ooo" or o7 == "ooo" or o8 == "ooo":
        return 2

def run_game():
    #initialize the current player
    current_player = "x"
    while is_it_draw() == False:

        #getting the players's input and recording in in grid_array
        given_index = get_player_input(current_player)
        grid_array[given_index] = current_player

        #players taking turns
        if current_player == "x":
            current_player = "o"
        else:
            current_player = "x"
        
        print_grid()

        #check for winner
        if check_winner() == 1:
            print()
            print('The winner is X')
            break
        if check_winner() == 2:
            print()
            print('The winner is O')
            break
    
    if is_it_draw() == True:
        print()
        print("It is a draw")



def main():
    create_grid()
    print_grid()
    run_game()
    print("Good game. Thanks for playing!")
    








if __name__ == "__main__":
    main()


