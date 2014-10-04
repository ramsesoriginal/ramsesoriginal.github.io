
var mq = window.matchMedia("(min-width: 1000px)");
mq.addListener(WidthChange);
WidthChange(mq);

function WidthChange(mq) {
	var $container = $('main');
	var em = parseFloat( $container.css('font-size') );
	if (mq.matches) {
		// window width is at least 1000px
		  $container.masonry({
		    columnWidth: 5 * em,
		    itemSelector: 'article'
		  });
	}
	else {
		// window width is less than 1000px
		$container.masonry( 'destroy' );
	}

}

