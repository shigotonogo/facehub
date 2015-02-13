(function($) {
    function center(element){
        var width = $(window).width() - element.width();
        width = width >= 0 ? width : 0;
        var height = $(window).height() - element.height();
        height = height >= 0 ? height : 0;
        element.css({
            'left' : width/2,
            'top'  : height/2 + $(window).scrollTop()
        });
    }

    $.fn.mask = function(params) {
        params = $.extend({
            opacity: 0.5
        }, params);

        if ($(this).hasClass('masked')) {
            return;
        }
        var element = $(this);
        if (element.css("position") === "static") {
            element.addClass("masked-relative");
        }
        var maskEl = $('<div class="loadmask"></div>').css('opacity', params.opacity);
        element.addClass("masked").append(maskEl);
        var loadingEl = $('<div class="loading"></div>').appendTo(element);

        loadingEl.css({
            'top': params.top || (element.height() / 2 - (loadingEl.height() + parseInt(loadingEl.css("padding-top"),10) + parseInt(loadingEl.css("padding-bottom"),10)) / 2),
            'left': params.left || (element.width() / 2 - (loadingEl.width() + parseInt(loadingEl.css("padding-left"),10) + parseInt(loadingEl.css("padding-right"),10)) / 2)
        });

        if(params.center){
            center(loadingEl);
        }
        return this;
    };

    $.fn.unmask = function() {
        var element = $(this);
        element.find(".loading, .loadmask").remove();
        element.removeClass("masked masked-relative");

        return this;
    };

    var mask;
    $.showGlobalMask = function(){
        mask = $('<div class="modal-mask"></div>');
        $(document.body).append(mask);
        mask.css({
            width : $(window).width(),
            height : $(document.body).height()
        });
    };
    $.hideGlobalMask = function(){
        mask.remove();
    };
})($);