<?php


print '<!DOCTYPE html>
<head>
<title>Ayy</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>';


$command = escapeshellcmd('python reddit.py hot ');
$output = shell_exec($command);
echo $output;

$command = escapeshellcmd('python reddit.py top ');
$output = shell_exec($command);
echo $output;


print '</body>';

?>