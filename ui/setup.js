//set the value of the input element with id storage-location to get_default_game_dir() from python

// start code
function setDefaultGameDir() {
    eel.get_default_game_dir()(function (result) {
        document.getElementById('storage-location').value = result;
    });
}
setDefaultGameDir();

function openFolderDialog() {
    eel.get_folder_dialog()(function (result) {
        document.getElementById('storage-location').value = result;
    });
}

// end code
