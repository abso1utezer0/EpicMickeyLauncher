// change page method - takes a page name and replaces the contents of the div with the content
// id with the contents of the html file with the same name as the page name
function changePage(pageName) {
    var pageContent = document.getElementById('content');
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/main_pages/' + pageName + '.html', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            pageContent.innerHTML = xhr.responseText;
        }
    };

    xhr.send();
    // wait until the page is loaded before running the page's js
    xhr.onload = function () {

        // run page's js
        if (pageName === 'games') {
            getGames();
        }
    }
}

function launchGame(gameID) {
    eel.launch_game(gameID)
}

let games = {};

function getGames() {
    eel.get_games()(function (result) {
        games = result;
        games_uids = Object.keys(games);
        console.log(games);
        var gameList = document.getElementById('games-list');
        // for game in games:
        for (var i = 0; i < games_uids.length; i++) {
            var gameUID = games_uids[i];
            var game = games[gameUID];
            var gameItem = document.createElement('div');
            gameItem.className = 'game-listing';
            gameItem.id = 'game-item-' + gameUID;
            gameItem.innerHTML = '<p class="game-title">' + game.name + '</p><div class="game-item-launch joined-button"><button class="launch-button" onclick="launchGame(\'' + gameUID + '\')">Launch</button><button onclick="openLaunchDropdown()">˅</button></div>';
            // set background image to assets/banners/[game.id].png, make it semi-transparent
            gameItem.style.backgroundImage = 'url(assets/banners/' + game.id + '.png)';
            gameItem.style.backgroundSize = 'cover';
            gameItem.style.backgroundPosition = 'center';
            gameItem.style.backgroundBlendMode = 'multiply';
            gameItem.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
            // blur the background only
            gameItem.style.backdropFilter = 'blur(100px)';


            // add game item to games list
            gameList.appendChild(gameItem);
        }
    });
}