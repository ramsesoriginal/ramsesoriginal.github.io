$.getJSON( "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=5c614dfbc3ba968e600ef21b0cebb014&user_id=31292129%40N00&per_page=1&page=1&format=json&nojsoncallback=1", function( data ) {
  var photo = data.photos.photo[0];
  var linkStart = '<a href="https://www.flickr.com/photos/ramsesoriginal/'
  	+ photo.id 
  	+ '" title="'
  	+ photo.title
  	+ '">';
  var imgUrl = 'https://farm9.staticflickr.com/'
  	+ photo.server
  	+ '/'
  	+ photo.id 
  	+ '_'
  	+ photo.secret
  	+ '.jpg';
  var imgTag = '<img src="'
  	+ imgUrl
  	+ '" alt="'
  	+ photo.title
  	+ '" />';

  $("#flickrLink").html(
  	"Latest picture: " + linkStart + photo.title + "</a>"
  );

  $("#flickPic").html(
  	linkStart + imgTag + "</a>"
  );
});