#!/usr/bin/python3

import sys, time, json, uuid, readline, pdb, os, copy
from random import randint
from enum import Enum

from dndlib import FileIO   as dnd
from dndlib import Menu     as menu
from dndlib import UI       as ui
from dndlib import Battle   as b
from dndlib import Area     as a

CAMPAIGN_FILE   = "campaign.json"

def main():
    campaign = dnd.get_data_from_json_file(CAMPAIGN_FILE)

    quit = False
    while quit is False:
        os.system('clear')
        ui.print_areas(campaign['areas'])
        response = menu.get_menuaction_from_options(menu.main_options)
        if response is menu.MenuActions.QUIT: 
            if ui.get_input("\nReally quit? (y/N) ").lower() == 'y':
                quit = True
        elif response is menu.MenuActions.ADD:
            campaign['areas'].append(a.new_area())
        elif response is menu.MenuActions.SAVE:
            if dnd.save_data_to_json_file(campaign, CAMPAIGN_FILE):
                print("Successfully saved!")
                input("\nPress return to continue.\n")
            else:
                print("Something went wrong when saving the file! Dumping it to STDOUT")
                print(json.dumps(campaign))
        elif isinstance(response, str) and response.isdigit() and int(response) >= 0 and int(response) <= len(campaign['areas'])-1:
            area = a.edit_area(campaign['areas'][int(response)])
            if area == {}: 
                del campaign['areas'][int(response)]    

    print("Bye")

main()
