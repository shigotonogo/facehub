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
    
    $('.raw-photo img').load(function(){
        var weight = $('.raw-photo img:visible').width();
        var height = $('.raw-photo img:visible').height();

        $('.raw-photo img').Jcrop({
            aspectRatio: 3 / 4,
            setSelect:   [ weight / 4, height / 2 - weight / 3, weight *3 / 4, height / 2 + weight / 3],
            onChange: updatePreview,
            boxWidth: 740,
            boxHeight: 740
        });
    })
    
    $('#submit').click(cropSelected);
})();