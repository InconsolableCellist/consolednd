#!/usr/bin/python3

from enum import Enum

from dndlib import UI   as ui

class MenuActions(Enum): 
    NONE = -1
    ADD = 1 
    EDIT = 2
    KILL_MONSTER = 3
    DELETE = 4
    CANCEL = 5
    QUIT = 6 
    YES = 7 
    NO = 8 
    SAVE = 9
    NAME = 10
    DESC = 11

main_options = { 
    '#' : { 'desc' : 'edit area (enter number)', 'action' : MenuActions.NONE },
    'a' : { 'desc' : 'add new area', 'action' : MenuActions.ADD },
    's' : { 'desc' : 'save', 'action' : MenuActions.SAVE },
    'q' : { 'desc' : 'quit', 'action' : MenuActions.QUIT } 
}

area_options = { 
    'a' : { 'desc' : 'add a battle', 'action' : MenuActions.ADD },
    'n' : { 'desc' : 'edit area name', 'action' : MenuActions.NAME },
    'i' : { 'desc' : 'edit area desc/info', 'action' : MenuActions.DESC },
    'd' : { 'desc' : 'delete area', 'action' : MenuActions.DELETE },
    'x' : { 'desc' : 'cancel', 'action' : MenuActions.CANCEL }
}

battlefield_options = { 
    'a' : { 'desc' : 'add participants', 'action' : MenuActions.ADD }, 
    'e' : { 'desc' : 'edit participants', 'action' : MenuActions.EDIT },
    'n' : { 'desc' : 'edit battle name', 'action' : MenuActions.NAME },
    'i' : { 'desc' : 'edit battle desc/info', 'action' : MenuActions.DESC },
    'd' : { 'desc' : 'delete battle', 'action' : MenuActions.DELETE },
    'x' : { 'desc' : 'cancel', 'action' : MenuActions.CANCEL }
}

edit_participant_options = { 
    'd' : { 'desc' : 'delete participant', 'action' : MenuActions.DELETE },
    'n' : { 'desc' : 'rename participant', 'action' : MenuActions.NAME },
    'x' : { 'desc' : 'cancel - back to participants list', 'action' : MenuActions.CANCEL }
}

edit_participant_full_options = {
    'd' : { 'desc' : 'delete participant', 'action' : MenuActions.DELETE },
    'x' : { 'desc' : 'cancel - back to participants list', 'action' : MenuActions.CANCEL }
}
add_participant_options = {
    '#' : { 'desc' : 'player/monster to add (type number)', 'action' : MenuActions.NONE }, 
    'x' : { 'desc' : 'cancel - back to battle', 'action' : MenuActions.CANCEL }
}

def get_menuaction_from_options(options):
    action = MenuActions.NONE

    print("\n")
    allowed_keys = []
    for k,v in options.items():
        print("{}: {}".format(k, v['desc']))
        allowed_keys.append(k)

    response = ui.get_input()
    if response in options:
        action = options[response]['action']
    elif response.isdigit():
        action = response

    return action
