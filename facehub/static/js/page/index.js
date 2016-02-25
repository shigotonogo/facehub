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

    var showBirthdayUsers = function (data) {
        var ractive = new Ractive({
            el: '#birthday',
            template: '#birthday-template',
            data: data
        })
    }

    var showUsers =  function (data){
        var ractive = new Ractive({
            el: 'members',
            template: '#users-template',
            data: data
        });
    }

    var toggleActionLink = function(data){
        var users = data.users;
        var currentUserEmail = decodeURIComponent(data.current_user);

        var exsiting = _.find(users, function(user){
            return user.email == currentUserEmail && user.photo && user.avatar
        });
        
        if (exsiting) {
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

    $.ajax({
        url: '/api/birthday-users',
        dataType: 'json',
        success: function(data) {
            if (data.users.length > 4) {
                data.users = data.users.slice(0, 4)
            }
            showBirthdayUsers(data);
        }
    })
})();
