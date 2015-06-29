<?php


print '<!DOCTYPE html>
<head>
<title>Ayy</title>
<link rel="stylesheet" type="text/css" href="style_2.css">
<link href="https://fonts.googleapis.com/css?family=RobotoDraft:400,500,700,400italic" rel="stylesheet" type="text/css">
<link href="http://fonts.googleapis.com/css?family=Noto+Sans" rel="stylesheet" type="text/css">
</head>

<body>';


$command = escapeshellcmd('/usr/local/bin/python3.4 /var/www/html/hub/reddit.py hot ');
$output = shell_exec($command);
print $output;

$command = escapeshellcmd('/usr/local/bin/python3.4 /var/www/html/hub/reddit.py top ');
$output = shell_exec($command);
print $output;


print '</body>';

?>
