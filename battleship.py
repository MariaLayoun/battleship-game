water = "~"
boat = "0"
hit = "|"
sunk = "X"
fired = "_"
 
player1_grid = [[water, water, water, water],[water, water, water, water], [water, water, water, water], [water, water, water, water]]
player2_grid = [[water, water, water, water], [water, water, water, water], [water, water, water, water], [water, water, water, water]]
 
player1_visible_grid = [[water, water, water, water], [water, water, water, water], [water, water, water, water], [water, water, water, water]]
player2_visible_grid = [[water, water, water, water], [water, water, water, water], [water, water, water, water], [water, water, water, water]]
 
def uinput(string):
    return input(string + " ")
 
# 0 0 ~ ~
# ~ ~ ~ ~
# ~ ~ ~ ~
# ~ 0 0 ~
 
def print_grid(grid):
    returnGrid = ""
    for row in grid:
        for column in row:
            returnGrid += str(column) + " "
        returnGrid += "\n"
    print(returnGrid)
 
def check_win(grid):
    won = True
    for row in grid:
        for column in row:
            if column == boat or column == hit:
                won = False
    return won
 
print(f"Welcome to battleship! Here is something you need to know:\nOn a grid,\n{water} is water\n{boat} is a boat\n{hit} is a hit part of a boat\n{sunk} is a part of a sunken ship\n{fired} is a spot on the board that has been fired at, and is empty")
 
for player in range(1,3):
    print(f"\nPlayer {player} Boats:\n")
    for ship in range(1,3):
        can_continue = False
        column1 = 0
        row = 0
        while can_continue == False:
            try:
                column1 = int(uinput(f"Boat {ship} column (1-4):"))
                if column1 > 4 or column1 < 1:
                    Error # Throws an error if ran, successfully parses
                row = int(uinput(f"Boat {ship} row (1-4):"))
                if row > 4 or row < 1:
                    Error # Throws an error if ran, successfully parses
                if column1 == 4:
                    column2 = 3
                else:
                    column2 = column1+1
                if player == 1:
                    if player1_grid[row-1][column1-1] == boat or player1_grid[row-1][column2-1] == boat:
                        Error # Throws an error if ran, successfully parses
                else:
                    if player2_grid[row-1][column1-1] == boat or player2_grid[row-1][column2-1] == boat:
                        Error # Throws an error if ran, successfully parses
                can_continue = True
            except:
                print("Sorry, please enter a number from 1-4 for the boat's column and row, and don't create overlapping boats.")
 
        if column1 == 4:
            column2 = 3
        else:
            column2 = column1+1
 
        if player == 1:
            player1_grid[row-1][column1-1]=boat
            player1_grid[row-1][column2-1]=boat
        else:
            player2_grid[row-1][column1-1]=boat
            player2_grid[row-1][column2-1]=boat
    print("Here is your grid!")
    if player == 1:
        print_grid(player1_grid)
    else:
        print_grid(player2_grid)
while True:
    if check_win(player2_grid) == True or check_win(player1_grid) == True:
        break
    for player in range(1,3):
        print(f"Player {player}'s turn:\nWhat position would you like to fire at?")
        can_continue = False
        column = 0
        row = 0
        while can_continue == False:
            try:
                column = int(uinput(f"Firing column (1-4):"))
                if column > 4 or column < 1:
                    Error # Throws an error if ran, successfully parses
                row = int(uinput(f"Firing row (1-4):"))
                if row > 4 or row < 1:
                    Error # Throws an error if ran, successfully parses
                can_continue = True
            except:
                print("Sorry, please enter a number from 1-4 for the firing point's column and row.")
        if player == 1:
            position = player2_grid[row-1][column-1]
            if position == water:
                player2_grid[row-1][column-1] = fired
                player2_visible_grid[row-1][column-1] = fired
                print("It's a miss! Here's the current boards:")
                print_grid(player2_visible_grid)
            elif position == boat:
                player2_grid[row-1][column-1] = hit
                player2_visible_grid[row-1][column-1] = hit
                print("It's a hit! Here's the current boards:")
                print_grid(player2_visible_grid)
            elif position == hit:
                player2_grid[row-1][column-1] = sunk
                player2_visible_grid[row-1][column-1] = sunk
                print("It's a hit! You sunk part of a battleship! Here's the current boards:")
                print_grid(player2_visible_grid)
            elif position == fired:
                player2_grid[row-1][column-1] = fired
                player2_visible_grid[row-1][column-1] = fired
                print("You already fired here! You loose a turn :( Here's the current boards:")
                print_grid(player2_visible_grid)
            elif position == sunk:
                player2_grid[row-1][column-1] = sunk
                player2_visible_grid[row-1][column-1] = sunk
                print("You already sunk this ship! You loose a turn :( Here's the current boards:")
                print_grid(player2_visible_grid)
        else:
            position = player1_grid[row-1][column-1]
            if position == water:
                player1_grid[row-1][column-1] = fired
                player1_visible_grid[row-1][column-1] = fired
                print("It's a miss! Here's the current boards:")
                print_grid(player1_visible_grid)
            elif position == boat:
                player1_grid[row-1][column-1] = hit
                player1_visible_grid[row-1][column-1] = hit
                print("It's a hit! Here's the current boards:")
                print_grid(player1_visible_grid)
            elif position == hit:
                player1_grid[row-1][column-1] = sunk
                player1_visible_grid[row-1][column-1] = sunk
                print("It's a hit! You sunk part of a battleship! Here's the current boards:")
                print_grid(player1_visible_grid)
            elif position == fired:
                player1_grid[row-1][column-1] = fired
                player1_visible_grid[row-1][column-1] = fired
                print("You already fired here! You loose a turn :( Here's the current boards:")
                print_grid(player1_visible_grid)
            elif position == sunk:
                player1_grid[row-1][column-1] = sunk
                player1_visible_grid[row-1][column-1] = sunk
                print("You already sunk this ship! You loose a turn :( Here's the current boards:")
                print_grid(player1_visible_grid)
        if check_win(player1_grid) == True or check_win(player2_grid) == True:
            print(f"Congrats, Player {player}! You won!")
            break
