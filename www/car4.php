<?php
//create a rainbow for 10 leds on channel 1:  
send_to_leds_fill_red("fill 1,FF0000,0,10");  
function send_to_leds_fill_red ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
send_to_leds_fill_green("fill 1,00FF00,10,10");  
function send_to_leds_fill_green ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
send_to_leds_fill_blue("fill 1,0000FF,20,10");  
function send_to_leds_fill_blue ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
send_to_leds_fill_yellow("fill 1,FFFF00,30,10");  
function send_to_leds_fill_yellow ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
sleep(1);
echo "Car with 4 tabs"; 
?>
