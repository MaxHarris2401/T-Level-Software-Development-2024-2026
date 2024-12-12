import random as rng

is_ai = False


empty_board_1 = [] # initialise empty board that will only change when a hit sinks a ship or misses
empty_board_2 = []
p2_board = [] # initialise board array
p1_board = [] # initialise board for the player
level = 1

# player 1
hits = 0
turns = 0

# player 2/ai
hits_2 = 0 
turns_2 = 0

player_turns = 1 


def main():
    global is_ai
    print("----------Battleships-----------\n1. New Game\n2. Help Screen\n3. Quit")
    while True:
        key_press_menu = input(">>> ")
        if key_press_menu == "1":
            setup_board()
            input_ship()
            display_board()
            player_turn()
            break
        elif key_press_menu == "2":
            print("To play, select a type of generation to use as the enemy board, between 1-3 or P for procedural generation\n \
                  Then, you must guess the position of the enemy ships using the grid (between 0-9 on rows or columns) and try to sink the entirety of the ship's length\n\
                  Once you have taken out all of the 5 enemy ships, you win\nOtherwise, you have 15 turns to win the game and if that number is exceeded the game will be over")
            key_press_help = input("Would you like to continue?\n>>> ")
            main()
        elif key_press_menu == "3":
            while True:
                exit_check = input("Are you sure you want to quit? Type Y or N\n>>> ")
                if exit_check.upper() == "Y":
                    print("Thanks for playing!")
                    exit()
                    break
                    
                elif exit_check.upper() == "N":
                    main()
                    break
                else:
                    print("Invalid option entered, please try again")
            
def setup_board():
    global empty_board_1
    global empty_board_2
    global p1_board
    global p2_board
    global level
    global is_ai
    for i in range(10):
        empty_board_1.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]) 
        empty_board_2.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        # empty boards to be displayed so the user has to play the game properly 
        p1_board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
        p2_board.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
   
    while True:
        game_mode = input("Type AI for AI player or M for multiplayer: ")
        if game_mode.upper() == "AI":
            is_ai = True
            while True:
                level = input("Enter a level (1-3) or type P for procedural generation: ")
                if level == "1" or level == "2" or level == "3":
                    print("Level",level)
                    break
                elif level.upper() == "P":
                    print("Procedural Generation")
                    for i in range(4): # different letter each time the for loop cycles
                        letter_val = (i % 4) + 1  
                        if letter_val == 1:
                            letter = "A"
                            length = 5
                        elif letter_val == 2:
                            letter = "B"
                            length = 4
                        elif letter_val == 3:
                            letter = "C"
                            length = 3
                        elif letter_val == 4:
                            letter = "S"
                            length = 3
                        place_ship(length, letter)
                    break
                else:
                    print("Invalid option entered, please try again")

            break
        elif game_mode.upper() == "M":
            is_ai = False
            break
        else:
            print("Invalid data entered, try again")
    
# levels system

    if level == "1":
        for i in range(5):
            board[3][3+i] = "A"
       
        for i in range(4):
            board[2+i][1] = "B"
            
        for i in range(3):
            board[7+i][5] = "S"
        
        for i in range(3):
            board[6][7+i] = "C"
            
    elif level == "2":
        for i in range(5):
            board[5+i][0] = "A"
           
        for i in range(4):
            board[7][2+i] = "B"
         
        for i in range(3):
            board[6][3+i] = "S"
           
        for i in range(3):
            board[1+i][9] = "C"
          
    elif level == "3":
        for i in range(5):
            board[2+i][8] = "A"
          
        for i in range(4):
            board[4+i][3] = "B"
        
        for i in range(3):
            board[4][5+i] = "S"
    
        for i in range(3):
            board[3+i][4] = "C"
    
def display_board():
    print("  0   1   2   3   4   5   6   7   8   9")
    for number, row in enumerate(empty_board_2): 
        # gets the number of each array and assigns it to the variable number
        print(number, " | ".join(row))
        print("   -+---+---+---+---+---+---+---+---+-")
    print(" --------------------------------------\n  0   1   2   3   4   5   6   7   8   9")
    for number, row in enumerate(empty_board_1): 
        # gets the number of each array and assigns it to the variable number
        print(number, " | ".join(row))
        print("   -+---+---+---+---+---+---+---+---+-")
        
