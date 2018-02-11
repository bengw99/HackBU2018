<?php
	$myfile=fopen("contact.txt",w+)
	$txt = $GET_["name"];
	fwrite($myfile,$txt);
	$txt= $GET_["email"];
	fwrite($myfile,$txt);
	$txt= $GET_["phone"];
	fwrite($myfile,$txt);
	$txt= $GET_["subject"];
	fwrite($myfile,$txt);
	$txt= $GET_["message"];
	fclose($myfile);
	?>