<?php
//create a rainbow for 10 leds on channel 1:  
send_to_leds("setup 1,10;init;brightness 1,32;");  
function send_to_leds ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
?>