def player_turn():
    global hits
    global turns

    global hits_2 # player 2/ai
    global turns_2

    global player_turns

    while game_over != True:
        if player_turns == 1:
            print("Player 1's Turn")
        else:
            print("Player 2's Turn")
        while True: # infinite while loop that breaks when correct data type entered
            str_col = input("Please enter a column (0-9): ")
            try:
                int_col = int(str_col)
                if int_col < 0 or int_col > 10:
                    print("Invalid value entered, please try again")
                else:
                    break
            except:
                print("Invalid data type entered, please try again")
        while True: # infinite while loop that breaks when correct data type entered
            str_row = int(input("Please enter a row (0-9): "))
            try:
                int_row = int(str_row)
                if int_row < 0 or int_row > 10:
                    print("Invalid value entered, please try again")
                else:
                    break
            except:
                print("Invalid data type entered, please try again")
                
        if player_turns == 1: # player 1
            if p2_board[int_col][int_row] == "A" or p2_board[int_col][int_row] == "B" or \
            p2_board[int_col][int_row] == "C" or p2_board[int_col][int_row] == "S":
                register = "\033[32mHit!\033[0m"
                p2_board[int_col][int_row] = "\033[32m*\033[0m" # red text
                # changed so you can't hit the same ship twice
                empty_board_2[int_col][int_row] = "\033[32m*\033[0m" 
                # changed so you can see you've hit that ship
                hits+=1
                turns+=1
            elif p2_board[int_col][int_row] == "-":
                register = "\033[31mMiss!\033[0m"
                p2_board[int_col][int_row] = "\033[31m.\033[0m" # green text
                # changed so you can't miss the same ship twice
                empty_board_2[int_col][int_row] = "\033[31m.\033[0m" 
                # changed so you can see you've missed that ship
                turns+=1
        else: # player 2
            if p1_board[int_col][int_row] == "A" or p1_board[int_col][int_row] == "B" or \
            p1_board[int_col][int_row] == "C" or p1_board[int_col][int_row] == "S":
                register = "\033[32mHit!\033[0m"
                p1_board[int_col][int_row] = "\033[32m*\033[0m" # red text
                empty_board_1[int_col][int_row] = "\033[32m*\033[0m" 
                hits_2+=1
                turns_2+=1
            elif p1_board[int_col][int_row] == "-":
                register = "\033[31mMiss!\033[0m"
                p1_board[int_col][int_row] = "\033[31m.\033[0m" # green text
                empty_board_1[int_col][int_row] = "\033[31m.\033[0m" 
                
                turns_2+=1

        display_board()
        print(register)
        
        if player_turns == 1:
            if turns - 20 > 1:
                print("You have",str(20 - turns),"hit remaining")
            else:
                print("You have",str(20 - turns),"hits remaining")
        else:
            if turns_2 - 20 > 1:
                print("You have",str(20 - turns_2),"hit remaining")
            else:
                print("You have",str(20 - turns_2),"hits remaining")

        if game_over():
            print("Game over as number of turns has exceeded 20")
            exit()

        if has_won():
            print("Game over as player",str(player_turns),"won")
            exit()

        if is_ai:
            ai_turn()
        else:
            if player_turns == 1:
                player_turns = 2
            else:
                player_turns = 1

def has_won():
    global hits
    if hits == 15:
        return True
    elif hits_2 == 15:
        return True
    else:
        return False

def game_over():
    global turns
    if turns == 20:
        return True
    elif turns_2 == 20:
        return True
    else:
        return False

def ai_turn():
    global turns_2
    global hits_2

    input("\nAI's turn, press enter to continue:")

    hit_found = False
    direction = None  # direction of the attack after a hit (None, "horizontal", "vertical")
    last_hit = None 

    while True:
        if not hit_found:
            hit_row = rng.randint(0, 9)
            hit_col = rng.randint(0, 9)
        else:
            if direction == "horizontal":
                hit_col += 1  # attacking to the right
            elif direction == "vertical":
                hit_row += 1  # attacking downwards
            if hit_row > 9 or hit_col > 9:
                hit_found = False  # redo

        if empty_board_1[hit_row][hit_col] == "-":
            if p1_board[hit_row][hit_col] in ['A', 'B', 'C', 'S']:  # Ship hit
                print("AI attacks at ("+str(hit_row)+",", str(hit_col)+") - Hit!")
                p1_board[hit_row][hit_col] = "\033[32m*\033[0m"
                empty_board_1[hit_row][hit_col] = "\033[32m*\033[0m"
                hits_2 += 1
                hit_found = True
                last_hit = (hit_row, hit_col)

                if hit_col + 1 < 10 and p1_board[hit_row][hit_col + 1] == p1_board[hit_row][hit_col]:
                    direction = "horizontal"  # check to the right
                elif hit_row + 1 < 10 and p1_board[hit_row + 1][hit_col] == p1_board[hit_row][hit_col]:
                    direction = "vertical"  # check downwards

                turns_2 += 1
                display_board()
                break
            else: 
                print("AI attacks at ("+str(hit_row)+",", str(hit_col)+") - Miss!")
                p1_board[hit_row][hit_col] = "\033[31m.\033[0m"
                empty_board_1[hit_row][hit_col] = "\033[31m.\033[0m"
                turns_2 += 1
                display_board()
                break
        else:
            hit_found = False

