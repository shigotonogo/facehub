(function(){
  var popupCurrent = function(user_data) {
    var current = new Ractive({template: $('#current-template').text() , data: user_data});
    $.magnificPopup.open({
      items:[{src: $(current.toHTML()), type: 'inline'}]
    });
  };

  $('#members').delegate('.profile', 'click', function(src){
    console.log(src.currentTarget);
    $.ajax({
      url: '/api/users/'+$(src.currentTarget).data('user-id'),
      dataType: 'json',
      success: popupCurrent
    });
  });

  $.ajax({
    url: '/api/users',
    dataType:'json',
    success: function(data){
      var ractive = new Ractive({el: 'members', template: '#template', data: data });
    }
  });
})();