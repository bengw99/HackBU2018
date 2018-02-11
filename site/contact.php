<?php
	$myfile=fopen("contact.txt",w) or die("Unable to open file!");
	$txt = $GET_["name"];
	fwrite($myfile,$txt\t);
	$txt= $GET_["email"];
	fwrite($myfile,$txt\t);
	$txt= $GET_["phone"];
	fwrite($myfile,$txt: );
	$txt= $GET_["subject"];
	fwrite($myfile,$txt\n);
	$txt= $GET_["message"];
	fclose($myfile);
	?>