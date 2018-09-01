(function($){
    $(function(){
        $('.sidenav').sidenav();
        $('.select').formSelect();
        $('.carousel').carousel();
        $('.parallax').parallax();
        $('.materialboxed').materialbox();
        $('.modal').modal();
        $('.scrollspy').scrollSpy();
        $('.dropdown-trigger').dropdown({
            hover: true
        });
        $('.fixed-action-btn').floatingActionButton();
    }); // end of document ready
})(jQuery); // end of jQuery name space