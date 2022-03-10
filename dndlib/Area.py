import json, uuid, os

from dndlib import Menu     as menu
from dndlib import UI       as ui
from dndlib import Battle   as b

"""
Returns a new area object with some basic parameters 
"""
def new_area():
    area = {}
    area['name'] = ui.get_input("area name or location: ", acceptEmpty=False)
    area['desc'] = ui.get_input("enter a detailed description (optional): ", acceptEmpty=True)
    area['id'] = str(uuid.uuid4())
    area['battles'] = []

    return area

"""
Takes an area object, prints it and its battles, and allows you to choose a battle to edit

Returns the modified area object
"""
def edit_area(area):
    print("Editing area: {}".format(area['name']))

    quit = False
    while quit is False:
        os.system('clear')
        print("area: {} ({})\nDescription: {}\n".format(area['name'], area['id'], area['desc']))
        battles = area['battles']
        ui.print_battles(battles)

        response = menu.get_menuaction_from_options(menu.area_options)
        if response is menu.MenuActions.CANCEL:
            quit = True
        elif response is menu.MenuActions.NAME:
            area['name'] = ui.get_input("area name or location: ", acceptEmpty=False)
        elif response is menu.MenuActions.DESC:
            new_desc = ui.get_input("Enter new description: ", acceptEmpty=True)
            if new_desc != "":
                area['desc'] = new_desc
            else:
                print("Canceled.")
        elif response is menu.MenuActions.ADD:
            area['battles'].append(b.new_battle())
        elif isinstance(response, str) and response.isdigit() and int(response) >= 0 and int(response) <= len(battles)-1:
            modified_battle = b.edit_battle(battles[int(response)])
            print("in index {}".format(response))
            if modified_battle == {}:
                del battles[int(response)]
            else:
                battles[int(response)] = modified_battle
        elif response is menu.MenuActions.DELETE:
            if ui.get_input("\nReally delete this area? (y/N) ").lower() == 'y':
                area = {}
                quit = True

    return area

