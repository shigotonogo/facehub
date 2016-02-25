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

    $('#members').delegate('.profile-link', 'click', function(src) {
        var dataId = $(src.currentTarget).data('user-id') || $(src.currentTarget).closest('tr').data('user-id'); 
        $.ajax({
            url: '/api/users/' + dataId,
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

    var showAnniversaryUsers = function (data) {
        var ractive = new Ractive({
            el: '#anniversary',
            template: '#anniversary-template',
            data: data
        })
    }

    var showUsers =  function (data, template){
        data.users = _.sortBy(data.users, "created_at").reverse();
        var ractive = new Ractive({
            el: '#members',
            template: template,
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

    var userData;
    $.ajax({
        url: '/api/users',
        dataType: 'json',
        success: function(data) {
            userData = data;
            showUsers(data, '#card-template');

            if (data.birthday_users.length > 4) {
                data.birthday_users = data.birthday_users.slice(0, 4)
            }

            if (data.anniversary_users.length > 4) {
                data.anniversary_users = data.birthday_users.slice(0, 4)
            }

            toggleActionLink(data);
            showAnniversaryUsers(data);
            showBirthdayUsers(data);
        }
    })
    $('.btn-group .list').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, '#list-template');
    });
    $('.btn-group .card').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, '#card-template');
    });
})();
