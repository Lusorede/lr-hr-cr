<?php
//create a rainbow for 10 leds on channel 1:  
send_to_leds("fill 1,FF0000,0,3");  
function send_to_leds ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
echo "This is Button1 that is selected"; 
?>
