(function(){
    var oForm = $('#loginForm');
    var locked = false;
    oForm.show().submit(function(e){
        e.preventDefault();
        if($('#user').val() === "") {
            $(".email").hide();
            $(".empty-email").show();
            return;
        }
        if(!locked){
            locked = true;
            $('.submit').val('请稍候...');
            $.post($(this).attr('action'), {
                user : $('#user').val() + $('.email-suffix').text()
            }, function(){
                locked = false;
                $('.submit').val('立即加入');
                $('.after-register').show();
                oForm.hide();

                $('.re-register').off('click').on('click', function(){
                    $('.email-address input').val("");
                    oForm.show();
                    $('.after-register').hide();
                });
            });
        }
        
    });

    var count = function(){
        $.ajax({
            url: '/api/users_count',
            dataType: 'json',
            success: function(data) {
                $('#count').text(data['count']);
            }
        });
    };
    count();

    setInterval(count, 60000);

})();