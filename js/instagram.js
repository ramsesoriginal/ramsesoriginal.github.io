$(document).ready(function() {
	var accessToken = '197139508.8dd0e97.9ccedb18ab1d4e298a69b139e15aaefa';
	if (document.location.hostname == "localhost") {
		accessToken = '197139508.de7d149.9ae6f841ed2c4ef29df155cc87a91598';
	}
	var userID = 197139508;
	$.getJSON( 'https://api.instagram.com/v1/users/' + userID + '/media/recent?access_token=' +  accessToken + '&count=1&callback=?', function( data ) {
		var photo = data.data[0];
		var linkStart = '<a href="'
			+ photo.link
			+ '" title="'
	  		+ photo.caption.text
			+ '">';
		var imgUrl = photo.images.standard_resolution.url;
		var imgTag = '<img src="'
			+ imgUrl
			+ '" alt="'
			+ photo.caption.text
			+ '" />';
		$("#instagramLink").html(
			"Latest snapshot: " + linkStart + "\"" + photo.caption.text +"\"</a>"
		);

		$("#instagramPic").html(
			linkStart + imgTag + "</a>"
		);
	});
});