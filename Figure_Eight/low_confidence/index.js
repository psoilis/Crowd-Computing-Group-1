require(['jquery-noconflict'], function($) {
    //Ensure MooTools is where it must be
    Window.implement('$', function(el, nc){
        return document.id(el, nc, this.document);
    });

    var $ = window.jQuery;

    $(window).load(function() {
        $('.avatar').each(function() {
            if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0 ) {
                this.src = 'https://storage.googleapis.com/crowd-computing-cdn-bucket/img/default.jpg';
            }
        });
    });
});