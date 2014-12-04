(function (){
    function updatePreview(coordinate){
        $('.preview').removeClass('blank');
        var src = $('.preview').find('img').attr('src');
        $("form input[name=image]").val(src);
        $("form input[name=x]").val(coordinate.x);
        $("form input[name=y]").val(coordinate.y);
        $("form input[name=width]").val(coordinate.w);
        $("form input[name=height]").val(coordinate.h);

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