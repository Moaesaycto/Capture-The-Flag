fetch(`${window.origin}/player`, {
    method: "GET",
    credentials: "include",
    cache: "no-cache",
    headers: new Headers({
        "content-type": "application/json"
    })
}).then(response => response.json()).then(json => setup(json))


function setup(json) {
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

function register_map() {
    fetch(`${window.origin}/player`, {
        method: "GET",
        credentials: "include",
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => send_map_request(json));
}


function send_map_request(json) {
    if (json['team'] == null) {
        json['team'] = "";
    }

    var slider = document.getElementById("slider");
    request = {
        "location": slider.value,
        "team": json['team']
    }

    console.log(request);

    fetch(`${window.origin}/map/set`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(request),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()).then(json => update_map_form(json));
}

function update_map_form(json) {
    var response_box = document.getElementById("response");

    if (!json['status']) {
        response_box.innerHTML = `<br>
        <div class="team-name" id="error">
            An error occurred while placing the map location. You must join a team before you can do this action.
        </div>`
        document.getElementById("error").style.backgroundColor = "rgb(216, 94, 94)";
        return;
    }

    var team_name = (json['team'] == 'o' ? "orange" : "yellow" )
    response_box.innerHTML = `<br>
    <div class="team-name" id="error">
        Map location has been updated for the ` + team_name + ` team. You can change this at any time
    </div>`
    document.getElementById("error").style.backgroundColor = "rgb(125, 219, 106)";
}