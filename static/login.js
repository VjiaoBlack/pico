$("#registerbox").hide();
$("#heading").hide();
$("#loginbox").hide();
$("#confirmationbox").hide();


$(document).ready(function(){
$("#registerbox").hide();
$("#heading").hide();
$("#loginbox").hide();
$("#confirmationbox").hide();

	$("#heading").fadeIn(1000);
    
    $("#registerbox input").keypress(function(e) {
	if(e.which == 13) {
	   	$("#registerbox").off("mouseenter");
		$("#registerbox").fadeOut(500);
		$("#confirmationbox").delay(500).animate({"opacity": ".7"}, 1).fadeIn(500).mouseenter(function() {
			$(this).stop().animate({"opacity": ".7"}, "fast");
		});
	}
    });
    
	$("#registerbox").animate({"opacity": ".7"}, 1).fadeIn(1000).mouseenter(function() {
		$(this).stop().animate({"opacity": ".7"}, "fast");
	});

	$("#isregistered").click(function(){
		$("#registerbox").off("mouseenter");
		$("#registerbox").fadeOut(500);
		$("#loginbox").delay(500).animate({"opacity": ".7"}, 1).fadeIn(500).mouseenter(function() {
			$(this).stop().animate({"opacity": ".7"}, "fast");
		});
	})
	
	$("#notregistered").click(function(){
		$("#registerbox").on("mouseenter");
		$("#loginbox").off("mouseenter");
		$("#loginbox").fadeOut(500);
		$("#registerbox").delay(500).animate({"opacity": ".7"}, 1).fadeIn(500).mouseenter(function() {
			$(this).stop().animate({"opacity": ".7"}, "fast");
		});
	})

});
 
