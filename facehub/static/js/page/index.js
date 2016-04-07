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
        var dataId = $(src.currentTarget).data('user-id') || $(src.currentTarget).closest('tr').find('.profile').data('user-id'); 
        $.ajax({
            url: '/api/users/' + dataId,
            dataType: 'json',
            success: popupCurrent
        });
    });

    var showBirthdayUsers = function (data) {
        var ractive = new Ractive({
            el: '.shou-xing-canvas',
            template: '#birthday-template',
            data: data
        })
    }

    var showAnniversaryUsers = function (data) {
        var ractive = new Ractive({
            el: '.anniversary-canvas',
            template: '#anniversary-template',
            data: data
        });
    }

    var showNewUsers = function (data) {
        var ractive = new Ractive({
            el: '.new-users-canvas',
            template: '#new-template',
            data: data
        })
    }


    var showUsers =  function (data, sortField, order, template){
        var userSort = {};
        userSort.users = order === 'asc' ? _.sortBy(data.users, sortField) : _.sortBy(data.users, sortField).reverse();

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

    var showBadge = function(data){
        var users = data.anniversary_users;
        _.find(users, function(user){
            anni = (new Date).getFullYear() - user.onboard.split("-")[0]
           $('#members .profile[data-user-id='+ user.id +']').addClass("anni").attr('data-anni', anni);
        });
    }

    var limit = function(data){
        if (data.length > 4) {
            data = data.slice(0, 4);
        }
        return data;
    }

    var userData = {};
    $.ajax({
        url: '/api/users',
        dataType: 'json',
        success: function(data) {
            showUsers(data, 'created_at', 'desc', '#card-template');
            showCrown(data);
            showBadge(data);

            userData.users = data.users;
            userData.birthday_users = data.birthday_users;
            userData.anniversary_users = data.anniversary_users;
            userData.new_users = data.new_users;

            data.birthday_users = limit(data.birthday_users);
            data.anniversary_users = limit(data.anniversary_users);
            data.new_users = limit(data.new_users);

            toggleActionLink(data);
            showAnniversaryUsers(data);
            showBirthdayUsers(data);
            showNewUsers(data);

            
        }
    })
    $('.btn-group .list').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'name', 'asc', '#list-template');
        showCrown(userData);
        showBadge(userData);
    });
    $('.btn-group .card').click(function(){
        $(this).addClass('active').siblings('.top-button').removeClass('active');
        showUsers(userData, 'created_at', 'desc', '#card-template');
        showCrown(userData);
        showBadge(userData);
    });

    var swiper = new Swiper('.swiper-container', {
            pagination: '.swiper-pagination',
            nextButton: '.swiper-button-next',
            prevButton: '.swiper-button-prev',
            slidesPerView: 1,
            paginationClickable: true,
            spaceBetween: 30,
            loop: false,
            //autoplay: 5000,
            autoplayDisableOnInteraction: false,
            mousewheelControl: true
        });
    

})();
