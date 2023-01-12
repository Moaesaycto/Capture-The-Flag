import shutil, json
from PIL import Image, ImageDraw, ImageFont
import discord

MARK_RAD = 10

GAME_PATH = "resources/game.json"
CLEAN_MAP_PATH = "static/media/clean_map.png"
DISPLAY_MAP_PATH = "static/media/display_map.png"
CONTROLLER_PATH = "resources\controller.json"

def set_map(stats):
    with open(CONTROLLER_PATH, 'r') as fp:
        cntr = json.load(fp)
        if cntr['state'] != "grace": {"status": False, "team": stats['team']}

    with open(GAME_PATH, 'r') as fp:
        status = True
        data = json.load(fp)
        location = stats['location']
        location = location.split("|")
        coordinates = {"x": round(float(location[0])), "y": round(float(location[1]))}

    if stats['team'] == "o":
        data["orange_flag_position"] = coordinates
        data['orange_flag_placed'] = True
        discord.orange_flag_registered()

    elif stats['team'] == "y":
        data["yellow_flag_position"] = coordinates
        data['yellow_flag_placed'] = True
        discord.yellow_flag_registered()

    else: status = False

    with open(GAME_PATH, 'w') as fp: json.dump(data, fp)

    return {"status": status, "team": stats['team']}


def generate_flag_map():
    with open(GAME_PATH, 'r') as fp:
        data = json.load(fp)
        o1, o2 = data['orange_flag_position']['x'], data['orange_flag_position']['y']
        y1, y2 = data['yellow_flag_position']['x'], data['yellow_flag_position']['y']

    shutil.copyfile(CLEAN_MAP_PATH, DISPLAY_MAP_PATH)
    with Image.open(DISPLAY_MAP_PATH) as im:
        X_DIST = 0.96
        draw = ImageDraw.Draw(im)
        draw.ellipse((im.size[0]*o1/1600*X_DIST - MARK_RAD, im.size[1]*(1 - o2/1800) - MARK_RAD, im.size[0]*o1/1600*X_DIST + MARK_RAD, im.size[1]*(1 - o2/1800) + MARK_RAD), fill='orange', outline='black', width=3)
        font = ImageFont.truetype('resources\AvenirLTStd-Black.otf', 20)
        draw.text((im.size[0]*o1/1600*X_DIST , im.size[1]*(1 - o2/1800) - 45 - MARK_RAD), "Orange Flag\nLocation", font=font, fill='orange', outline='black', align="center")

        draw.ellipse((im.size[0]*y1/1600*X_DIST - MARK_RAD, im.size[1]*(1 - y2/1800) - MARK_RAD, im.size[0]*y1/1600*X_DIST + MARK_RAD, im.size[1]*(1 - y2/1800) + MARK_RAD), fill='yellow', outline='black', width=3)
        font = ImageFont.truetype('resources\AvenirLTStd-Black.otf', 20)
        draw.text((im.size[0]*y1/1600*X_DIST - 60, im.size[1]*(1 - y2/1800) - 45 - MARK_RAD), "Yellow Flag\nLocation", font=font, fill='yellow', outline='black', align="center")
        im.save(DISPLAY_MAP_PATH)


def hide_map():
    shutil.copyfile(CLEAN_MAP_PATH, DISPLAY_MAP_PATH)


def display_map():
    with open(GAME_PATH, 'r') as fp:
        game_data = json.load(fp)


if __name__ == '__main__':
    generate_flag_map()