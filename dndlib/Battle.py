import json, uuid, os

from dndlib import Menu     as menu
from dndlib import UI       as ui
from dndlib import Participants as p

"""
Returns a new battle object with some basic parameters 
"""
def new_battle():
    battle = {}
    battle['name'] = ui.get_input("Battle name or location: ", acceptEmpty=False)
    battle['desc'] = ui.get_input("Battle description: ", acceptEmpty=True)
    battle['id'] = str(uuid.uuid4())
    battle['participants'] = []

    return battle

"""
Takes a battle object, prints it and its participants, and allows you to edit it

Returns the modified battle object
"""
def edit_battle(battle):
    print("Editing battle: {}".format(battle['name']))

    quit = False
    while quit is False:
        os.system('clear')
        print("Battle: {} ({})\nDescription: {}\n".format(battle['name'], battle['id'], battle['desc']))
        participants = battle['participants']
        ui.print_participants(participants)

        response = menu.get_menuaction_from_options(menu.battlefield_options)
        if response is menu.MenuActions.CANCEL:
            quit = True
        elif response is menu.MenuActions.NAME:
            battle['name'] = ui.get_input("Battle name or location: ", acceptEmpty=False)
        elif response is menu.MenuActions.DESC:
            new_desc = ui.get_input("Enter new description: ", acceptEmpty=True)
            if new_desc != "":
                battle['desc'] = new_desc
            else:
                print("Canceled.")
        elif response is menu.MenuActions.ADD:
            participant = p.add_participant(battle['participants'])
            print(json.dumps(participant))
            if participant != {}:
                battle['participants'].append(participant)
        elif isinstance(response, str) and response.isdigit() and int(response) >= 0 and int(response) <= len(participants)-1:
            modified_participant = p.edit_participant(participants[int(response)])
            print("in index {}".format(response))
            if modified_participant == {}:
                del participants[int(response)]
            else:
                participants[int(response)] = modified_participant
        elif response is menu.MenuActions.DELETE:
            if ui.get_input("\nReally delete this battle? (y/N) ").lower() == 'y':
                battle = {}
                quit = True

    return battle

