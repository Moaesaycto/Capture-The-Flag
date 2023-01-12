function player_register() {
    var name = document.getElementById("name").value;
    if (name == "") return;

    request = {"name": name}

    fetch(`${window.origin}/player/add`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(request),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => form_update(json));

    location.reload();
}

function form_update(json) {
    if (json["result"]) {
        form = document.getElementById("name-form");
        form.remove();
    }
    else {
        document.getElementById("error").innerHTML = "Invalid name. Try a different one.";
    }
}

function load_session() {
    fetch(`${window.origin}/player`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => name_form_update(json));
}

function name_form_update(json) {
    console.log(json);
    if (!json['status']) {
        return;
    }
    var name_form = document.getElementById("name-form");
    document.getElementById("error").innerHTML = "You are playing as " + json['name'] + ". ";
    if (json['team'] == "y") {
        document.getElementById("error").innerHTML += "You are on the yellow team."
        document.getElementById("player-options").innerHTML += `<a href="player-controller"><button class="home-button">Register name</button></a>`;
    }
    else if (json['team'] == "o") {
        document.getElementById("error").innerHTML += "You are on the orange team."
        document.getElementById("player-options").innerHTML += `<a href="player-controller"><button class="home-button">Register name</button></a>`;
    }
    else {
        document.getElementById("error").innerHTML += "You have not been assigned a team yet."
    }
    document.getElementById("name").remove();
    document.getElementById("name-button").remove();
    name_form.innerHTML += `<button onclick="user_remove();" class="home-button">Leave Game</button>`;
}


function clear_session() {
    fetch(`${window.origin}/get-session-name`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => user_remove(json['name']));
}

function user_remove() {
    var player_info = {};
    fetch(`${window.origin}/player`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => delete_user(json));

}

function delete_user(player_json) {
    fetch(`${window.origin}/player/remove`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(player_json),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });

    location.reload();
}