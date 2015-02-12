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
        coordinate.user_id = $('#user-id').val();
        coordinate.image_type = $("#image-type").val();

        $.ajax({
            type: "POST",
            url: '/crop',
            data: coordinate,
            success: nextStep,
        });
    };
 
    var nextStep = function() {
        var id = $('#user-id').val();
        window.location="/users/" + id + "/avatar/crop"
    }
    
    $('.raw-photo img').Jcrop({
        aspectRatio: 3 / 4,
        onChange: updatePreview
    });
    $('#submit').click(cropSelected);
})();