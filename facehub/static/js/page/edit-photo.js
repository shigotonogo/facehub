(function() {
    var updatePreview = function(coordinate) {
        $('.preview img').data('coordinate', coordinate);
        $('.preview img').hide();

    };

    var cropSelected = function() {
        var coordinate = $('.preview img').data('coordinate');
        coordinate.src = $('.preview img').attr('src');
        coordinate.image_type = $("#image-type").val();

        $('.mask').show();

        $.ajax({
            type: "POST",
            url: '/crop',
            data: coordinate,
            success: nextStep,
            complete: hideMask
        });
    };

    var hideMask = function(){
        $('.mask').hide();
    };

    var nextStep = function() {
        window.location="/avatar"
    };
    
    $('.raw-photo img').Jcrop({
        aspectRatio: 3 / 4,
        onChange: updatePreview
    });
    $('#submit').click(cropSelected);
})();