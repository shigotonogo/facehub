(function (){
    function updatePreview(coordinate){
        $('.preview').removeClass('blank');
        var rx = 300 / coordinate.w;
        var ry = 400 / coordinate.h;

        $('.preview img').css({
            width: Math.round(rx * 740) + 'px',
            // height: Math.round(ry * 370) + 'px',
            marginLeft: '-' + Math.round(rx * coordinate.x) + 'px',
            marginTop: '-' + Math.round(ry * coordinate.y) + 'px',
        });
    };

    $('.raw-photo img').Jcrop({
        aspectRatio: 3/4,
        minSize: [300, 400],
        onChange: updatePreview,
        onSelect: updatePreview
    });
})();