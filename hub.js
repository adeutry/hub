

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



function createThreadBox( data,col , board , postNo)
{

	var offset = $("#content_div_"+col+"_"+board+"_"+postNo).offset().top;
	var column = "<div style=\"margin-top: "+ offset +"px;\" id=\"thread_column_" + board + "_" + postNo + "\" class=\"thread_column\" >";
		var posts = data['posts'];
		var replyDiv;
		for (var i = 0 ; i < posts.length ; i++ )
		{
			replyDiv = "<div id=\"reply_div_" + posts[i]['no'] + "\" class=\"reply_div\">";
				if(posts[i]['tim'] != null){
				replyDiv += "<img width =\"70\" height=\"70\" src=\"http://i.4cdn.org/" + board + "/" + posts[i]['tim'] +"s.jpg\" >"; }
				replyDiv += posts[i].com;		
			replyDiv += "</div>";
			column+=replyDiv;
		}
	column += "</div>";
	$("#content_column_" + col).after(column);


} 

function getPostData( col,board , postNo)
{
	var posts;
	var url= "https://a.4cdn.org/" + board + "/thread/" + postNo +".json";
	url = 'proxy.php?url='+url;
	$.ajax({
	    url: url,
	    dataType: 'json',
	    success:  function (data) 
            {
		createThreadBox(data , col , board , postNo);		
            }
	});
	
	return posts;

}







$(".content_div").click(function(event) { 
	var data = event.target.id;
	console.log("Got data: " + data);
	var col = data.charAt(data.indexOf("_div_")+5);
	var board = data.slice( data.indexOf("_div_") + 7,data.lastIndexOf("_"));
	var postNo = data.slice(data.lastIndexOf("_")+1);
	console.log("col: " + col +"\nboard: " + board + "\npostNo :" + postNo );
	getPostData(col,board, postNo)

 });



