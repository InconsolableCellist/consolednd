#!/usr/bin/python3

def print_areas(areas):
    print("Areas")
    for i, area in enumerate(areas):
        print("{}: \"{}\"\n\t{} battles".format(i, area['name'], len(area['battles'])))

def print_battles(battles): 
    print("Battles")
    for i, battle in enumerate(battles):
        print("{}: \"{}\"\n\t{} participants".format(i, battle['name'], len(battle['participants'])))

def print_participants(participants):
    if len(participants) == 0:
        print("No participants")
        return

    for i, participant in enumerate(participants):
        if participant != {}:
            if participant.get('isPlayer', False): 
                print("{}: (P) {}".format(i, participant['name']))
            else: 
                print("{}: {}".format(i, participant['name']))

def print_players(players, full=False):
    if full: 
        print(json.dumps(players, sort_keys=True, indent=4))
    else:
        for player in players: 
            print("{}, Level {} {}".format(player['name'], player['class'], player['ranger']))

def get_input(prompt = "", acceptEmpty=True):
    retry = True
    response = ""

    while retry:
        if prompt == "":
            prompt = "> "

        try:
            response = input(prompt)
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass

        if acceptEmpty or response != "":
            retry = False
    return response


