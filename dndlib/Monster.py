import json, uuid, copy

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from dndlib import FileIO   as dnd
from dndlib import UI       as ui

MONSTERS_FILE       = "monsters.json"

def get_monsters():
    return dnd.get_data_from_json_file(MONSTERS_FILE)

def find_monster():
    monster_names = []
    monsters = get_monsters()
    for monster in monsters:
        monster_names.append(monster['name'])
    monster_completer = WordCompleter(monster_names, ignore_case=True)
    text = prompt("\n\nEnter monster: ", completer=monster_completer)

    try:
        index = next(i for i,v in enumerate(monster_names) if v.lower() == text.lower())
        monster = copy.deepcopy(monsters[index])
    except StopIteration:
        print("Unable to find an existing monster by the name of {}. Making a new one".format(text))
        monster = { 'name' : text, 'type' : 'unknown', 'armor_class' : '', 'hit_points' : '' }

    monster['uuid'] = str(uuid.uuid4())
    print("Monster information: {}".format(json.dumps(monster, indent=4, sort_keys=True)))
    quit = False
    while quit is False:
        response = ui.get_input("\nUse this monster? (y/n) ", acceptEmpty=False).lower()
        if response == 'y':
            quit = True
        elif response == 'n':
            monster = {}
            quit = True

    return monster

