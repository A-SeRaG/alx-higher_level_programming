//adds <li> element to a list when clicks on the tag DIV#add_item

$('DIV#add_item').click(function () {
	let element = '<li>Item</li>';
	$('UL.my_list').append(element);
});
