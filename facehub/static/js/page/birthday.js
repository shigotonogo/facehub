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
        var dataId = $(src.currentTarget).data('user-id') || $(src.currentTarget).closest('tr').data('user-id'); 
        $.ajax({
            url: '/api/users/' + dataId,
            dataType: 'json',
            success: popupCurrent
        });
    });

    var showUsers =  function (data, sortField, order, template){
        var userSort = {};
        userSort.birthday_users = order === 'asc' ? _.sortBy(data.birthday_users, sortField) : _.sortBy(data.birthday_users, sortField).reverse();

        var ractive = new Ractive({
            el: '#members',
            template: template,
            data: userSort
        });
    }

    var toggleActionLink = function(data){
        var users = data.users;
        var currentUserEmail = decodeURIComponent(data.current_user);

        var exsiting = _.find(users, function(user){
            return user.email == currentUserEmail && user.photo && user.avatar
        });
        
        if (exsiting) {
            $(".edit-profile").removeClass("hidden").prepend("<img src='" + exsiting.avatar + "' alt='" + exsiting.name + "' width='36'>");
        }else{
            $(".new-profile").removeClass("hidden");
        }
    }

    var showCrown = function(data){
        var users = data.birthday_users;
        _.find(users, function(user){
            $('#members .profile[data-user-id='+ user.id +']').addClass("crown");
        });
    }

    var userData = {};
    $.ajax({
        url: '/api/users',
        dataType: 'json',
        success: function(data) {
            showUsers(data, 'created_at', 'desc', '#card-template');
            showCrown(data);

            userData.birthday_users = data.birthday_users;

            toggleActionLink(data);
        }
    })
    $('.btn-group .list').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'name', 'asc', '#list-template');
        showCrown(userData);
    });
    $('.btn-group .card').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'created_at', 'desc', '#card-template');
        showCrown(userData);
    });
})();
