(function(){
    $.get('/',function(data){
        var ractive = new Ractive({
          el: 'container',

          template: '#template',

          data: {
            'list' : [
                { "id": 1, "name": "Yao Shaobo", "photo":"http://uxhongkong.com/interviews/img/people/thumb-alain-robillard-bastien.jpg" },
                { "id": 2, "name": "Dong Yuwei", "photo":"http://uxhongkong.com/interviews/img/people/thumb-andrew-mayfield.jpg" },
                { "id": 1, "name": "Dou Yutao", "photo":"http://uxhongkong.com/interviews/img/people/thumb-boon-yew-chew.jpg" },
                { "id": 2, "name": "Liu Liang", "photo":"http://uxhongkong.com/interviews/img/people/thumb-cornelius-rachieru.jpg" }
             ]
          }
        });
    });
})();
