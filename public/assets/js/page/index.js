(function(){
    $.ajax({
      url: '/users',
      success: function(data){
        console.log(data)
        var ractive = new Ractive({
          el: 'members',

          template: '#template',

          data: data
        });
      },
      dataType:'json'
    });
    
})();
