import requests

GLOBAL_PATH = "https://discord.com/api/v9/channels/1062757092005519460/messages"
ORANGE_PATH = "https://discord.com/api/v9/channels/1062756743324647485/messages"
YELLOW_PATH = "https://discord.com/api/v9/channels/1062756974195920967/messages"

HEADER = {
    'authorization': "MTA2MTE3MjIyNTUzNDg3MzYwMA.GX8Sag.qhiMtxmpxhQw5gBRYRTbrsMjnTxY4XYXrjZJpU"
}


def send_global(message): r = requests.post(GLOBAL_PATH, data={"content": message}, headers=HEADER)
def send_orange(message): r = requests.post(ORANGE_PATH, data={"content": message}, headers=HEADER)
def send_yellow(message): r = requests.post(YELLOW_PATH, data={"content": message}, headers=HEADER)


def global_start(): send_global("**The game has begun!**\n\nRemember to read the rules and register your team's flag _before_ the grace period is over!\n\n\n---")

def global_play(): send_global("**The game has resumed!**\n\nThe timer has started again.")

def global_flag_error(): send_global("**Grace period is extended by one minute.**\n\nNot all teams have registered their flags. Both teams have an additional minute to do so. Grace period rules are still active.\n\n\n---")

def global_commando(): send_global("**The grace period is over!**\n\nThe commando period has begun, which means you can be caught. This is the time you should use to try to locate the opposition's flag location.\n\n\n---")

def global_informed(): send_global("**The map has been revealed!**\n\nThe informed period has begun, which means you can now access the opposition's flag location. You can do this on the game's control panel.\n\n\n---")

def global_end_general(): send_global("**The game has finished!**\n\nThe game has concluded. This means that a team has obtained their opposition's flag, you have run out of time or some other reason. Report back to the peak of the hill.\n\n\n---")

def global_end_orange_win(): send_global("**The Orange team has declared victory!**\n\nThis means that a team has obtained their opposition's flag, you have run out of time or some other reason. Report back to the peak of the hill.\n\n\n---")

def global_end_yellow_win(): send_global("**The Yellow team has declared victory!**\n\nThis means that a team has obtained their opposition's flag, you have run out of time or some other reason. Report back to the peak of the hill.\n\n\n---")

def global_end_draw(): send_global("**The game has run out of time!**\n\nThis means neither team has captured the flag in time. Report back to the meeting point.\n\n\n---")

def global_pause(): send_global("**The game has been paused.**\n\nThe game will continue after everything has been resolved. Stay tuned for further information.\n\n\n---")

def global_add_five(): send_global("**Five minutes has been added.**\n\nFive minutes has been added to the current section.\n\n\n---")

def global_timeout(): send_global("**A timeout has been reported!**\n\nReport to the global general channel for more information.\n\n\n---")

def global_declare_victory(team): send_global("**The " + team + " team has reported their victory!**\n\nReport to the meeting point.\n\n\n---")


def orange_flag_registered(): send_orange("**Flag successfully registered!**\n\nSomeone on the Orange team has registered the flag position. You can register a new position as long as you are still in the grace period.\n\n\n---")

def orange_notify_capture(): send_orange("**Someone has your flag!**\n\nA player on your team has reported your flag as missing!\n\n\n---")

def orange_notify_return(): send_orange("**Your flag has been returned!**\n\nA player has reported that your flag has been returned!\n\n\n---")

def orange_notify_opposition_capture(): send_orange("**Your team has the opposition's flag!**\n\nA player from your team has taken the opposition's flag! Make sure to help them as they make their way back to your base.\n\n\n---")

def orange_notify_opposition_return(): send_orange("**Opposition's flag has been taken back.**\n\nThe opposition has retrieved their flag from your possession.\n\n\n---")

def orange_return_to_base(): send_orange("**Return to base!**\n\nSomeone in your team has requested that everybody returns to the base! Hurry, it could be important!\n\n\n---")


def yellow_flag_registered(): send_yellow("**Flag successfully registered!**\n\nSomeone on the Orange team has registered the flag position. You can register a new position as long as you are still in the grace period.\n\n\n---")

def yellow_notify_capture(): send_yellow("**Someone has your flag!**\n\nA player on your team has reported your flag as missing!\n\n\n---")

def yellow_notify_return(): send_yellow("**Flag returned!**\n\nA player has reported that your flag has been returned!\n\n\n---")

def yellow_notify_opposition_capture(): send_yellow("**Your team has the opposition's flag!**\n\nA player from your team has taken the opposition's flag! Make sure to help them as they make their way back to your base.\n\n\n---")

def yellow_notify_opposition_return(): send_yellow("**Opposition's flag has been taken back.**\n\nThe opposition has retrieved their flag from your possession.\n\n\n---")

def yellow_return_to_base(): send_yellow("**Return to base!**\n\nSomeone in your team has requested that everybody returns to the base! Hurry, it could be important!\n\n\n---")
