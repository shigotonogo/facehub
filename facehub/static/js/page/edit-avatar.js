(function() {
    var updatePreview = function(coordinate) {
        $('.raw-photo img').data('coordinate', coordinate);
        $('.preview img').hide();
    };

    var cropSelected = function() {
        var coordinate = $('.raw-photo img').data('coordinate');
        coordinate.src = $('.raw-photo img').attr('src');
        coordinate.image_width = $('.raw-photo img').width();
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
        var id = $('#user-id').val();
        window.location="/profile"
    };

    $('.raw-photo img').load(function(){
        var width = $('.raw-photo img:visible').width();
        var height = $('.raw-photo img:visible').height();

        $('.raw-photo img').Jcrop({
            aspectRatio: 1,
            setSelect:   [ width / 4, height / 2 - width / 4, width * 3 / 4, height / 2 + width / 4],
            onChange: updatePreview,
            boxWidth: 740,
            boxHeight: 740
        });
    })

    $('#submit').click(cropSelected);
})();