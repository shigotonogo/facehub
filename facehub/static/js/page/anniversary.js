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
        $('.profile-detail .birthday').each(function(){
            $(this).text($(this).text().replace(/^\d{4}/, '****'));
        });
    };

    $('#members').delegate('.profile-link', 'click', function(src) {
        var dataId = $(src.currentTarget).data('user-id') || $(src.currentTarget).closest('tr').find('.profile').data('user-id'); 
        $.ajax({
            url: '/api/users/' + dataId,
            dataType: 'json',
            success: popupCurrent
        });
    });

    var showUsers =  function (data, sortField, order, template){
        var userSort = {};
        userSort.anniversary_users = order === 'asc' ? _.sortBy(data.anniversary_users, sortField) : _.sortBy(data.anniversary_users, sortField).reverse();

        var ractive = new Ractive({
            el: '#members',
            template: template,
            data: userSort
        });
    }

    var toggleActionLink = function(data){
        var users = data.users;
        var currentUserEmail = decodeURIComponent(data.current_user_email);

        var exsiting = _.find(users, function(user){
            return user.email == currentUserEmail && user.photo && user.avatar
        });
        
        if (exsiting) {
            $(".edit-profile").removeClass("hidden").prepend("<img src='" + exsiting.avatar + "' alt='" + exsiting.name + "' width='36'>");
        }else{
            $(".new-profile").removeClass("hidden");
        }
    }

    var showBadge = function(data){
        var users = data.anniversary_users;
        _.find(users, function(user){
            anni = (new Date).getFullYear() - user.onboard.split("-")[0]
           $('#members .profile[data-user-id='+ user.id +']').addClass("anni").attr('data-anni', anni);
        });
    }

    var addPinYinName = function(users){
        for(index in users) {
            users[index].pinyYinName = pinyin.getFullChars(users[index].name);
        }
        return users
    }

    var userData = {};
    var list_view_cookie = $.cookie('_list_view_') || 'card';
    $.ajax({
        url: '/api/users',
        dataType: 'json',
        success: function(data) {
            data.users = addPinYinName(data.anniversary_users);

            if($.cookie('_list_view_') === 'card'){
                showUsers(data, 'created_at', 'desc', '#card-template');
            }else{
                showUsers(data, 'pinyYinName', 'asc', '#list-template');
            }
            showBadge(data);

            userData.anniversary_users = data.anniversary_users;

            toggleActionLink(data);
        }
    })
    $('.btn-group .list').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'pinyYinName', 'asc', '#list-template');
        showBadge(userData);

        $.cookie('_list_view_', 'list');
    });
    $('.btn-group .card').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'created_at', 'desc', '#card-template');
        showBadge(userData);

        $.cookie('_list_view_', 'card');
    });

    $('.btn-group .top-button').removeClass('active').siblings('.' + list_view_cookie).addClass('active');

})();
