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

    var back = function() {
        window.location="/photo"
    };
 
    var nextStep = function() {
        var id = $('#user-id').val();
        window.location="/profile"
    };
    
    $('.raw-photo img').Jcrop({
        aspectRatio: 1,
        onChange: updatePreview
    });
    $('#submit').click(cropSelected);
    $('#back').click(back);
})();