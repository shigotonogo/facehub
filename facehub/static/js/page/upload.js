(function() {
    Dropzone.autoDiscover = false;
    var myDropzone = new Dropzone("#upload-form");
    myDropzone.on("success", function(file,id) {
        window.location.href = "/photo"
    });
})();