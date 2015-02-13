(function() {
    var updatePreview = function(coordinate) {
        $('.preview img').data('coordinate', coordinate);
        $('.preview img').hide();

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