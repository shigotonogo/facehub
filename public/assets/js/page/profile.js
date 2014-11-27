(function() {
    // $.get('/',function(data){

    // });
    //
    var ractive = new Ractive({
        el: 'info',

        template: '#template',

        data: {
            "id": 1,
            "name": "Yao Shaobo",
            "photo": "http://uxhongkong.com/interviews/img/people/thumb-alain-robillard-bastien.jpg",
            'mobile': 15502980060,
            'skype': 'dyw@gmail.com',
            'role': 'fe',
            'team': 'myfun',
            'email': 'dyw@thoughtworks.com'
        }
    });
})();
