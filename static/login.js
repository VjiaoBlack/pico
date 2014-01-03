$("#registerbox").hide();
$("#heading").hide();
$("#loginbox").hide();


$(document).ready(function(){
	$("#registerbox").hide();
$("#heading").hide();
$("#loginbox").hide();

	$("#heading").fadeIn(1000);


	$("#registerbox").animate({"opacity": ".7"}, 1).fadeIn(1000).mouseenter(function() {
		$(this).stop().animate({"opacity": ".7"}, "fast");
	});
	$("#registerbox").mouseleave(function() {
		$(this).stop().animate({"opacity": ".4"}, "fast"); 
	});


	$("#isregistered").click(function(){
		$("#registerbox").off("mouseleave mouseenter");
		$("#registerbox").fadeOut(500);
		$("#loginbox").delay(500).animate({"opacity": ".7"}, 1).fadeIn(500).mouseenter(function() {
			$(this).stop().animate({"opacity": ".7"}, "fast");
		});
		$("#loginbox").mouseleave(function() {
			$(this).stop().animate({"opacity": ".4"}, "fast"); 
		});
	})
	
	$("#notregistered").click(function(){
		$("#registerbox").on("mouseleave mouseenter");
		$("#loginbox").off("mouseleave mouseenter");
		$("#loginbox").fadeOut(500);
		$("#registerbox").delay(500).animate({"opacity": ".7"}, 1).fadeIn(500).mouseenter(function() {
			$(this).stop().animate({"opacity": ".7"}, "fast");
		});
		$("#registerbox").mouseleave(function() {
			$(this).stop().animate({"opacity": ".4"}, "fast"); 
		});
	})

});
 
