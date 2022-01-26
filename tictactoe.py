theboard = {'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ','1':' ','2':' ','3':' '}
def gameboard(place_holder):
    print(place_holder['7'] + '   |  ' + place_holder['8'] + '   |  ' + place_holder['9'])
    print('----+------+----')
    print(place_holder['4'] + '   |  ' + place_holder['5'] + '   |  ' + place_holder['6'])
    print('----+------+----')
    print(place_holder['1'] + '   |  ' + place_holder['2'] + '   |  ' + place_holder['3'])
def gamemain_function():
    player = 'X'
    player_tries = 0
    for i in range(10):
        gameboard(theboard)
        print('Its your turn ' +player+' Choose a place to move' )
        move = input(': ')
        if theboard[move] == ' ':
            theboard[move] = player
            player_tries+=1
        else:
            print('That place is already taken. \nPlease choose another place')
            continue
        if player_tries >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'***** " {player} " Won *****')
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] !=' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'**** " {player} " Won *****')
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] !=' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'***** " {player} " Won *****')
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'***** " {player} " Won *****')
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] !=' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'***** " {player} " Won *****')
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'**** " {player} " Won *****')
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] !=' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'**** " {player} " Won *****')
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] !=' ':
                gameboard(theboard)
                print('\nGame Over')
                print(f'**** "{player}" Won *****')
                break
        if player_tries == 9:
            print('\nGame Over')
            print('Its a tie')
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

gamemain_function()