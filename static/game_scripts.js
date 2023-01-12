game_state();

function game_state() {
    fetch(`${window.origin}/game/info`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => display_game_state(json));
}

function display_game_state(json) {
    if (json['stopped']) {
        document.getElementById('game-status').innerHTML = 'Game is inactive.';
        document.getElementById('timer').innerHTML = '--:--';
    }

    else if (json['paused']) {
        document.getElementById('game-status').innerHTML = 'Game is paused.';
        display_time(json['time']);
    }

    else {
        document.getElementById('game-status').innerHTML = json['state'];
        display_time(json['time']);
        run_timer(json['time']);

        if (json['state'] == "informed") {
            var map = document.getElementById("map");
            map.innerHTML = "";
            map.innerHTML = `<img src="../static/media/display_map.png">`;
        }
    }
}

function display_time(time) {
    document.getElementById('timer').innerHTML = Math.round((time - (time % 60))/60).toString() + "m " + (time % 60).toString() + "s";
}

function run_timer(time) {
    var intervalId = window.setInterval(function(){
        display_time(time);
        if (time == 0) {
            clearInterval(intervalId);
            game_state();
        }
        time--;
      }, 1000);
}