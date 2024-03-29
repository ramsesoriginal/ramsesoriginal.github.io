document.initialLayout = false;

$(document).ready(function() {
	if (document.enableMasonry) {
		var container = document.querySelector('main');
		imagesLoaded( container, function() {
			var mq = window.matchMedia("(min-width: 1000px)");
			mq.addListener(WidthChange);
			WidthChange(mq);
		});
	}
	function WidthChange(mq) {
		var $container = $('main > .wrapper');
		var em = parseFloat( $container.css('font-size') );
		if (mq.matches) {
			document.masonryActive=true;
			// window width is at least 1000px
			  $container.masonry({
			    columnWidth: 5 * em,
			    itemSelector: 'article',
			    transitionDuration: 0
			  });
			  $container.imagesLoaded().always(function() {
					 $container.masonry();
				}
			  );
		}
		else {
			document.masonryActive=false;
			// window width is less than 1000px
			$container.masonry( 'destroy' );
		}

	}
});

