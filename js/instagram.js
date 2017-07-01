if (document.enableInstagram)  {
	$(document).ready(function() {
		//access stuf here https://www.instagram.com/developer/clients/manage/
		// get it through https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=token
		var accessToken = '197139508.8f6d6de.0ef0152969fe44b79ea2511b2db695b5';
		if (document.location.hostname == "localhost") {
			accessToken = '197139508.de7d149.8f983cc103534c20a1fc1a8156c35373';
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
				+ '" onload="$(\'main > .wrapper\').masonry();" alt="'
				+ photo.caption.text
				+ '" />';
			$("#instagramLink").html(
				"Latest snapshot: " + linkStart + "\"" + photo.caption.text +"\"</a>"
			);

			$("#instagramPic").html(
				linkStart + imgTag + "</a>"
			);
			if (document.masonryActive)
				$("main > .wrapper").masonry();
		});
	});
}