def place_ship(ship_length, ship_letter):
    while True: # checks the length of ship isn't bigger than the index
        col_pos = rng.randint(0,9) # random column position
        row_pos = rng.randint(0,9) # random row position
        axis_pos = rng.randint(0,1) # 0 is horizontal 1 is vertical
        
        if axis_pos == 0:
            if col_pos + ship_length > 10:
                continue
        else:
            if row_pos + ship_length > 10:
                 continue
            
        can_place = True
        for i in range(ship_length):
            if axis_pos == 0:  # horizontal
                if board[row_pos][col_pos + i] != "-":
                    can_place = False
                    break
            else:  # vertical
                if board[row_pos + i][col_pos] != "-":
                    can_place = False
                    break
        
        if can_place:
            for i in range(ship_length):
                if axis_pos == 0:  # horizontal
                    board[row_pos][col_pos + i] = ship_letter
                else:  # vertical
                    board[row_pos + i][col_pos] = ship_letter
            break  # exit the loop after placing the ship

def input_ship():
    global player_turns
    global is_ai

    for player in (1, 2):
        if is_ai and player == 2:
            break  # skip player 2 if AI is enabled
        if player == 1:
            board_to_use = p1_board
        else:
            board_to_use = p2_board

        for i in range(4):  # different letter each time the for loop cycles

            display_board()

            letter_val = (i % 4) + 1
            # ship type cycle
            if letter_val == 1:
                ship_letter = "A"
                ship = "Aircraft Carrier"
                ship_length = 5
            elif letter_val == 2:
                ship_letter = "B"
                ship = "Battleship"
                ship_length = 4
            elif letter_val == 3:
                ship_letter = "C"
                ship = "Cruiser"
                ship_length = 3
            elif letter_val == 4:
                ship_letter = "S"
                ship = "Submarine"
                ship_length = 3

            while True:  # checks the length of ship isn't bigger than the index
                while True:
                    print("Player", player, "- Please enter co-ordinates for your", ship, "which is of the length:", str(ship_length) + "\n")
                    row_pos = input("Enter a row position (0-9): ")
                    col_pos = input("Enter a column position (0-9): ")
                    axis_pos = input("Enter an axis position (0 for horizontal and 1 for vertical): ")
                    try:
                        col_pos = int(col_pos)
                        row_pos = int(row_pos)
                        axis_pos = int(axis_pos)
                        if axis_pos < 0 or axis_pos > 1:
                            print("\nInvalid position entered, please try again")
                            continue
                        break
                    except:
                        print("\nInvalid data entered, please try again")

                if axis_pos == 0:
                    if col_pos + ship_length > 10:
                        print("\nPosition is too big for the grid, please try again")
                        continue
                else:
                    if row_pos + ship_length > 10:
                        print("\nPosition is too big for the grid, please try again")
                        continue

                can_place = True
                for i in range(ship_length):
                    if axis_pos == 0:  # horizontal
                        if board_to_use[row_pos][col_pos + i] != "-":
                            can_place = False
                            break
                    else:  # vertical
                        if board_to_use[row_pos + i][col_pos] != "-":
                            can_place = False
                            break

                if not can_place:
                    print("\nThis ship cannot be placed, please try again")
                    continue
                else:
                    for i in range(ship_length):
                        if axis_pos == 0:  # horizontal
                            board_to_use[row_pos][col_pos + i] = ship_letter
                        else:  # vertical
                            board_to_use[row_pos + i][col_pos] = ship_letter

                break  # exit the loop after placing the ships

main()