(function() {
    var popupCurrent = function(user_data) {
        var current = new Ractive({
            template: $('#current-template').text(),
            data: user_data
        });
        $.magnificPopup.open({
            items: [{
                src: $(current.toHTML()),
                type: 'inline'
            }],
            closeMarkup: '<div class="close-bg"><button title="%title%" type="button" class="mfp-close">&times;</button></div>'
        });
    };

    $('#members').delegate('.profile', 'click', function(src) {
        $.ajax({
            url: '/api/users/' + $(src.currentTarget).data('user-id'),
            dataType: 'json',
            success: popupCurrent
        });
    });

    var showUsers =  function (data){
        var ractive = new Ractive({
            el: 'members',
            template: '#template',
            data: data
        });
    }

    var toggleActionLink = function(data){
        var users = data.users;
        var currentUserEmail = decodeURIComponent(data.current_user);

        var existing = _.find(users, function(user){
            return user.email == currentUserEmail
        });
        
        if (existing) {
            $(".edit-profile").removeClass("hidden");
        }else{
            $(".new-profile").removeClass("hidden");
        }
    }

    $.ajax({
        url: '/api/users',
        dataType: 'json',
        success: function(data) {
            showUsers(data);
            toggleActionLink(data);
        }
    });
})();
