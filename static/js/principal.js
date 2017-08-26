$(document).ready(function() {
    setTimeout(function() {
        $('.message').fadeOut('slow');
    }, 20000);

    // delete message
    $('.del-msg').bind('click',function(){
        $('.del-msg').parent().attr('style', 'display:none;');
    });

	$('.datepicker').datepicker({
      changeMonth: true,
      changeYear: true
    });

    $('#confirm-delete').on('show.bs.modal', function(e) {
		$(this).find('.btn-ok').attr('href', $(e.relatedTarget).data('href'));
	});

});
