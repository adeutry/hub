

var d;
var url= "https://a.4cdn.org/g/thread/48721670.json";
url = 'proxy.php?url='+url;
$.ajax({
    url: url,
    dataType: 'json',
    success:  function (data) {
        d = data;
    }
});

$(".content_div").click(function(event) { 
	var data = event.target.id;
	console.log("Got data: " + data);
	var col = data.charAt(data.indexOf("_div_")+5);
	var board = data.slice( data.indexOf("_div_") + 7,data.lastIndexOf("_"));
	var postNo = data.slice(data.lastIndexOf("_")+1);
	console.log("col: " + col +"\nboard: " + board + "\npostNo :" + postNo );
	getPostData(board, postNo);
 });


function getPostData ( board , postNo)
{
	var posts;
	var url= "https://a.4cdn.org/" + board + "/thread/" + postNo +".json";
	url = 'proxy.php?url='+url;
	$.ajax({
	    url: url,
	    dataType: 'json',
	    success:  function (data) 
            {
		posts = data['posts'];
		for(var i =0; i < posts.length ; i++)
		{
			console.log(posts[i]['com']);
		}
            }
	});
	


}
