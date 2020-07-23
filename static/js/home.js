$(function() {
	$('a').each(function() {
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
	});
});

$(document).ready(function() {

    var table = $('#table_id').DataTable({
        "scrollX": true, 
        rowCallback: function(row, data, index){
        	if(data[status]==='Incomplete'){
        		$('td', row).css('background-color', '#ffcccc');
        	}
        	if(data[status]==='Ready for Review'){
        		$('td', row).css('background-color', '#d3f3dd');
        	}
        }
    });


    var str = window.location.href;
    var n = str.lastIndexOf("/");
    var substr = str.substring(n +1, str.length);

    // if (approveButton) {
    //     new $.fn.dataTable.Buttons( table, {
    //         buttons: [
    //             {
    //                 text: 'New',
    //                 action: function ( e, dt, node, conf ) {
    //                     location.href = '/ramon/forms/new-' + substr;
    //                 }
    //             },
    //             {
    //                 text: 'Approve All',
    //                 attr: {
    //                     id: 'approveButton'
    //                 }
    //             }
    //         ]
    //     });
    // } else {
    new $.fn.dataTable.Buttons( table, {
        buttons: [{
            text: 'New',
            action: function ( e, dt, node, conf ) {
                location.href = '/ramon/forms/new-' + substr;
            }
        }]
    });
    // }


	table.buttons( 0, null ).container().prependTo(
    	table.table().container()
	);


    // $('#approveButton').click(function() {
    //     console.log('approveButton clicked');
    //     $.ajax({
    //         type: 'POST',
    //         url: '/ramon/forms/' + substr,
    //         'data': {
    //             'approveButton': true,
    //             'csrfmiddlewaretoken': csrf,
    //         },
    //         success: function(data){
    //             $('#content').html(data);
    //         }
    //     });
    // });
});