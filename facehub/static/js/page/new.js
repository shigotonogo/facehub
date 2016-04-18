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
        $('.profile-detail .new').each(function(){
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
        userSort.new_users = order === 'asc' ? _.sortBy(data.new_users, sortField) : _.sortBy(data.new_users, sortField).reverse();

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

    var capitalizeFirstLetter = function(string) {
        var reg = /^[a-z]/;
        if (reg.test(string)){
            return string.charAt(0).toUpperCase() + string.slice(1);
        }
        return string;
    }

    var addPinYinName = function(users){
        for(index in users) {
            users[index].pinYinName = capitalizeFirstLetter(pinyin.getFullChars(users[index].name));
        }
        return users
    }

    var userData = {};
    var list_view_cookie = $.cookie('_list_view_') || 'card';
    $.ajax({
        url: '/api/users',
        dataType: 'json',
        success: function(data) {
            data.users = addPinYinName(data.new_users);
            
            if(list_view_cookie === 'card'){
                showUsers(data, 'created_at', 'desc', '#card-template');
            }else{
                showUsers(data, 'pinYinName ', 'asc', '#list-template');
            }

            userData.new_users = data.new_users;

            toggleActionLink(data);
        }
    })
    $('.btn-group .list').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'pinYinName ', 'asc', '#list-template');

        $.cookie('_list_view_', 'list');
    });
    $('.btn-group .card').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'created_at', 'desc', '#card-template');

        $.cookie('_list_view_', 'card');
    });

     $('.btn-group .top-button').removeClass('active').siblings('.' + list_view_cookie).addClass('active');

})();
