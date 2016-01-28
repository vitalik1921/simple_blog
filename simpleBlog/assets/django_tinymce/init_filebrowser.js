function tinyDjangoBrowser(field_name, url, type, win) {
    var managerURL = window.location.toString()
            + '../../../posts/image/?type=' + type;

    tinyMCE.activeEditor.windowManager.open({
        file: managerURL,
        title: 'Кликните на эскиз нужной картинки',
        width: 800,
        height: 450,
        resizable: 'yes',
        inline: 'yes',
        close_previous: 'no',
        popup_css : false
    }, {
        window: win,
        input: field_name
    });

    return false;
}