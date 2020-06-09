<?php
//create a rainbow for 10 leds on channel 1:  
send_to_fill("fill 1,FFFFF,0,40");  
function send_to_fill ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}
send_to_blink("blink 1,FFFFFF,000000,500,10,0,40");   
function send_to_blink ($data){  
   $sock = fsockopen("127.0.0.1", 9999);  
   fwrite($sock, $data);  
   fclose($sock);  
}

echo "System Reset"; 
?>
