import json

PLAYERS_PATH = 'resources/players.json'
SESSION_KEY_PATH = "resources/session_keys.json"

"""
Add player to game. Returns true if success. Returns false if:
    > Name is already in use
"""
def player_add(name, key):
    with open(PLAYERS_PATH, 'r') as fp:
        data = json.load(fp)
        if name in data.keys(): return False
        data[name] = {"team": "", "session_key": key}
    
    with open(PLAYERS_PATH, 'w') as fp:
        json.dump(data, fp)
    
    return True;


"""
Remove player from game. Returns true if success. Returns false if:
    > Name is not in game
"""
def player_remove(player):
    with open(PLAYERS_PATH, 'r') as fp:
        data = json.load(fp)

    with open(SESSION_KEY_PATH, 'r') as fp:
        sesh_info = json.load(fp)
        sesh_info['invalid_keys'].append(data[player]['session_key'])

    with open(SESSION_KEY_PATH, 'w') as fp:
        json.dump(sesh_info, fp)

    with open(PLAYERS_PATH, 'w') as fp:
        data.pop(player, None)
        json.dump(data, fp)

    return True


"""
Update player team. Returns true if success. Returns false if
    > Name is not in game
"""
def player_join(name, team):
    with open(PLAYERS_PATH, 'r') as fp:
        data = json.load(fp)
        if name not in data.keys(): return False
        
        data[name]['team'] = team

    with open(PLAYERS_PATH, 'w') as fp: json.dump(data, fp)
    
    return True


"""
Takes in an updated dictionary with the player information and replaces
it in the JSON file.
"""
def player_update(players):
    with open(PLAYERS_PATH, 'r') as fp:
        data = json.load(fp)

    to_remove = []
    with open(PLAYERS_PATH, 'w') as fp:
        new_data = {}
        for player in players.keys():
            if players[player] == "": to_remove.append(player)
            new_data[player] = {"team": players[player], "session_key": data[player]['session_key']}
        json.dump(new_data, fp)
    
    for player in to_remove: player_remove(player)
    return True


"""
Get player JSON dictionary.
"""
def player_get():
    with open(PLAYERS_PATH, 'r') as fp:
        data = json.load(fp)
    
    return data


"""
Get player information dictionary.
"""
def player_info(player):
    new_data = {}
    with open(PLAYERS_PATH, 'r') as fp:
        data = json.load(fp)

    new_data['name'] = player
    new_data['status'] = True
    new_data['team'] = data[player]['team']
    return new_data


"""
Clear player data
"""
def clear_player_data():
    with open(PLAYERS_PATH, 'w') as fp:
        json.dump({}, fp)


if __name__ == '__main__':
    player_add("test")
    player_add("tests")
    player_remove("tsest")
    player_join("tests", "o")
