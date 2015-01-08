(function(){
    Dropzone.autoDiscover = false;
    $.get('/token',function(token){
        console.log(token)

        $('#upload-form').find('input[name="token"]').val(token);
        var myDropzone = new Dropzone("#upload-form");
        myDropzone.on("success", function(data) {
           console.log(arguments)
        });

    })
})();