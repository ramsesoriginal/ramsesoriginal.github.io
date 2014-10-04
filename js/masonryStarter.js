var $container = $('main');
  var em = parseFloat( $container.css('font-size') );
  $container.masonry({
    columnWidth: 5 * em,
    itemSelector: 'article'
  });