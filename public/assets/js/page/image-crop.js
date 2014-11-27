(function() {
    $("#main-photo").Jcrop({
        onChange: showPreview,
        onSelect: showPreview,
        aspectRatio: 0.75
    });

    function showPreview(coords) {
        var rx = 300 / coords.w;
        var ry = 400 / coords.h;
        $('.preview').css({
            marginLeft: '-' + Math.round(rx * coords.x) + 'px',
            marginTop: '-' + Math.round(ry * coords.y) + 'px'
        });
    }
})();