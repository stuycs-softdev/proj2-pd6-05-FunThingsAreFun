$(document).ready(function() {
	$('.circle').slideUp(0);
	/*
	$.ajax({
	    type:'POST',
	    url: '/static/js/hello.py',
	    crossDomain:'TRUE',
	    success: function(data) {
		$('#generate').html($(data).text());
	    }
	});
	*/
	var f = function(x) {
	    console.log(x);
	    $('circle').slideUp('slow');
	    var html = '' +  
	    '<li>' + 
            '<div class="profile">' + 
                '<div>' + 
                    '<div class="container">' +
                        '<header>' + x.name + '</header>' + 
			'<img class="propic" src=' + x.image + '>' + 
                    '</div>' + 
                '</div>' + 
                '<div>' + 
                    '<div class="container">' + 
                        '<header>About</header>' + 
                        '<table>' + 
                            '<tr><td>Name</td><td>' + x.name + '</td></tr>' + 
                            '<tr><td>Location</td><td>' + x.location + '</td></tr>' + 
                            '<tr><td>Email</td><td>' + x.email + ' </td></tr>' + 
                            '<tr><td>Call me</td><td>' + x.cell + '</td></tr>' + 
                            '<tr><td>Seeking</td><td>' + x.ori + '</td></tr>' + 
                            '<tr><td>Hobbies</td><td>' + x.hobbies[0].hobby + ', ' + x.hobbies[1].hobby + ', ' + x.hobbies[2].hobby + '</td> </tr>' + 
                            '<tr><td>About me</td><td>' + x.about + '</td></tr>' + 
                        '</table>' + 
                    '</div>' + 
                '</div>' + 
                '<div>' + 
                    '<div class="container">' + 
                        '<header>Activity</header>' + 
			'<ul>' + 
			    '<li>' + 
				'<b>' + x.activity[0][2] + '</b>' + ': ' + x.activity[0][1] +
			    '</li>' + 	
                    '</div>' + 
                '</div>' + 
            '</div>' + 
	    '</li>'
	    $('.circle').slideUp('slow');
	    $('#prolist').prepend(html);
	}

	$('#generate').click(function() {
	    $('.circle').slideDown('slow');

	    console.log('starting');
	    jQuery.post('/gen',f);
	    console.log('genned');
	});
});
