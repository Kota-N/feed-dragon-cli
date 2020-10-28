from random import randint

food_count = 0
dragon_state = 0

def pick_a_command(): 
    print("command list:\nsearch -> search food for your dragon\nfeed -> feed Dragon\nstatus -> check dragon status\nquit -> quit the game\n")
    game_command = input("Enter your command: ")

    if game_command == "search":
        search()
    elif game_command == "status":
        status()
    elif game_command == "feed":
        feed()
    elif game_command == "quit":
        quit_game()
    else:
        print("command not found: " + game_command + " <---\n")
        pick_a_command()
    


def search():
    global food_count
    print('Looking for food!')
    input('OK: (enter)')
    item_index = randint(0, 3)
    if item_index == 0:
        print("Found no beetles...\n")
    elif item_index == 1:
        print("Found 1 beetle.\n")
        food_count += 1
    else:
        print("Found " + str(item_index) + " beetles!\n")
        food_count += item_index
    pick_a_command()

def status():
    print('You have ' + str(food_count) + ' beetles.\nDragon Status: ' + str(dragon_state) + '/30')
    input('Go Back: (enter)\n')
    pick_a_command()
    

def feed():
    global food_count
    global dragon_state

    if food_count and dragon_state == 29:
        print("Congrats!")
        input("What!?: (enter)")
        print("You fed 30 beetles!")
        input("OK: (enter)")
        print("Look! Baby Dragon became big!")
        input("Wow: (enter)")
        print("Very big!")
        input("Oh, okay: (enter)")
        input("Quit: (enter)")
        quit_game()
        return

    elif food_count > 0:
        food_count -= 1
        dragon_state += 1
        print('You fed Baby Dragon(' + str(dragon_state) + '/30)\n')
    else:
        print('You don\'t have any food...\n')
    pick_a_command()

def quit_game():
    print('Bye!')
    return


pick_a_command()




