import json, os

from dndlib import FileIO   as dnd
from dndlib import Menu     as menu
from dndlib import UI       as ui
from dndlib import Monster  as m

import pdb


PLAYERS_FILE        = "players.json"

def get_players():
    players_file = dnd.get_data_from_json_file(PLAYERS_FILE)
    return players_file.get('players', [])

def unroll_values(i, key, value): 
    if isinstance(value, dict):
        for k2, v2 in value.items():
            i = unroll_values(i, k2, v2)
    elif isinstance(value, list):
        for item in value:
            i = unroll_values(i, "", item)
            
    else:
        print("{:<3}: {:<30}: {:<60}".format(i, key, value))
        i += 1
    return i

def edit_participant_full(participant):
    quit = False
    while quit is False:
        os.system('clear')
        p = participant

        i = 0
        for key, value in p.items():
            i = unroll_values(i, key, value)
#            print("{}: {}: \t\t{}".format(i, key, value))
#            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float):
#                print("{:<3}: {:<30}: {:<60}".format(i, key, value))
#            else:
#                print("{}: {}: {}".format(i, key, json.dumps(value)))
#                pdb.set_trace()
#            i += 1


        response = menu.get_menuaction_from_options(menu.edit_participant_full_options)
        if response is menu.MenuActions.CANCEL:
            quit = True
        elif response is menu.MenuActions.DELETE:
            p = {}
            quit = True

    return participant

def edit_participant(participant):
    quit = False
    while quit is False:
        os.system('clear')
        p = participant
        if p.get('isPlayer', False):
            print("{}, a level {} {} {} {}\n".format(p['name'], p['level'], p['class'], p['race'], "PLAYER" if p['isPlayer'] else ""))
        else:
            print("An NPC {} of type {}. AC {}, HP {}.\n".format(p['name'], p['type'], p['armor_class'], p['hit_points']))

        print(json.dumps(p, sort_keys=True, indent=4))
        response = menu.get_menuaction_from_options(menu.edit_participant_options)
        if response is menu.MenuActions.CANCEL:
            quit = True
        elif response is menu.MenuActions.DELETE:
            p = {}
            quit = True
        elif response is menu.MenuActions.NAME:
            p['name'] = ui.get_input("Change name from \"{}\" to: ".format(p['name']), acceptEmpty=False)

    return p

def add_participant(current_participants):
    participant = {}
    players = get_players()

    quit = False
    while quit is False:
        os.system('clear')
        i = 0
        print("Available players: ")
        for player in players:
            print("{}: {}, Level {} {}".format(i, player['name'], player['level'], player['class']))
            i += 1

        print("\n\n{}: add new monster".format(i))

        response = menu.get_menuaction_from_options(menu.add_participant_options)
        if response is menu.MenuActions.CANCEL:
            quit = True
        elif isinstance(response, str) and response.isdigit() and int(response) >= 0:
            if int(response) <= len(players)-1:
                participant = players[int(response)]
                quit = True
                for current_participant in current_participants:
                    if current_participant['id'] == participant['id']:
                        print("{} is already a participant in this battle!".format(participant['name']))
                        input("Press return to continue.")
                        quit = False
                        participant = {}
                        break
            elif int(response) == i:
                # i = the last item, add new monster
                print("\nAdding new monster")
                monster = m.find_monster()
                participant = monster
                quit = True

    return participant

