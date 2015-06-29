
var url= "https://a.4cdn.org/v/thread/300663258.json";
url = 'proxy.php?url='+url;
$.ajax({
    url: url,
    dataType: 'json',
    success:  function (data) {
        console.log(data);
    }
});

$(".content_div").click(function(event) { 
	console.log("Got data: " + event.target.id);
 });
