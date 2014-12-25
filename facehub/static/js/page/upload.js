(function(){
    Dropzone.autoDiscover = false;
    $.get('/token',function(token){

        $('#upload-form').find('input[name="token"]').val(token);
        var myDropzone = new Dropzone("#upload-form");
        myDropzone.on("addedfile", function(file) {
            /* Maybe display some more file information on your page */
        });

    })
})();