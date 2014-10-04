$.getJSON( "https://api.github.com/users/ramsesoriginal/events", function( data ) {
	var text = "<ul class=\"githubList\">";
	for (var i = 0; i<5; i++) {
		var current = data[i];
		var repoName = current.repo.name;
		var repoUrl = "https://github.com/"+repoName;
		if (current.type=="PushEvent") {
			text += "<li>Pushed to <a href=\""+repoUrl+"\">"+repoName+"</a>: <ul class=\"commitList\">";
			for (var j=0; j<current.payload.commits.length; j++) {
				var url = repoUrl + "/commits/" + current.payload.commits[j].sha;
				text+= "<li><a href=\"" +url + "\">" + current.payload.commits[j].message + "</a></li>";
			}
			text += "</ul></li>";
		} else if (current.type=="IssuesEvent") {
			text += "<li>Issue " + current.payload.action + " in <a href=\""+repoUrl+"\">"+repoName+"</a>:";
			text += "<a href=\""+current.payload.issue.html_url+"\">"+current.payload.issue.title+"</a>"
			text += "</li>";
		} else if (current.type=="PullRequestEvent") {
			text += "<li>Pull request " + current.payload.action + " for <a href=\""+repoUrl+"\">"+repoName+"</a>:";
			text += "<a href=\""+current.payload.pull_request.html_url+"\">"+current.payload.pull_request.title+"</a>"
			text += "</li>";
		}
	}
	text += "</ul>";

	$("#githubContent").html(text);
	/*var track = data.recenttracks.track[0];
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
	);*/
});