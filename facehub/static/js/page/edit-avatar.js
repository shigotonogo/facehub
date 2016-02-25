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

    $('.raw-photo img').load(function(){
        var weight = $('.raw-photo img').width();
        var height = $('.raw-photo img').height();

        $('.raw-photo img').Jcrop({
            aspectRatio: 1,
            setSelect:   [ weight / 4, height / 2 - weight / 4, weight * 3 / 4, height / 2 + weight / 4],
            onChange: updatePreview,
            boxWidth: 740,
            boxHeight: 740
        });
    })

    $('#submit').click(cropSelected);
    $('#back').click(back);
})();