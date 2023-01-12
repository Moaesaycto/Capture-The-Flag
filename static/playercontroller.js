window.onload = function() {
    refresh_players();
    refresh_options();
};

var player_list = new Array;

function refresh_players() {
    list = document.getElementById('player-list').innerHTML = "";
    fetch(`${window.origin}/player/get`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => display_players(json));
}

function display_players(players) {
    player_list = [];
    for (let i = 0; i < Object.keys(players).length; i++) {
        player_list.push(Object.keys(players)[i]);
        var orange = (players[Object.keys(players)[i]]['team'] == 'o' ? " checked" : "")
        var yellow = (players[Object.keys(players)[i]]['team'] == 'y' ? " checked" : "")
        var remove = (players[Object.keys(players)[i]]['team'] == '' ? " checked" : "")
    
        document.getElementById('player-list').innerHTML += `
        <div class="player" id="player` + i.toString() + `">
            <b>` + Object.keys(players)[i] + `</b>
            <div class="player-options">
                <label>
                    <input type="radio" name="player` + Object.keys(players)[i] + `" id="orange` + Object.keys(players)[i] +`" value="o" class="checklist"` + orange + `>
                    Orange
                </label>
                <label>
                    <input type="radio" name="player` + Object.keys(players)[i] + `" id="yellow` + Object.keys(players)[i] +`" value="y" class="checklist"` + yellow + `>
                    Yellow
                </label>
                <label>
                    <input type="radio" name="player` + Object.keys(players)[i] + `" id="delete` + Object.keys(players)[i] +`" value="" class="checklist"` + remove + `>
                    Delete
                </label>
            </div>
        </div>`;
    }
}


function refresh_options() {
    fetch(`${window.origin}/game/get-stats`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => display_options(json));
}

function display_options(json) {
    document.getElementById('grace-period').value = json['grace_period_time'];
    document.getElementById('commando-period').value = json['commando_period_time'];
    document.getElementById('informed-period').value = json['informed_period_time'];
}

function update_options() {
    request = {
        'grace_period_time': parseInt(document.getElementById('grace-period').value),
        'commando_period_time': parseInt(document.getElementById('commando-period').value),
        'informed_period_time': parseInt(document.getElementById('informed-period').value)
    };

    fetch(`${window.origin}/game/set-stats`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(request),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });

    refresh_options();
}

function update_players() {
    request = {};
    for (var i = 0; i < player_list.length; i++) {
        request[player_list[i]] = document.querySelector('input[name = "player' + player_list[i] + '"]:checked').value
    }
    list = document.getElementById('player-list').innerHTML = "";
    fetch(`${window.origin}/player/update`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(request),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });

    refresh_players();
}

function start() {
    fetch(`${window.origin}/game/start`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}


function restart() {
    fetch(`${window.origin}/game/restart`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}

function pause() {
    fetch(`${window.origin}/game/pause`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}

function play() {
    fetch(`${window.origin}/game/play`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}


function skip() {
    fetch(`${window.origin}/game/skip`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}


function previous() {
    fetch(`${window.origin}/game/previous`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}


function restart_section() {
    fetch(`${window.origin}/game/restart-section`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}


function add_five() {
    fetch(`${window.origin}/game/add-five`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}

function hard_reset() {
    fetch(`${window.origin}/game/hard-reset`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}