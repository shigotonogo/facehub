(function() {
    var updatePreview = function(coordinate) {
        $('.preview').removeClass('blank');
        var rx = 300 / coordinate.w;
        var ry = 400 / coordinate.h;
        $('.preview img').css({
            width: Math.round(rx * 680) + 'px',
            // height: Math.round(ry * 370) + 'px',
            marginLeft: '-' + Math.round(rx * coordinate.x) + 'px',
            marginTop: '-' + Math.round(ry * coordinate.y) + 'px',
        });
        $('.preview img').data('coordinate', coordinate)
    };

    var cropSelected = function() {
        var coordinate = $('.preview img').data('coordinate');
        coordinate.src = $('.preview img').attr('src');
        $.ajax({
            type: "POST",
            url: '/edit',
            data: coordinate,
            success: nextStep,
        });
    };
 
    var nextStep = function() {
        // window.location='/edit/2'
    }
    
    $('.raw-photo img').Jcrop({
        aspectRatio: 3 / 4,
        onChange: updatePreview
    });
    $('#submit').click(cropSelected);
})();