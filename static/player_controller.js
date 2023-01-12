var team = ""

fetch(`${window.origin}/player`, {
    method: "GET",
    credentials: "include",
    cache: "no-cache",
    headers: new Headers({
        "content-type": "application/json"
    })
}).then(response => response.json()).then(json => setup(json))


function setup(json) {
    team = json['team']
    var sign = document.getElementById("team-sign");
    if (json['team'] == "o") {
        sign.innerHTML = "You are on the orange team"
        sign.style.backgroundColor = "orange";
    }

    else if (json['team'] == "y") {
        sign.innerHTML = "You are on the yellow team"
        sign.style.backgroundColor = "yellow";
    }
}

function declare_victory() {
    fetch(`${window.origin}/player-controller/declare-victory`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({"team" : team}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}

function timeout() {
    fetch(`${window.origin}/player-controller/timeout`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({"team" : team}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}


function missing() {
    fetch(`${window.origin}/player-controller/missing`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({"team" : team}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}

function returned() {
    fetch(`${window.origin}/player-controller/returned`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({"team" : team}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}

function summon() {
    fetch(`${window.origin}/player-controller/summon`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({"team" : team}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    });
}