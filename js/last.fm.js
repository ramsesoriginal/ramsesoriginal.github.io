if (document.enableLastFM) {
	$.getJSON( "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=ramsesoriginal&api_key=f94511b2a2a7e7dead1751d50ced0469&format=json", function( data ) {
		var track = data.recenttracks.track[0];
		var linkStart = '<a href="'
			+ track.url
			+ '" title="'
	  		+ track.name
			+ '">';
		var imgUrl = track.image[3]["#text"];
		var imgTag = '<img src="'
			+ imgUrl
			+ '" alt="'
			+ track.name
			+ '" />';

		$("#lastfmLink").html(
			"Latest listened song: " + linkStart + "\"" + track.name +"\"</a>"
		);

		$("#lastfmPic").html(
			linkStart + imgTag + "</a>"
		);

		$('#lastfmArtist').html(
			linkStart + " ~ " + track.artist["#text"] + "</a>"
		);
		
		if (document.masonryActive)
			$("main > .wrapper").masonry();
	});
}