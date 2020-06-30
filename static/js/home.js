$(function() {
	$('a').each(function() {
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
	});
});

$(document).ready(function() {
    var table = $('#table_id').DataTable({
        "scrollX": true
    });

    new $.fn.dataTable.Buttons( table, {
    	buttons: [{
    		text: 'New',
    		action: function ( e, dt, node, conf ) {
    			var str = window.location.href
				var n = str.lastIndexOf("/");
				var length = str.length;
				var substr = str.substring(n +1, length);
        		location.href = '/ramon/forms/new-' + substr;
        		console.log( 'new-' + substr  );
    		}
        }]
	});

	table.buttons( 0, null ).container().prependTo(
    	table.table().container()
	);
});