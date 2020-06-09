<?php
//create a rainbow for 10 leds on channel 1:  
send_to_leds_fill_red("fill 1,FF0000,0,13");  
function send_to_leds_fill_red ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
send_to_leds_fill_green("fill 1,00FF00,13,13");  
function send_to_leds_fill_green ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
send_to_leds_fill_blue("fill 1,0000FF,26,14");  
function send_to_leds_fill_blue ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
sleep(1);
echo "Car with 3 tabs"; 
?>
