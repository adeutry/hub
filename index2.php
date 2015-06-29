<?php

$servername = "localhost";
$username = "root";
$password = "password";
$dbname =   "hub";

$boards = array("mu","g","lit","v");


try {
    $conn = new PDO("mysql:host=$servername;port=3306;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $results = array();
    
    foreach ($boards as $board){
    	
	$sql = "SELECT * FROM 4chan_$board ORDER BY replies DESC ";
    	$nodes = $conn->query($sql);
    	$result = $nodes->fetchAll();
	$results[] = $result;
    } 
    
    





print '<!DOCTYPE html>
<head>
<title>Ayy</title>
<link rel="stylesheet" type="text/css" href="style_2.css">
<link href="https://fonts.googleapis.com/css?family=RobotoDraft:400,500,700,400italic" rel="stylesheet" type="text/css">
<script language="javascript" type="text/javascript" src="jquery-2.1.4.min.js"></script>
<link href="http://fonts.googleapis.com/css?family=Noto+Sans" rel="stylesheet" type="text/css">
</head>

<body>';

foreach($results as $i=>$result){
	print "<div id=\"content_column_$i\" class=\"content_column\">";
		print "<div id=\"content_column_info_$i\" class=\"content_column_info\" >/".$boards[$i]."/</div>";

		foreach($result as $key=>$post){
			print "<div id=\"content_div_".$post['no']."\" class=\"content_div\">";
				print "<div class=\"content_subject\">".$post['subject']."</div>";
				print $post['body'];
				print "<div class=\"score_comments\">";
					print "<div class=\"score\" >".$post['replies']."</div>"; 
				print "</div>";
			print "</div>";
		}

	print "</div>";
}



print '<script language="javascript" type="text/javascript" src="hub.js"></script></body></html>';

	  }
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }
