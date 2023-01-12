from flask import Flask, jsonify, request, make_response, render_template, session, redirect, url_for
import threading, webbrowser
import random
import player, game, arena, discord
import json, string

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdjkfh5s7uih98"
PORT = 5001
HOST = "127.0.0.1"

STRING_LENGTH = 8
SESSION_KEY_PATH = "resources/session_keys.json"

@app.route('/') 
def index(): return render_template('index.html')

@app.route('/map')
def view_map(): return render_template('map.html')


@app.route('/home')
def home(): return render_template('index.html')


@app.route('/rules')
def rules(): return render_template('rules.html')


@app.route('/controller')
def controller(): return render_template('controller.html')


@app.route('/player-controller')
def player_controller(): return render_template('player_controller.html')


@app.route('/player', methods=['GET'])
def get_session_name():
     try: 
          if not _valid_session(): return make_response(jsonify({'status': False}), 200)
          data = player.player_info(session['name'])
     except: data = {'status': False}
     return make_response(jsonify(data), 200)


@app.route('/player/add', methods=['POST'])
def player_add():
     req = request.get_json()
     session['session_key'] = _generate_session_key(STRING_LENGTH)
     session['name'] = req['name']
     return make_response(jsonify({"result": player.player_add(req['name'], session['session_key'])}), 200)


@app.route('/player/remove', methods=['POST'])
def player_remove():
     req = request.get_json()
     return make_response(jsonify({"result": player.player_remove(req['name'])}), 200)


@app.route('/player/get', methods=['GET'])
def player_get():
     try: data = player.player_get()
     except: data = {'status': False}
     return make_response(jsonify(data), 200)


@app.route('/player/update', methods=['POST'])
def player_update():
     req = request.get_json()
     return make_response(jsonify({"result": player.player_update(req)}), 200)


@app.route('/player/info', methods=['POST', 'GET'])
def player_info():
     req = request.get_json()
     return make_response(jsonify({"result": player.player_info(req['name'])}), 200)
 

@app.route('/map/set', methods=['POST'])
def map_set():
     req = request.get_json()
     return make_response(jsonify(arena.set_map(req)), 200)


@app.route('/game/start', methods=['POST'])
def game_start():
     game.start()
     discord.global_start()
     return make_response(jsonify({}), 200)


@app.route('/game/play', methods=['POST'])
def game_play():
     game.play()
     discord.global_play()
     return make_response(jsonify({}), 200)


@app.route('/game/info', methods=['GET'])
def game_info():
     try: data = game.info()
     except: data = {'status': False}
     return make_response(jsonify(data), 200)


@app.route('/game/pause', methods=['POST'])
def game_pause():
     game.pause()
     discord.global_pause()
     return make_response(jsonify({}), 200)


@app.route('/game/restart', methods=['POST'])
def game_restart():
     game.restart()
     return make_response(jsonify({}), 200)


@app.route('/game/skip', methods=['POST'])
def game_skip():
     game.next_section()
     return make_response(jsonify({}), 200)


@app.route('/game/previous', methods=['POST'])
def game_prev():
     game.prev_section()
     return make_response(jsonify({}), 200)


@app.route('/game/add-five', methods=['POST'])
def game_add_five():
     game.add_five()
     discord.global_add_five()
     return make_response(jsonify({}), 200)


@app.route('/game/restart-section', methods=['POST'])
def game_restart_section():
     game.restart_section()
     return make_response(jsonify({}), 200)


@app.route('/game/hard-reset', methods=['POST'])
def game_hard_reset():
     game.game_reset()
     return make_response(jsonify({}), 200)


@app.route('/game/get-stats', methods=['GET'])
def game_get_stats():
     return make_response(jsonify(game.get_stats()), 200)


@app.route('/game/set-stats', methods=['POST'])
def game_set_stats():
     req = request.get_json()
     game.set_stats(req)
     return make_response(jsonify({}), 200)
     

@app.route('/player-controller/declare-victory', methods=['POST'])
def controller_declare_victory():
     req = request.get_json()
     game.pause()
     if req['team'] == 'o': team = 'Orange'
     elif req['team'] == 'y': team = 'Yellow'
     discord.global_declare_victory(team)
     return make_response(jsonify({}), 200)


@app.route('/player-controller/timeout', methods=['POST'])
def controller_timeout():
     discord.global_timeout()
     game.pause()
     return make_response(jsonify({}), 200)


@app.route('/player-controller/missing', methods=['POST'])
def controller_missing():
     req = request.get_json()
     if req['team'] == 'o':
          discord.orange_notify_capture()
          discord.yellow_notify_opposition_capture()
     elif req['team'] == 'y':
          discord.yellow_notify_capture()
          discord.orange_notify_opposition_capture()
     return make_response(jsonify({}), 200)


@app.route('/player-controller/returned', methods=['POST'])
def controller_return():
     req = request.get_json()
     if req['team'] == 'o':
          discord.orange_notify_return()
          discord.yellow_notify_opposition_return()
     elif req['team'] == 'y':
          discord.yellow_notify_return()
          discord.orange_notify_opposition_return()
     return make_response(jsonify({}), 200)


@app.route('/player-controller/summon', methods=['POST'])
def controller_summon():
     req = request.get_json()
     if req['team'] == 'o':
          discord.orange_return_to_base()

     elif req['team'] == 'y':
          discord.yellow_return_to_base()
     return make_response(jsonify({}), 200)


"""
Session helpers
"""

def _generate_session_key(length):
     with open(SESSION_KEY_PATH, 'r') as fp:
          data = json.load(fp)
          string = ''.join(random.choice("abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(length))
          while string in data['invalid_keys']:
               string = ''.join(random.choice("abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(length))
     return string


def _valid_session():
     with open(SESSION_KEY_PATH, 'r') as fp:
          data = json.load(fp)
          return session['session_key'] not in data['invalid_keys']




""" @app.route('/submit', methods=['POST'])
def submit():
     req = request.get_json()
     return make_response(jsonify(generate(req)), 200)
 """
if __name__ == '__main__':
    url = "http://{0}:{1}/".format(HOST, PORT)
    threading.Timer(0.1, lambda: webbrowser.open(url) ).start()
    app.run(host=HOST, port=PORT, debug=False)